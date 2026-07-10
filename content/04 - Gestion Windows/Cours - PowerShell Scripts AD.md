# Scripts Active Directory

> Voir aussi : [[Cours - PowerShell Bases]] · [[../../02 - Active Directory/Cours - Active Directory]]

## Objectif

Automatiser la gestion des utilisateurs, groupes et postes dans Active Directory.

## Prérequis

```powershell
Import-Module ActiveDirectory
```

## Exemples de scripts

### Lister les utilisateurs inactifs (90 jours)

```powershell
$Date = (Get-Date).AddDays(-90)
Get-ADUser -Filter {LastLogonDate -lt $Date} -Properties LastLogonDate |
    Select-Object Name, SamAccountName, LastLogonDate
```

### Créer un utilisateur

```powershell
New-ADUser `
    -Name "Marie Martin" `
    -SamAccountName "mmartin" `
    -UserPrincipalName "mmartin@acme.local" `
    -Path "OU=Production,DC=acme,DC=local" `
    -AccountPassword (ConvertTo-SecureString "MotDePasse123!" -AsPlainText -Force) `
    -Enabled $true
```

### Ajouter un utilisateur à un groupe

```powershell
Add-ADGroupMember -Identity "GRP-Production-RW" -Members "mmartin"
```

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[Cours - PowerShell Bases]] · [[../../02 - Active Directory/Cours - Active Directory]] |
| Suite recommandée | → [[Cours - PowerShell Scripts Administration]] |
| Branches | - |
| TP associé | - |

> Suivi : [[00 - Administration du parcours/Progression]]
