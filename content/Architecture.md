# Architecture

> Laboratoire SER8 — [[README]] · [[Inventaire]] · [[Procedures]] · [[Projet final - ACME Industries]]

## Schéma réseau

```text
                    Internet
                        │
                   [Routeur]
                        │
              192.168.1.0/24
                        │
        ┌───────────────┼───────────────┐
        │               │               │
     PVE-SR8        SRV-DC01      WIN11-CLIENT01
  192.168.1.200   192.168.1.210   192.168.1.211
   (Proxmox)      (DC/DNS/DHCP)   (Poste client)
```

## Machines

### PVE-SR8 — Hyperviseur Proxmox

- Hôte : `pve-sr8.lab.local`
- IP : `192.168.1.200/24`
- Passerelle : `192.168.1.254`

### SRV-DC01 — Contrôleur de domaine

- IP : `192.168.1.210`
- OS : Windows Server 2022 · VM ID : 100
- Services : AD, DNS, DHCP
- Annuaire : OU Direction, Production, Comptabilité — [[02 - Active Directory/TP/TP05-Creation-OU|TP05]]

### WIN11-CLIENT01 — Poste client

- IP : `192.168.1.211`
- OS : Windows 11 Pro · VM ID : 101
- Domaine : `lab.local`

### DEBIAN01 — Serveur Linux _(prévu)_

- Rôle : services Linux (module 05)
- OS : Debian

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
| Réseau | [[06 - Réseau/TP/TP10-Routage-et-segmentation|TP10]] |

## Évolution prévue

- [ ] DEBIAN01 (module 05)
- [ ] Segmentation réseau (TP10)
- [ ] GPO et serveur de fichiers (module 04)
- [ ] Sauvegardes (module 09)
- [ ] Microsoft 365 / Entra ID (module 08)
