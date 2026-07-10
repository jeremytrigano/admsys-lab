# Administration Linux

> Voir aussi : [[Cours 01 - Linux]]

## Utilisateurs et groupes

Les utilisateurs sont enregistrés dans :

- `/etc/passwd`
- `/etc/shadow`

Les groupes sont enregistrés dans :

- `/etc/group`

Commandes principales :

```bash
adduser utilisateur
userdel utilisateur
passwd utilisateur
groups utilisateur
id utilisateur
```

## Permissions

Affichage :

```bash
ls -l
```

Exemple :

```text
-rwxr-xr--
```

Correspondance :

- r : lecture
- w : écriture
- x : exécution

Modifier les permissions :

```bash
chmod 755 fichier
chmod 644 fichier
```

Changer le propriétaire :

```bash
chown utilisateur fichier
```

## sudo

Permet d'exécuter une commande avec les privilèges administrateur.

```bash
sudo commande
```

## Gestion des paquets

Debian / Ubuntu :

```bash
apt update
apt upgrade
apt install paquet
apt remove paquet
```

Rocky / AlmaLinux :

```bash
dnf install paquet
dnf update
dnf remove paquet
```

## Processus

Lister :

```bash
ps
ps aux
top
```

Arrêter :

```bash
kill PID
kill -9 PID
```

## Cron

Planification de tâches automatiques.

Éditer les tâches :

```bash
crontab -e
```

Afficher :

```bash
crontab -l
```

## Bash

Le shell Bash permet d'automatiser des tâches.

Exemple :

```bash
#!/bin/bash
echo "Bonjour"
```

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[Cours 01 - Linux]] |
| Suite recommandée | → [[Cours 03 - Réseau Linux]] |
| Branches | [[../09 - Sécurité/Cours - Comptes privilégiés]] |
| TP associé | [[TP/TP14 - Administration Linux]] |

> Suivi : [[../00 - Administration du parcours/Progression]]
