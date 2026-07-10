# TP08 - DNS

> Théorie : [[../Cours - DNS]]  
> Captures : `99-Captures/TP08/` · Prérequis : [[../02 - Active Directory/TP/TP07-Jonction-poste-client]]

## Objectif

Configurer et vérifier le service DNS intégré au domaine Active Directory.

## Contexte

Les postes et serveurs du laboratoire doivent résoudre les noms internes (`*.lab.local`).

## Architecture

| Élément | Valeur |
|---------|--------|
| Serveur DNS | SRV-DC01 (192.168.1.210) |
| Zone | lab.local |

## Prérequis

- [v] [[../02-Active-Directory/TP07-Jonction-poste-client]] validé
- [v] DNS installé avec AD DS

## Étapes

### 1. Vérification de la zone DNS

![[../../99-Captures/TP08/01-zone-dns.png]]

### 2. Enregistrements A

![[../../99-Captures/TP08/02-enregistrements-a.png]]

### 3. Tests de résolution

```powershell
nslookup lab.local
nslookup srv-dc01.lab.local
Resolve-DnsName lab.local
```

![[../../99-Captures/TP08/03-test-resolution.png]]

## Validation

- [v] Zone lab.local active
- [v] Résolution interne OK

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[../02-Active-Directory/TP07-Jonction-poste-client]] |
| Suite recommandée | → [[TP09-DHCP]] |
| Branches | - |
| Théorie | [[../Cours - DNS]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
