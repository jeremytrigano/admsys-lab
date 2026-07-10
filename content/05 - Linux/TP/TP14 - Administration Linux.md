# TP14 - Administration Linux

> Théorie : [[../../05 - Linux/Cours 02 - Administration Linux]]  
> Captures : `99-Captures/TP14/` · Prérequis : [[TP13 - Installation et découverte Linux]]

## Objectifs

- Gérer les utilisateurs
- Appliquer des permissions
- Installer des logiciels
- Automatiser une tâche

## Contexte

La VM Linux est installée ([[TP13 - Installation et découverte Linux]]). Ce TP couvre l'administration système quotidienne.

## Prérequis

- [v] [[TP13 - Installation et découverte Linux]] validé
- [v] Accès sudo sur la VM

## Étapes

### 1. Utilisateurs

Créer :

```bash
sudo adduser technicien
```

Créer un groupe :

```bash
sudo groupadd admins
```

Ajouter l'utilisateur :

```bash
sudo usermod -aG admins technicien
```

### 2. Permissions

Créer un dossier :

```bash
mkdir /srv/projet
```

Modifier le propriétaire :

```bash
sudo chown technicien:admins /srv/projet
```

Modifier les droits :

```bash
chmod 770 /srv/projet
```

### 3. Processus

Afficher :

```bash
ps aux
```

Surveiller :

```bash
top
```

### 4. Cron

Créer une tâche :

```bash
crontab -e
```

Ajouter :

```bash
*/5 * * * * echo "test" >> ~/cron.log
```

## Validation

- [v] Utilisateur créé
- [v] Permissions fonctionnelles
- [v] Tâche cron exécutée

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[TP13 - Installation et découverte Linux]] |
| Suite recommandée | → [[TPxx - Services et réseau Linux]] |
| Branches | [[../../09 - Sécurité/Cours - Comptes privilégiés]] |
| Théorie | [[../../05 - Linux/Cours 02 - Administration Linux]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
