# Stockage avancé et réseaux virtuels

> Voir aussi : [[Cours 01 - Architecture avancée de virtualisation]] · [[Cours 03 - Haute disponibilité, migration et sauvegarde]] · [[../../06 - Réseau/Cours 03 - Commutation et VLAN]]

## Objectifs

Comprendre comment stocker les VM et construire un réseau virtuel.

## 1. Stockage en virtualisation

Les VM utilisent des volumes virtuels.

Formats courants :

- RAW
- QCOW2
- VMDK
- VHDX

Exemple :

```text
Stockage physique

SSD RAID
 |
 +---- VM Windows
 |
 +---- VM Linux
 |
 +---- VM Firewall
```

## 2. RAID

Objectifs :

- performance
- sécurité

### RAID 1

Miroir :

```text
Disque 1
  |
Disque 2
```

Tolérance à la panne d'un disque.

### RAID 5

Répartition + parité.

### RAID 10

Performance + sécurité.

## 3. Stockage partagé

Dans un cluster :

```text
        Proxmox 01
             |
        Stockage partagé
             |
        Proxmox 02
```

Solutions :

- NFS
- iSCSI
- Ceph
- SAN

Le stockage partagé est souvent requis pour la migration à chaud et la haute disponibilité.

## 4. Réseau virtuel

Un hyperviseur possède des switchs virtuels.

Exemple Proxmox :

```text
VM
 |
vmbr0
 |
Carte physique
 |
LAN
```

Dans le lab SER8 : `vmbr0` (domestique) et `vmbr1` (lab isolé) - voir [[../../Architecture]].

## 5. VLAN

Permet de séparer les réseaux.

Exemple :

```text
VLAN 10 - Serveurs
VLAN 20 - Clients
VLAN 30 - Administration
```

→ concepts détaillés : [[../../06 - Réseau/Cours 03 - Commutation et VLAN]]

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[Cours 01 - Architecture avancée de virtualisation]] |
| Suite recommandée | → [[Cours 03 - Haute disponibilité, migration et sauvegarde]] |
| Branches | [[../../06 - Réseau/Cours 03 - Commutation et VLAN]] |
| TP associé | [[TP/TP19 - Stockage partage NFS Proxmox]] · [[TP/TP20 - Creation d'un cluster Proxmox]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
