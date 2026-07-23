# TP18 - Préparation des nœuds Proxmox (Nested)

> Théorie : [[../../07 - Virtualisation avancée/Cours 01 - Architecture avancée de virtualisation]] · [[../../01 - Virtualisation/Cours - Hyperviseurs]]  
> Captures : `99-Captures/TP18/` · Prérequis : [[../../01 - Virtualisation/TP/TP01-Installation-Proxmox]] · [[../../06 - Réseau/TP/TP17 - Mise en place d'un routeur]]

## Objectif

Préparer deux nœuds Proxmox indépendants, prêts à former un cluster au TP suivant.

## Contexte

> Cette partie est à réaliser uniquement si vous ne disposez que d'un seul serveur physique Proxmox. Les deux futurs nœuds du cluster seront installés dans des machines virtuelles (**Nested Virtualization**).

## Prérequis

- [v] L'hyperviseur **PVE-SR8** est déjà installé ([[../../01 - Virtualisation/TP/TP01-Installation-Proxmox]])
- [v] [[../../06 - Réseau/TP/TP17 - Mise en place d'un routeur]] validé
- [v] L'ISO de **Proxmox VE** est disponible dans le stockage `local`
- [v] La virtualisation imbriquée (Nested Virtualization) est activée sur le serveur physique
- [v] Le réseau `vmbr1` permet aux deux futurs nœuds de communiquer

Pour vérifier si la virtualisation imbriquée est activée `cat /sys/module/kvm_amd/parameters/nested` doit retourner 1 (si Intel : `cat /sys/module/kvm_intel/parameters/nested`)

## Étapes

### 1. Créer la machine virtuelle `PVE-Node01`

Créer une nouvelle VM.

| Paramètre         | Valeur                   |
| ----------------- | ------------------------ |
| Nom               | `PVE-Node01`             |
| VM ID             | automatique              |
| OS                | **Do not use any media** |
| BIOS              | OVMF (UEFI)              |
| Machine           | q35                      |
| EFI Disk          | Oui                      |
| TPM               | Non                      |
| SCSI Controller   | VirtIO SCSI Single       |
| Disque            | 128 Go                   |
| Stockage          | local-lvm                |
| Cache             | Default                  |
| SSD Emulation     | Oui                      |
| Nombre de sockets | 1                        |
| Nombre de cœurs   | 4                        |
| Type              | host                     |
| RAM               | 8192 Mo                  |
| Ballooning        | Désactivé                |
| Carte réseau      | VirtIO                   |
| Bridge            | vmbr1                    |
| VLAN              | Aucun                    |

Créer ensuite la VM.

### 2. Monter l'ISO Proxmox

Dans la VM :

```text
Hardware
    CD/DVD Drive
        ISO Image
            proxmox-ve-*.iso
```

Cocher :

```text
Start at boot
```

### 3. Installer Proxmox VE

Démarrer la VM puis suivre l'installation.

Configurer :

| Paramètre  | Valeur                 |
| ---------- | ---------------------- |
| Hostname   | `pve-node01.lab.local` |
| Adresse IP | `192.168.10.201/24`    |
| Passerelle | `192.168.10.254`       |
| DNS        | `192.168.10.210`       |
| Domaine    | `lab.local`            |

Une fois l'installation terminée :

- retirer l'ISO
- redémarrer la VM

Vérifier que l'interface Web est accessible :

```text
https://192.168.10.201:8006
```

### 4. Créer `PVE-Node02`

Reproduire exactement les mêmes étapes.

Modifier uniquement :

| Paramètre  | Valeur                 |
| ---------- | ---------------------- |
| Nom        | `PVE-Node02`           |
| Hostname   | `pve-node02.lab.local` |
| Adresse IP | `192.168.10.202/24`    |

Le reste de la configuration est identique.

### 5. Vérifications

Depuis chaque nœud :

```bash
ping 192.168.10.201
ping 192.168.10.202
```

Les deux interfaces Web doivent être accessibles :

```text
https://192.168.10.201:8006
https://192.168.10.202:8006
```

Lorsque les deux nœuds communiquent correctement, poursuivre avec le stockage partagé ([[TP19 - Stockage partage NFS Proxmox]]), puis le cluster.

> **Important pour la HA :** `local-lvm` convient pour les disques des **hyperviseurs nested** eux-mêmes. Les VM qui seront protégées par la HA devront être stockées sur un **stockage partagé** (NFS, TP19). Avec seulement 2 nœuds, un **quorum device** (TP21) sera nécessaire pour éviter le split-brain.

## Remarque pédagogique

Pourquoi choisir **"Do not use any media"** lors de la création de la VM ?

L'assistant de création de Proxmox propose un type de système d'exploitation (Linux, Windows, etc.), mais ici nous allons installer **un hyperviseur** et non un système déjà présent.

Il est donc préférable de :

- créer une VM "vide" (`Do not use any media`)
- monter ensuite manuellement l'ISO de Proxmox VE
- démarrer sur cette ISO comme sur un serveur physique

Cette méthode reproduit exactement une installation réelle et évite certaines optimisations spécifiques à Linux ou Windows qui n'apportent rien ici.

## Validation

- [v] `PVE-Node01` installé (`192.168.10.201`) · Web :8006 OK
- [v] `PVE-Node02` installé (`192.168.10.202`) · Web :8006 OK
- [v] Ping croisé entre les deux nœuds OK

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[../../01 - Virtualisation/TP/TP01-Installation-Proxmox]] · [[../../06 - Réseau/TP/TP17 - Mise en place d'un routeur]] |
| Suite recommandée | → [[TP19 - Stockage partage NFS Proxmox]] |
| Branches | [[../../Architecture]] · [[../../Inventaire]] |
| Théorie | [[../../07 - Virtualisation avancée/Cours 01 - Architecture avancée de virtualisation]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
