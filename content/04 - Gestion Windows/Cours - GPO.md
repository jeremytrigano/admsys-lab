# GPO

> Voir aussi : [[../../02 - Active Directory/Cours - Active Directory]]

## Définition

Les GPO (Group Policy Objects) sont des stratégies de groupe appliquées automatiquement aux utilisateurs et postes du domaine.

## Utilisations

- Politique de mots de passe
- Fond d'écran et restrictions
- Mappage de lecteurs réseau
- Paramètres de sécurité Windows
- Déploiement de logiciels
- Redirection de dossiers

## Ordre d'application

```
Local  →  Site  →  Domaine  →  OU
```

En cas de conflit : **le plus spécifique gagne** (OU > Domaine > Site > Local).

## Types de paramètres

- **Computer Configuration** : s'applique au poste
- **User Configuration** : s'applique à l'utilisateur connecté

## Outils

| Outil | Usage |
|-------|-------|
| `gpmc.msc` | Gestion des GPO |
| `gpupdate /force` | Forcer l'application |
| `gpresult /r` | Voir les GPO appliquées |
| `rsop.msc` | Résultat des stratégies |

## Bonnes pratiques

- Nommer les GPO de façon explicite (ex. `GPO-MotDePasse-Domaine`)
- Éviter de lier trop de GPO à une même OU
- Tester sur une OU pilote avant déploiement global
- Documenter chaque GPO et son objectif

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[../../02 - Active Directory/Cours - Active Directory]] |
| Suite recommandée | → [[Cours - Fichiers et Permissions]] |
| Branches | [[09 - Sécurité/Cours - Comptes privilégiés]] |
| TP associé | - |

> Suivi : [[00 - Administration du parcours/Progression]]
