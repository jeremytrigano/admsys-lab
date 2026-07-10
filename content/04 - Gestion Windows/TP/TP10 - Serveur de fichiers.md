# TP10 - Serveur de fichiers

> Théorie : [[../Cours - Fichiers et Permissions]]  
> Captures : `99-Captures/TP10/` · Prérequis : [[../../02 - Active Directory/TP/TP06-Utilisateurs-et-groupes]]

## Objectif

Mettre en place un serveur de fichiers centralisé en utilisant les bonnes pratiques Microsoft :

- création de partages réseau ;
- attribution des permissions NTFS ;
- utilisation de groupes Active Directory plutôt que de droits directs sur les utilisateurs ;
- validation des accès depuis un poste client.

À l'issue de ce TP, les utilisateurs disposeront d'un espace partagé propre à leur service.

---

## Architecture

Le serveur **SRV-DC01** hébergera plusieurs dossiers partagés.

```
D:\Partages
│
├── Direction
├── Production
└── Comptabilite
```

Chaque dossier sera accessible uniquement aux membres du groupe correspondant.

|Dossier|Groupe autorisé|
|---|---|
|Direction|GRP-Direction-RW|
|Production|GRP-Production-RW|
|Comptabilite|GRP-Comptabilite-RW|

---

## Prérequis

- [v] [[../../02 - Active Directory/TP/TP06-Utilisateurs-et-groupes]] validé
- [v] [[../../03 - DNS et DHCP/TP/TP09-DHCP]] validé

---

# Étapes

## 1. Création de l'arborescence

Sur **SRV-DC01**, créer le dossier :

```
D:\Partages
```

Créer ensuite les sous-dossiers :

```
Direction
Production
Comptabilite
```

L'arborescence obtenue doit être :

```
D:\Partages
│
├── Direction
├── Production
└── Comptabilite
```

![[../../99-Captures/TP10/01-arborescence.png]]  
_Arborescence des dossiers_

---

## 2. Vérification des groupes Active Directory

Ouvrir :

```
Outils
→ Utilisateurs et ordinateurs Active Directory
```

Vérifier l'existence des groupes :

- GRP-Direction-RW
- GRP-Production-RW
- GRP-Comptabilite-RW

![[../../99-Captures/TP10/02-groupes.png]]
_Groupes de sécurité_

---

## 3. Création des partages

Partager chacun des dossiers.

Exemple :

```
D:\Partages\Direction
```

Nom du partage :

```
Direction
```

Faire de même pour :

- Production
- Comptabilite

Conserver les paramètres par défaut pour les permissions de partage. Les restrictions seront principalement assurées par les permissions NTFS.

![[../../99-Captures/TP10/03-partages.png]]  
_Création des partages_

---

## 4. Configuration des permissions NTFS

Pour chaque dossier :

1. ouvrir **Propriétés**
2. onglet **Sécurité**
3. supprimer les autorisations inutiles si nécessaire ;
4. ajouter le groupe correspondant.

Exemple :

### Dossier Direction

Ajouter :

```
GRP-Direction-RW
```

Autoriser :

- Modifier
- Lecture et exécution
- Affichage du contenu
- Lecture
- Écriture

Procéder de la même manière pour les autres dossiers.

![[../../99-Captures/TP10/04-permissions.png]]  
_Permissions NTFS_

---

## 5. Vérification des accès depuis le client

Se connecter sur **WIN11-CLIENT01** avec un utilisateur appartenant au groupe :

```
GRP-Production-RW
```

Ouvrir :

```
\\SRV-DC01
```

Tester :

- ouverture du dossier Production ;
- création d'un fichier texte ;
- modification du fichier ;
- suppression du fichier.

Vérifier ensuite que l'utilisateur ne peut pas modifier les dossiers Direction ou Comptabilite.

![[../../99-Captures/TP10/05-test-acces.png]]
_Test des permissions_

---

## Validation

- [v] Les dossiers sont créés
- [v] Les partages sont publiés
- [v] Les permissions NTFS utilisent uniquement des groupes AD
- [v] Les utilisateurs autorisés peuvent modifier leur dossier
- [v] Les utilisateurs non autorisés sont refusés

---

## Progression

|Étape|Lien|
|---|---|
|Prérequis|[[../../02 - Active Directory/TP/TP06-Utilisateurs-et-groupes]]|
|Suite recommandée|→ [[TP11-GPO]]|
|Branches|[[../Cours - PowerShell Bases]]|
|Théorie|[[../Cours - Fichiers et Permissions]]|

> Suivi : [[../../00 - Administration du parcours/Progression]]