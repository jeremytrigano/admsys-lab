# TP05 — Création des OU

> Théorie : [[../../02 - Active Directory/Cours - Active Directory]]  
> Captures : `99-Captures/TP05/` · Prérequis : [[TP04-Promotion-DC]]

## Objectif

Structurer l'annuaire Active Directory avec des unités d'organisation adaptées au laboratoire.

## Structure cible

```text
lab.local
├── Direction
├── Production
└── Comptabilité
```

## Prérequis

- [v] [[TP04-Promotion-DC]] validé
- [v] Accès administrateur au domaine

## Étapes

### 1. Création des OU

Créer les trois OU dans Active Directory Users and Computers.

![[../../99-Captures/TP05/01-creation-ou.png]]

### 2. Vérification

```powershell
Get-ADOrganizationalUnit -Filter * | Select-Object Name, DistinguishedName
```

![[../../99-Captures/TP05/02-verification-ou.png]]

## Bonnes pratiques

- Structurer par fonction, pas par personne
- Nommer les OU de façon explicite
- Documenter le schéma dans [[../../Architecture]]

## Validation

- [v] OU Direction créée
- [v] OU Production créée
- [v] OU Comptabilité créée

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[TP04-Promotion-DC]] |
| Suite recommandée | → [[TP06-Utilisateurs-et-groupes]] |
| Branches | — |
| Théorie | [[../../02 - Active Directory/Cours - Active Directory]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
