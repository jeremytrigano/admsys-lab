# TP07 — Jonction du poste client

> Théorie : [[../../02 - Active Directory/Cours - Active Directory]]  
> Captures : `99-Captures/TP07/` · Prérequis : [[TP06-Utilisateurs-et-groupes]]

## Objectif

Joindre WIN11-CLIENT01 au domaine `lab.local` et valider l'authentification d'un utilisateur du domaine.

## Architecture

| Élément | Valeur |
|---------|--------|
| Poste | WIN11-CLIENT01 |
| IP | 192.168.1.211 |
| Domaine | lab.local |
| DC | SRV-DC01 (192.168.1.210) |

## Prérequis

- [v] [[TP06-Utilisateurs-et-groupes]] validé
- [v] WIN11-CLIENT01 opérationnel
- [v] DNS du client pointant vers 192.168.1.210

## Étapes

### 1. Vérification de la résolution

```powershell
nslookup lab.local
ping srv-dc01.lab.local
```

![[../../99-Captures/TP07/01-verification-dns.png]]

### 2. Jonction au domaine

Paramètres → Système → Informations système → Domaine ou groupe de travail
Rejoindre un domaine → `lab.local`

![[../../99-Captures/TP07/02-jonction-domaine.png]]

### 3. Connexion utilisateur domaine

Se connecter avec un compte utilisateur créé au TP06.

![[../../99-Captures/TP07/03-connexion-domaine.png]]

## Validation

- [v] Poste joint au domaine `lab.local`
- [v] Redémarrage effectué
- [v] Connexion utilisateur domaine réussie

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[TP06-Utilisateurs-et-groupes]] |
| Suite recommandée | → [[../../03 - DNS et DHCP/TP/TP08-DNS]] |
| Branches | [[../../04 - Gestion Windows/Cours - GPO]] |
| Théorie | [[../../02 - Active Directory/Cours - Active Directory]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
