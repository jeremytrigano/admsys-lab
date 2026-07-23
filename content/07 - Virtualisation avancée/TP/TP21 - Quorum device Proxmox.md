# TP21 - Quorum device Proxmox

> Théorie : [[../../07 - Virtualisation avancée/Cours 03 - Haute disponibilité, migration et sauvegarde]]  
> Captures : `99-Captures/TP21/` · Prérequis : [[TP20 - Creation d'un cluster Proxmox]]

## Objectif

Ajouter un quorum device pour obtenir 3 votes et permettre une vraie HA sur un cluster à 2 nœuds.

## Pourquoi ce TP

Proxmox utilise **Corosync** pour le quorum. Avec 2 nœuds seulement :

```text
PVE-Node01  <--->  PVE-Node02
```

Si PVE-Node01 tombe :

- PVE-Node02 n'a plus que 1 vote sur 2
- il perd le quorum
- les ressources HA restent **bloquées** (protection anti **split-brain**)

Solution pédagogique : un troisième vote via `corosync-qnetd` (qdevice).

```text
             Corosync

     PVE-Node01 -------- PVE-Node02
            \               /
             \             /
           SRV-QDEVICE
           (qnetd)
```

## Architecture

| Élément | Valeur |
|---------|--------|
| VM | `SRV-QDEVICE` |
| IP | `192.168.10.221/24` |
| OS | Debian / Ubuntu Server (léger) |
| Rôle | `corosync-qnetd` uniquement |
| Stockage VM HA | Non (pas de disques de VM) |

## Prérequis

- [v] [[TP20 - Creation d'un cluster Proxmox]] validé
- [v] Les deux nœuds du cluster en ligne

## Étapes

### 1. Créer SRV-QDEVICE

VM minimale :

| Paramètre         | Valeur            |
| ----------------- | ----------------- |
| Nom               | SRV-QDEVICE       |
| IP                | 192.168.10.221/24 |
| Passerelle        | 192.168.10.254    |
| DNS               | 192.168.10.210    |
| Start at boot     | Activé            |
| Qemu Agent        | Activé            |
| Disque            | 16 Go             |
| SSD emulation     | Activé            |
| RAM               | 2 Go              |
| Ballooning Device | Désactivé         |
| Bridge            | vmbr1             |

### 2. Installer qnetd sur SRV-QDEVICE

```bash
sudo apt update
sudo apt install corosync-qnetd
sudo systemctl enable --now corosync-qnetd
```

### 3. Installer qdevice sur les nœuds Proxmox

Sur **PVE-Node01** et **PVE-Node02** :

```bash
apt update
apt install corosync-qdevice
```

### 4. Enregistrer le qdevice

Sur un nœud du cluster (ex. PVE-Node01) :

```bash
pvecm qdevice setup 192.168.10.221
```

### 5. Vérifier

```bash
pvecm status
```

Votes attendus :

```text
PVE-Node01   1
PVE-Node02   1
QDevice      1
Total        3
```

## Validation

- [v] `corosync-qnetd` actif sur SRV-QDEVICE
- [v] `pvecm qdevice setup` réussi
- [v] 3 votes visibles dans `pvecm status`
- [v] Cluster toujours `Quorate: Yes`

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[TP20 - Creation d'un cluster Proxmox]] |
| Suite recommandée | → [[TP22 - Migration et haute disponibilite Proxmox]] |
| Branches | [[../../Architecture]] · [[../../Inventaire]] |
| Théorie | [[../../07 - Virtualisation avancée/Cours 03 - Haute disponibilité, migration et sauvegarde]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
