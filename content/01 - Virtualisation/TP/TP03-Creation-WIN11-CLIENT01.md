# TP03 - Création WIN11-CLIENT01

> Théorie : [[../Cours - Hyperviseurs]] · [[../../Architecture]]  
> Captures : `99-Captures/TP03/` · Prérequis : [[TP02-Creation-SRV-DC01]]

## Objectif

Créer un poste utilisateur destiné à rejoindre le domaine Active Directory.

À la fin du TP :

```text
Proxmox
├── SRV-DC01       (192.168.1.210)
└── WIN11-CLIENT01 (192.168.1.211)
```

## Création de la VM

| Paramètre | Valeur |
|-----------|--------|
| Nom | WIN11-CLIENT01 |
| ID | 101 |

## Configuration système

```text
Machine : q35
BIOS : OVMF
TPM : Oui
QEMU Agent : Oui
```

## Ressources

```text
CPU : 2 vCPU
RAM : 8 Go
Disque : 80 Go
```

## Réseau

```text
vmbr0
VirtIO
```

### Capture recommandée

![[../../99-Captures/TP03/01-creation-vm.png]]
_Création VM terminé_

## Installation Windows 11

Choisir `Windows 11 Pro`.

## Installation du pilote réseau VirtIO

Pendant l'OOBE : **Installer un pilote** → `NetKVM\w11\amd64`

## Renommage

```text
WIN11-CLIENT01
```

## Configuration IP

| Élément | Valeur |
|---------|--------|
| IP | 192.168.1.211 |
| Masque | 255.255.255.0 |
| Passerelle | 192.168.1.254 |
| DNS | 192.168.1.210 |

Le DNS pointe déjà vers le futur contrôleur de domaine.

## Validation

Tester :

```powershell
ping 192.168.1.210
```

## Snapshot

Créer le snapshot `FreshInstall`.

![[../../99-Captures/TP03/02-bureau-win11.png]]
_Bureau Windows 11 avec nom du PC, adresse IP et connectivité réseau_

## Prérequis

- [v] [[TP02-Creation-SRV-DC01]] validé
- [v] ISO Windows 11 et VirtIO disponibles sur Proxmox

## Validation finale

- [v] VM WIN11-CLIENT01 créée (ID 101)
- [v] Windows 11 installé et renommé
- [v] IP statique `192.168.1.211` configurée
- [v] Connectivité vers SRV-DC01 vérifiée
- [v] Snapshot `FreshInstall` créé

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[TP02-Creation-SRV-DC01]] |
| Suite recommandée | → [[../../02 - Active Directory/TP/TP04-Promotion-DC]] |
| Branches | [[../../06 - Réseau/Cours 01 - Fondamentaux réseau]] |
| Théorie | [[../../02 - Active Directory/Cours - Active Directory]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
