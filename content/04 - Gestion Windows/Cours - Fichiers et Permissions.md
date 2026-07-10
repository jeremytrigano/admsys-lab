# Fichiers et Permissions

> Voir aussi : [[../../02 - Active Directory/Cours - Active Directory]] · [[Cours - GPO]]

## Définition

Le serveur de fichiers centralise le stockage et le partage de documents au sein de l'entreprise.

## Concepts

### Partage (Share)

Point d'accès réseau (`\\srv-fichiers\Comptabilite`).

### NTFS

Permissions au niveau du système de fichiers.

### Combinaison Share + NTFS

La permission la plus restrictive des deux s'applique.

## Niveaux de permissions NTFS

| Permission | Description |
|------------|-------------|
| Lecture | Consulter les fichiers |
| Écriture | Modifier et créer |
| Modifier | Lecture + écriture + suppression |
| Contrôle total | Tous les droits |

## Bonnes pratiques

- **Jamais** de droits directs sur les utilisateurs → utiliser des groupes AD
- Structurer les partages par service (Comptabilité, Direction, Production)
- Appliquer le principe du moindre privilège
- Auditer les accès sensibles
- Sauvegarder régulièrement → [[../09 - Sécurité/Cours - Sauvegardes]]

## Modèle ACME Industries

```
\\SRV-FILES\Direction
\\SRV-FILES\Production
\\SRV-FILES\Comptabilite
```

Groupes :

- `GRP-Direction-RW`
- `GRP-Production-RW`
- `GRP-Comptabilite-RW`

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[Cours - GPO]] |
| Suite recommandée | → [[Cours - PowerShell Bases]] |
| Branches | [[../09 - Sécurité/Cours - Sauvegardes]] |
| TP associé | - |

> Suivi : [[00 - Administration du parcours/Progression]]
