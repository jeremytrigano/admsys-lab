# Authentification Kerberos

> Voir aussi : [[Cours - Active Directory]] · [[00 - Administration du parcours/Préparation entretiens#02 - Active Directory]]

## Principe

```text
Utilisateur → demande TGT au DC → reçoit ticket → accès aux ressources
```

Kerberos est le protocole d'authentification par défaut dans un domaine Windows.

## Flux simplifié

```text
Utilisateur → AD → Validation Kerberos → Accès
```

1. Le poste contacte un contrôleur de domaine
2. Le client demande un **TGT** (Ticket Granting Ticket)
3. Le DC valide les identifiants
4. Le TGT permet d'obtenir des tickets de service pour les ressources
5. Pas de ressaisie du mot de passe à chaque accès

## Port associé

| Port | Service |
|------|---------|
| 88 | Kerberos |

## À retenir pour les entretiens

- Kerberos = authentification mutuelle client/serveur
- Le TGT a une durée de vie limitée
- La synchronisation horaire entre client et DC est critique (dérive > 5 min = échec)

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[Cours - Active Directory]] |
| Suite recommandée | → [[TP/TP04-Promotion-DC]] |
| Théorie | [[Cours - Active Directory]] |

> Suivi : [[00 - Administration du parcours/Progression]]
