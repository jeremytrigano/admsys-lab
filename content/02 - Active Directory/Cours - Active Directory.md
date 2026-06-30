# Active Directory

> Voir aussi : [[../03 - DNS et DHCP/Cours - DNS]] · [[../04 - Gestion Windows/Cours - GPO]] · [[TP/TP04-Promotion-DC]] · [[00 - Administration du parcours/Préparation entretiens#02 — Active Directory]]

## Définition

Service d'annuaire Microsoft pour centraliser l'authentification et la gestion des identités.

## Rôle

Permet :

- Authentification
- Gestion des utilisateurs
- Gestion des groupes
- Gestion des postes

## Architecture

### Domaine

Unité de sécurité et d'administration.

Exemple : `lab.local`

### Forêt

Ensemble de domaines partageant un schéma commun.

### Contrôleur de domaine (DC)

Serveur hébergeant les services AD DS.

### OU (Unité d'organisation)

Conteneur logique pour structurer les objets.

Exemple :

```
lab.local
├── Direction
├── Production
└── Comptabilité
```

### Groupe

Permet d'attribuer des droits de manière centralisée. Toujours privilégier les groupes aux droits directs.

### Utilisateur

Compte permettant la connexion aux ressources du domaine.

## Authentification Kerberos

Voir le cours dédié : [[Cours - Authentification Kerberos]].

## Réplication

Les DC d'un même domaine répliquent l'annuaire entre eux (multi-master).

## Ports utilisés

| Port | Service |
|------|---------|
| 53 | DNS |
| 88 | Kerberos → [[Cours - Authentification Kerberos]] |
| 389 | LDAP |
| 445 | SMB |
| 636 | LDAPS |

## Flux d'authentification

Voir [[Cours - Authentification Kerberos]].

## Bonnes pratiques

- Utiliser des groupes pour les droits
- Éviter les droits directs sur les utilisateurs
- Structurer les OU par fonction, pas par personne
- Avoir au minimum 2 DC en production
- Protéger les comptes administrateurs → [[09 - Sécurité/Cours - Comptes privilégiés]]

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[../../01 - Virtualisation/TP/TP03-Creation-WIN11-CLIENT01]] |
| Suite recommandée | → [[../03 - DNS et DHCP/Cours - DNS]] |
| Branches | [[09 - Sécurité/Cours - Comptes privilégiés]] · [[../04 - Gestion Windows/Cours - PowerShell Scripts AD]] |
| TP associé | [[TP/TP04-Promotion-DC]] |

> Suivi : [[00 - Administration du parcours/Progression]]
