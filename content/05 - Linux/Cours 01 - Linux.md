# Linux

## Définition

Linux est un système d'exploitation libre basé sur le noyau Linux. Il est principalement utilisé sur les serveurs, dans le cloud, les équipements réseau et les supercalculateurs.

Une **distribution Linux** regroupe le noyau, des logiciels, un gestionnaire de paquets et des outils d'administration.

## Distributions courantes

| Distribution | Usage |
|--------------|-------|
| Ubuntu Server | Serveurs, cloud |
| Debian | Stable et légère |
| Rocky Linux | Compatible Red Hat |
| AlmaLinux | Alternative à RHEL |
| Red Hat Enterprise Linux (RHEL) | Entreprise avec support |
| Kali Linux | Tests de sécurité |

## Arborescence

Contrairement à Windows, Linux possède une arborescence unique commençant par :

```text
/
```

Répertoires principaux :

| Répertoire | Rôle |
|------------|------|
| `/home` | Dossiers utilisateurs |
| `/root` | Dossier de l'administrateur |
| `/etc` | Configuration système |
| `/var` | Journaux et données variables |
| `/tmp` | Fichiers temporaires |
| `/usr` | Applications |
| `/dev` | Périphériques |
| `/proc` | Informations du noyau |

## Le Shell

Le shell est l'interpréteur de commandes.

Le plus utilisé est **Bash**, mais il existe également `sh`, `zsh` et `fish`.

## Navigation

| Commande | Description |
|----------|-------------|
| `pwd` | Affiche le répertoire courant |
| `ls` | Liste les fichiers |
| `cd dossier` | Change de répertoire |
| `ls -l` | Affichage détaillé |
| `ls -la` | Inclure les fichiers cachés |

## Manipulation de fichiers

| Commande | Description |
|----------|-------------|
| `touch fichier` | Créer un fichier |
| `mkdir dossier` | Créer un dossier |
| `cp source destination` | Copier |
| `mv source destination` | Déplacer ou renommer |
| `rm fichier` | Supprimer un fichier |
| `rm -r dossier` | Supprimer un dossier |

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[../04 - Gestion Windows/Cours - PowerShell Bases]] |
| Suite recommandée | → [[Cours 02 - Administration Linux]] |
| Branches | [[Cours 03 - Réseau Linux]] |
| TP associé | [[TP/TP13 - Installation et découverte Linux]] |

> Suivi : [[../00 - Administration du parcours/Progression]]
