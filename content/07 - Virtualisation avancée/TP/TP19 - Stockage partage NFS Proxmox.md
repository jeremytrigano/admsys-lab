# TP19 - Stockage partagé NFS Proxmox

> Théorie : [[../../07 - Virtualisation avancée/Cours 02 - Stockage avancé et réseaux virtuels]]  
> Captures : `99-Captures/TP19/` · Prérequis : [[TP18 - Preparation des noeuds Proxmox nested]]

## Objectif

Mettre en place un stockage NFS partagé accessible par les deux nœuds Proxmox, prérequis indispensable à la HA.

## Pourquoi ce TP

Une VM sur `local-lvm` n'existe physiquement que sur un nœud. Si ce nœud tombe, l'autre ne retrouve pas le disque : **la HA est impossible**.

```text
PVE-Node01                          PVE-Node02
 |
 +-- local-lvm
       |
       +-- vm-100-disk-0   →   disque introuvable sur Node02
```

Architecture cible :

```text
        PVE-Node01 -------- PVE-Node02
              \                 /
               \               /
                SRV-NAS01 (NFS)
                 /srv/proxmox
```

## Architecture

| Élément          | Valeur                 |
| ---------------- | ---------------------- |
| VM               | `SRV-NAS01`            |
| IP               | `192.168.10.220/24`    |
| OS               | Debian / Ubuntu Server |
| Export NFS       | `/srv/proxmox`         |
| Clients          | `192.168.10.0/24`      |
| Stockage Proxmox | `NFS-Proxmox`          |

## Prérequis

- [ ] [[TP18 - Preparation des noeuds Proxmox nested]] validé
- [ ] PVE-Node01 et PVE-Node02 joignables sur `vmbr1`

## Étapes

### 1. Créer SRV-NAS01

Créer une VM légère sur PVE-SR8 (ou un nœud) :

| Paramètre  | Valeur                     |
| ---------- | -------------------------- |
| Nom        | SRV-NAS01                  |
| IP         | 192.168.10.220/24          |
| Passerelle | 192.168.10.254             |
| DNS        | 192.168.10.210             |
| Disque     | 100 Go (ou plus selon lab) |
| RAM        | 2 Go                       |
| Bridge     | vmbr1                      |

### 2. Installer NFS

```bash
sudo apt update
sudo apt install nfs-kernel-server
```

### 3. Créer et exporter le partage

```bash
sudo mkdir -p /srv/proxmox
sudo chown nobody:nogroup /srv/proxmox
sudo chmod 777 /srv/proxmox
```

Éditer `/etc/exports` :

```text
/srv/proxmox 192.168.10.0/24(rw,sync,no_subtree_check,no_root_squash)
```

Appliquer :

```bash
sudo exportfs -ra
sudo systemctl enable --now nfs-kernel-server
sudo exportfs -v
```

### 4. Tester depuis un nœud Proxmox

```bash
ping -c 2 192.168.10.220
showmount -e 192.168.10.220
```

Test de montage manuel (obligatoire) :

```bash
mkdir -p /mnt/test-nfs
mount -t nfs -o vers=3 192.168.10.220:/srv/proxmox /mnt/test-nfs
touch /mnt/test-nfs/ok.txt
umount /mnt/test-nfs
```

Scan Proxmox (peut être vide même si `showmount` OK) :

```bash
pvesm nfsscan 192.168.10.220
```

### 5. Ajouter le stockage dans Proxmox

#### Méthode recommandée (CLI)

Si le menu **Export** de l'interface reste vide après le scan, ajouter le stockage en ligne de commande depuis un nœud :

```bash
pvesm add nfs NFS-Proxmox \
  --server 192.168.10.220 \
  --export /srv/proxmox \
  --content images,iso,backup,vztmpl,snippets \
  --options vers=3
```

Vérifier :

```bash
pvesm status
cat /etc/pve/storage.cfg
```

#### Méthode interface Web

```text
Datacenter → Storage → Add → NFS
```

| Champ | Valeur |
|-------|--------|
| ID | NFS-Proxmox |
| Server | 192.168.10.220 |
| Export | `/srv/proxmox` (saisir manuellement si la liste est vide) |
| Version | **3** |
| Content | Disk image, ISO, Container, Backup, Snippets |
| Nodes | PVE-Node01, PVE-Node02 |

> **Piège fréquent :** `showmount` et `mount` OK, mais le déroulant Export reste vide.  
> Cause : le scan UI (`pvesm nfsscan`) échoue ou ne remonte rien. Contournement : **CLI `pvesm add nfs`** ou saisie manuelle du chemin d'export + **vers=3**.

Résultat attendu :

```text
PVE-Node01 → NFS-Proxmox (active)
PVE-Node02 → NFS-Proxmox (active)
```

## Validation

- [v] SRV-NAS01 joignable
- [v] Export NFS visible (`showmount -e`)
- [v] Stockage `NFS-Proxmox` présent sur les deux nœuds
- [v] Création d'un fichier test possible depuis les deux nœuds (même contenu)

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[TP18 - Preparation des noeuds Proxmox nested]] |
| Suite recommandée | → [[TP20 - Creation d'un cluster Proxmox]] |
| Branches | [[../../Architecture]] · [[../../Inventaire]] |
| Théorie | [[../../07 - Virtualisation avancée/Cours 02 - Stockage avancé et réseaux virtuels]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
