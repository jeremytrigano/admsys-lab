# TP17 - Mise en place d'un routeur

> Théorie : [[../../06 - Réseau/Cours 02 - Routage]] · [[../../06 - Réseau/Cours 01 - Fondamentaux réseau]]  
> Captures : `99-Captures/TP17/` · Prérequis : [[TP16 - Analyse du réseau]]

## Objectif

Créer un routeur entre le réseau domestique et le laboratoire pour donner accès à Internet tout en conservant l'isolation du lab.

## Contexte

Le laboratoire doit sortir vers Internet sans être directement mélangé au réseau domestique. Ce TP met en place la brique manquante du parcours réseau.

## Architecture

```text
Internet
    │
Box
192.168.1.1
    │
vmbr0
    │
SRV-RT01 (Ubuntu Server)
ens18 = DHCP (WAN)
ens19 = 192.168.10.254 (LAN)
    │
vmbr1
    │
Windows Server
Ubuntu
Windows 11
```

> Sous Proxmox / Ubuntu Server, les interfaces s'appellent généralement `ens18`, `ens19`… et non `eth0` / `eth1`. Vérifier avec `ip link`.

## Prérequis

- [v] [[TP16 - Analyse du réseau]] validé
- [v] Hyperviseur Proxmox opérationnel ([[../../01 - Virtualisation/TP/TP01-Installation-Proxmox]])
- [v] DHCP actif sur le lab ([[../../03 - DNS et DHCP/TP/TP09-DHCP]])

## Étapes

### 1. Créer la VM routeur

Créer une VM **Ubuntu Server** (`SRV-RT01`) avec **2 cartes réseau** :

| Interface (typique) | Réseau | Configuration |
|---------------------|--------|---------------|
| ens18 | vmbr0 (domestique / WAN) | DHCP |
| ens19 | vmbr1 (lab / LAN) | `192.168.10.254/24` |

Identifier les interfaces :

```bash
ip link
ip addr
```

### 2. Configurer Netplan (WAN DHCP / LAN statique)

> **Piège critique :** si `ens19` est en DHCP, elle reçoit l'option **003 Router** (`192.168.10.254`) et crée une **seconde route par défaut** vers elle-même.  
> Symptômes : `ping 8.8.8.8` OK (routes host), mais `curl` / `apt` vers Internet → `No route to host` (trafic sort via `ens19`).

Configurer explicitement :

```bash
ls /etc/netplan/
sudo nano /etc/netplan/00-installer-config.yaml
```

```yaml
network:
  version: 2
  ethernets:
    ens18:
      dhcp4: true
      dhcp4-overrides:
        route-metric: 100
    ens19:
      addresses:
        - 192.168.10.254/24
      dhcp4: false
```

Appliquer et vérifier :

```bash
sudo netplan apply
ip route
```

Table de routage **attendue** :

```text
default via 192.168.1.254 dev ens18 ...
192.168.1.0/24 dev ens18 ...
192.168.10.0/24 dev ens19 proto kernel scope link src 192.168.10.254
```

- **Une seule** route `default`, via `ens18` (Freebox)
- **Aucune** `default via 192.168.10.254 dev ens19`

Test depuis le routeur lui-même :

```bash
curl -4 -I --connect-timeout 10 https://archive.ubuntu.com
```

### 3. Activer le routage IPv4

Activation immédiate :

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

Rendre permanent (Ubuntu Server récent) via un fichier drop-in dans `/etc/sysctl.d/` :

```bash
echo 'net.ipv4.ip_forward=1' | sudo tee /etc/sysctl.d/99-ipforward.conf
sudo sysctl --system
```

> Sur les distributions modernes, `/etc/sysctl.conf` peut être absent ou minimal. La configuration recommandée se fait dans `/etc/sysctl.d/*.conf`.

### 4. Configurer le NAT et le forward

Le MASQUERADE seul ne suffit pas : il faut aussi autoriser le transit dans la chaîne `FORWARD`.

```bash
# NAT : le lab sort vers Internet via l'interface WAN (ens18)
sudo iptables -t nat -A POSTROUTING -o ens18 -j MASQUERADE

# Autoriser le trafic lab → WAN
sudo iptables -A FORWARD -i ens19 -o ens18 -j ACCEPT

# Autoriser les réponses WAN → lab
sudo iptables -A FORWARD -i ens18 -o ens19 -m state --state RELATED,ESTABLISHED -j ACCEPT
```

Vérifier :

```bash
sudo iptables -t nat -L -n -v
sudo iptables -L FORWARD -n -v
```

> Adapter `ens18` / `ens19` si `ip link` affiche d'autres noms.

Pour conserver les règles après redémarrage :

```bash
sudo apt install iptables-persistent
sudo netfilter-persistent save
```

### 5. Configurer la passerelle DHCP

Sur le serveur DHCP Windows, ajouter l'option **003 Router** :

```text
192.168.10.254
```

> Cette option est destinée aux **clients du lab**, pas à `ens19` du routeur. D'où l'intérêt du LAN en IP **statique** (`dhcp4: false`).

### 6. Tests

Depuis **SRV-RT01** :

```bash
ip route
curl -4 -I --connect-timeout 10 https://archive.ubuntu.com
```

Depuis un poste du lab (ex. WIN11-CLIENT01) :

```text
ping 192.168.10.254
ping 192.168.1.1
ping 8.8.8.8
ping google.com
```

Résultats attendus :

| Test | Attendu |
|------|---------|
| `ip route` (RT01) | 1 seule default via `ens18` |
| `curl` HTTPS (RT01) | OK |
| `192.168.10.254` | OK (passerelle LAN) |
| `192.168.1.1` | OK (box via NAT/forward) |
| `8.8.8.8` | OK (Internet) |
| `google.com` | OK (DNS + Internet) |

#### Dépannage rapide

| Symptôme | Cause probable | Action |
|----------|----------------|--------|
| 2× `default` (ens18 + ens19) | LAN en DHCP | Netplan : `ens19` statique, `dhcp4: false` |
| `ping 8.8.8.8` OK, `curl`/`apt` KO | Mauvaise default / sort via ens19 | Corriger Netplan puis `netplan apply` |
| Seul `192.168.10.254` répond (clients) | Forward / NAT | Vérifier `ip_forward` et iptables |

## Validation

- [v] VM routeur créée avec 2 interfaces (`ens18` / `ens19`)
- [v] Netplan : WAN DHCP, LAN statique `192.168.10.254/24`
- [v] Une seule route par défaut via `ens18`
- [v] Routage IPv4 activé
- [v] NAT + FORWARD configurés
- [v] Passerelle DHCP diffusée (clients lab)
- [v] Accès Internet fonctionnel depuis le lab (`curl` / `apt`)
- [v] Schéma mis à jour dans [[../../Architecture]]

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[TP16 - Analyse du réseau]] |
| Suite recommandée | → [[../../05 - Linux/TP/TP15 - Services et réseau Linux]] |
| Branches | [[../../Architecture]] |
| Théorie | [[../../06 - Réseau/Cours 02 - Routage]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
