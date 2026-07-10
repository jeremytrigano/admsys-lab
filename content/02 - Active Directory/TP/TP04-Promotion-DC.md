# TP04 - Promotion du contrôleur de domaine

> Théorie : [[../../02 - Active Directory/Cours - Active Directory]]  
> Captures : `99-Captures/TP04/` · Prérequis : [[../../01 - Virtualisation/TP/TP03-Creation-WIN11-CLIENT01]]

## Objectif

Installer le rôle AD DS et promouvoir SRV-DC01 en contrôleur de domaine `lab.local`.

## Contexte

Le serveur SRV-DC01 est installé. Il doit devenir le point central d'authentification du laboratoire.

## Architecture

| Élément | Valeur        |
| ------- | ------------- |
| Serveur | SRV-DC01      |
| IP      | 192.168.1.210 |
| Domaine | lab.local     |

## Prérequis

- [v] [[../../01 - Virtualisation/TP/TP03-Creation-WIN11-CLIENT01]] validé
- [v] SRV-DC01 accessible avec IP statique

## Étapes

### 1. Installation du rôle AD DS

Server Manager → Add Roles and Features → Active Directory Domain Services

![[../../99-Captures/TP04/01-installation-role.png]]

### 2. Promotion en contrôleur de domaine

Créer une nouvelle forêt et le domaine `lab.local`.

![[../../99-Captures/TP04/02-promotion-domaine.png]]

### 3. Vérification

```powershell
Get-ADDomain
net share
Get-Service DFSR
dcdiag /test:sysvolcheck
dcdiag /test:advertising
```

![[../../99-Captures/TP04/03-verification-ad-01.png]]

![[../../99-Captures/TP04/03-verification-ad-02.png]]

![[../../99-Captures/TP04/03-verification-ad-03.png]]

![[../../99-Captures/TP04/03-verification-ad-04.png]]

![[../../99-Captures/TP04/03-verification-ad-05.png]]

## Résultat attendu

Domaine `lab.local` opérationnel avec SRV-DC01 comme premier contrôleur de domaine.

## Validation

- [v] Rôle AD DS installé
- [v] Domaine `lab.local` créé
- [v] Promotion DC réussie

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[../../01 - Virtualisation/TP/TP03-Creation-WIN11-CLIENT01]] |
| Suite recommandée | → [[TP05-Creation-OU]] |
| Branches | [[../../09 - Sécurité/Cours - Comptes privilégiés]] |
| Théorie | [[../../02 - Active Directory/Cours - Active Directory]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
