# TP13 - Installation et découverte Linux

> Théorie : [[../../05 - Linux/Cours 01 - Linux]]  
> Captures : `99-Captures/TP13/` · Prérequis : [[../../04 - Gestion Windows/TP/TP12 - PowerShell]]

## Objectifs

- Installer un serveur Linux
- Découvrir l'environnement Linux
- Utiliser les commandes essentielles

## Contexte

Le laboratoire SER8 dispose d'une infrastructure virtualisée documentée dans [[../../Architecture]]. Ce TP pose les bases Linux avant l'administration serveur (DEBIAN01).

## Préparation

Créer une VM :

| Élément             | Valeur                                     |
| ------------------- | ------------------------------------------ |
| OS                  | Ubuntu Server LTS                          |
| RAM                 | 2 Go minimum                               |
| Disque              | 20 Go                                      |
| Réseau              | Même réseau que le lab (`192.168.1.0/24`)  |
| CPU                 | 1 à 2 vCPU                                 |
| Réseau              | Réseau interne du laboratoire via `vmbr1`  |
| Adresse IP attendue | `192.168.10.x/24`                          |
| Attribution IP      | DHCP fourni par le serveur Windows du labo |

## Prérequis

- [v] [[../../04 - Gestion Windows/TP/TP12 - PowerShell]] [[TP12 - PowerShell]] validé
- [v] Hyperviseur opérationnel ([[../../01 - Virtualisation/TP/TP01-Installation-Proxmox]])

## Étapes

### 1. Installation

Installer Ubuntu Server et créer un utilisateur administrateur.

Vérifier :

```bash
hostname
whoami
```

### 2. Mise à jour

```bash
sudo apt update
sudo apt upgrade
```

### 3. Navigation

Explorer :

```bash
/
```

Identifier :

```text
/etc
/home
/var
/tmp
```

### 4. Manipulation de fichiers

Créer :

```bash
mkdir ~/test-linux
touch fichier.txt
```

Copier :

```bash
cp fichier.txt ~/test-linux/
```

Déplacer :

```bash
mv fichier.txt ~/test-linux/
```

Supprimer :

```bash
rm fichier.txt
```

## Validation

- [v] La VM démarre correctement
- [v] Les commandes de base sont maîtrisées
- [v] L'arborescence Linux est comprise

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[../../04 - Gestion Windows/TP/TP12 - PowerShell]] |
| Suite recommandée | → [[TP14 - Administration Linux]] |
| Branches | - |
| Théorie | [[../../05 - Linux/Cours 01 - Linux]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
