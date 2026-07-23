# Architecture

> Laboratoire SER8 - [[README]] · [[Inventaire]] · [[Procedures]] · [[Projet final - ACME Industries]]

## Schéma réseau

```text
Internet
    │
Freebox
192.168.1.1 / .254
    │
vmbr0 — 192.168.1.0/24 (domestique)
    │
    ├── PVE-SR8 ………… 192.168.1.200
    └── SRV-RT01 ……… ens18 DHCP (WAN)
            │
            │ ens19 = 192.168.10.254
            │
        vmbr1 — 192.168.10.0/24 (lab isolé)
            │
            ├── SRV-DC01 ……… 192.168.10.210  (AD, DNS, DHCP)
            ├── WIN11-CLIENT01  DHCP / 192.168.10.x
            └── DEBIAN01 ……… prévu (après TP15)
```

Routeur lab : [[06 - Réseau/TP/TP17 - Mise en place d'un routeur|TP17]] · Passerelle lab : `192.168.10.254`

## Machines

### PVE-SR8 - Hyperviseur Proxmox

- Hôte : `pve-sr8.lab.local`
- IP : `192.168.1.200/24` (vmbr0)
- Passerelle : Freebox (`192.168.1.1` / `192.168.1.254`)

### SRV-RT01 - Routeur Linux

- Hôte : `srv-rt01.lab.local`
- OS : Ubuntu Server
- Rôle : Routage + NAT entre réseau domestique et lab
- Interfaces :
  - `ens18` → vmbr0 (WAN) · DHCP sur `192.168.1.0/24`
  - `ens19` → vmbr1 (LAN) · `192.168.10.254/24`
- Services : `ip_forward`, iptables MASQUERADE + FORWARD
- TP : [[06 - Réseau/TP/TP17 - Mise en place d'un routeur|TP17]]

### SRV-DC01 - Contrôleur de domaine

- IP : `192.168.10.210` (vmbr1)
- OS : Windows Server 2022 · VM ID : 100
- Services : AD, DNS, DHCP
- Passerelle DHCP (option 003) : `192.168.10.254`
- Annuaire : OU Direction, Production, Comptabilité - [[02 - Active Directory/TP/TP05-Creation-OU|TP05]]

### WIN11-CLIENT01 - Poste client

- Réseau : `192.168.10.0/24` (vmbr1) · DHCP
- OS : Windows 11 Pro · VM ID : 101
- Domaine : `lab.local`
- Passerelle : `192.168.10.254`

### DEBIAN01 - Serveur Linux _(prévu)_

- Réseau : `192.168.10.0/24` (vmbr1)
- Rôle : services Linux (module 05)
- OS : Debian / Ubuntu
- Passerelle : `192.168.10.254`
- TP : [[05 - Linux/TP/TP15 - Services et réseau Linux|TP15]] (après TP17)

## Domaine

- Nom : `lab.local`
- NetBIOS : `LAB`
- Structure AD ([[02 - Active Directory/TP/TP05-Creation-OU|TP05]] validé) :

```text
lab.local
├── Direction
├── Production
└── Comptabilité
```

## TP par couche

| Couche | TP |
|--------|-----|
| Virtualisation | [[01 - Virtualisation/TP/TP01-Installation-Proxmox|TP01]] · [[01 - Virtualisation/TP/TP02-Creation-SRV-DC01|TP02]] · [[01 - Virtualisation/TP/TP03-Creation-WIN11-CLIENT01|TP03]] |
| Active Directory | [[02 - Active Directory/TP/TP04-Promotion-DC|TP04]] · [[02 - Active Directory/TP/TP05-Creation-OU|TP05]] · [[02 - Active Directory/TP/TP06-Utilisateurs-et-groupes|TP06]] · [[02 - Active Directory/TP/TP07-Jonction-poste-client|TP07]] |
| DNS et DHCP | [[03 - DNS et DHCP/TP/TP08-DNS|TP08]] · [[03 - DNS et DHCP/TP/TP09-DHCP|TP09]] |
| Linux | [[05 - Linux/TP/TP13 - Installation et découverte Linux|TP13]] · [[05 - Linux/TP/TP14 - Administration Linux|TP14]] · [[05 - Linux/TP/TP15 - Services et réseau Linux|TP15]] |
| Réseau | [[06 - Réseau/TP/TP16 - Analyse du réseau|TP16]] · [[06 - Réseau/TP/TP17 - Mise en place d'un routeur|TP17]] |
| Virtualisation avancée | [[07 - Virtualisation avancée/TP/TP18 - Preparation des noeuds Proxmox nested|TP18]] · [[07 - Virtualisation avancée/TP/TP19 - Stockage partage NFS Proxmox|TP19]] · [[07 - Virtualisation avancée/TP/TP20 - Creation d'un cluster Proxmox|TP20]] · [[07 - Virtualisation avancée/TP/TP21 - Quorum device Proxmox|TP21]] · [[07 - Virtualisation avancée/TP/TP22 - Migration et haute disponibilite Proxmox|TP22]] · [[07 - Virtualisation avancée/TP/TP23 - Sauvegarde et restauration de VM|TP23]] |
| Téléphonie IP | [[12 - Téléphonie IP/TP/TP43-Installer-un-IPBX|TP43]] · [[12 - Téléphonie IP/TP/TP44-Creer-des-extensions|TP44]] · [[12 - Téléphonie IP/TP/TP45-Configurer-un-softphone|TP45]] |

## Évolution prévue

- [v] Routeur lab et accès Internet ([[06 - Réseau/TP/TP17 - Mise en place d'un routeur|TP17]] - SRV-RT01)
- [ ] DEBIAN01 (module 05 - [[05 - Linux/TP/TP15 - Services et réseau Linux|TP15]], après TP17)
- [ ] Cluster Proxmox / NFS / qdevice / HA / backups ([[07 - Virtualisation avancée/TP/TP18 - Preparation des noeuds Proxmox nested|TP18]]–[[07 - Virtualisation avancée/TP/TP23 - Sauvegarde et restauration de VM|TP23]])
- [ ] GPO et serveur de fichiers (module 04)
- [ ] Sauvegardes (module 09)
- [ ] Microsoft 365 / Entra ID (module 08)
- [ ] Téléphonie IP - IPBX et extensions (module 12)
