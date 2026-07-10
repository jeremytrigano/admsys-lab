# PowerShell - Bases

> Voir aussi : [[Cours - PowerShell Scripts AD]] · [[Cours - PowerShell Scripts Administration]] · [[00 - Administration du parcours/Préparation entretiens#04 - Gestion Windows]]

## Pourquoi PowerShell ?

Automatiser l'administration système, réduire les erreurs et gagner du temps sur les tâches répétitives.

## Commandes essentielles

```powershell
Get-Process
Get-Service
Get-ComputerInfo
Get-EventLog -LogName System -Newest 10
```

## Variables

```powershell
$Nom = "Jean Dupont"
$Age = 35
$Services = Get-Service
```

## Pipeline

Enchaîner les commandes avec `|` :

```powershell
Get-Service | Where-Object {$_.Status -eq "Running"}
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
```

## Cmdlets AD (module ActiveDirectory)

```powershell
Get-ADUser -Filter *
Get-ADGroup -Filter *
Get-ADComputer -Filter *
New-ADUser -Name "Jean Dupont" -SamAccountName "jdupont"
```

## Export de données

```powershell
Get-ADUser -Filter * -Properties DisplayName, EmailAddress |
    Select-Object Name, DisplayName, EmailAddress |
    Export-Csv utilisateurs.csv -NoTypeInformation -Encoding UTF8
```

## Bonnes pratiques

- Utiliser `-WhatIf` pour simuler avant d'exécuter
- Commenter les scripts
- Versionner les scripts dans un dépôt
- Tester sur un environnement de labo d'abord

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[Cours - Fichiers et Permissions]] |
| Suite recommandée | → [[Cours - PowerShell Scripts AD]] |
| Branches | [[../09 - Sécurité/Cours - Sauvegardes]] |
| TP associé | - |

> Suivi : [[00 - Administration du parcours/Progression]]
