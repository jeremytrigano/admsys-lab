# TP12 - PowerShell

> Théorie : [[../Cours - PowerShell Bases]] · [[../Cours - PowerShell Scripts AD]] · [[../Cours - PowerShell Scripts Administration]]
> Captures : `99-Captures/TP12/` · Prérequis : [[TP11-GPO]]

## Objectif

Découvrir l'administration système avec PowerShell en automatisant plusieurs tâches courantes :

- obtenir des informations sur le système ;
- administrer Active Directory ;
- exporter des données ;
- créer des scripts réutilisables.

À l'issue de ce TP, vous disposerez d'une première boîte à outils PowerShell pour administrer votre laboratoire.

---

## Prérequis

- [v] [[TP11-GPO]] validé

---

# Étapes

## 1. Ouverture de PowerShell

Sur **SRV-DC01**, ouvrir PowerShell en tant qu'administrateur.

Vérifier la version installée :

```powershell
$PSVersionTable.PSVersion
```

![[../../99-Captures/TP12/01-version.png]]
_Version de PowerShell_

---

## 2. Informations système

Afficher quelques informations sur le serveur :

```powershell
Get-ComputerInfo |
Select-Object WindowsProductName, OsArchitecture, CsTotalPhysicalMemory
```

Afficher également :

```powershell
Get-PSDrive -PSProvider FileSystem
```

Repérer :

- les lecteurs disponibles ;
- l'espace libre.

![[../../99-Captures/TP12/02-systeme.png]]
_Informations système et lecteurs_

---

## 3. Services Windows

Afficher les services démarrés :

```powershell
Get-Service |
Where-Object {$_.Status -eq "Running"}
```

Puis les services arrêtés configurés en démarrage automatique :

```powershell
Get-Service |
Where-Object {
    $_.Status -eq "Stopped" -and
    $_.StartType -eq "Automatic"
}
```

![[../../99-Captures/TP12/03-services.png]]
_Services Windows_

---

## 4. Import du module Active Directory

Charger le module :

```powershell
Import-Module ActiveDirectory
```

Vérifier que le module est disponible :

```powershell
Get-Module ActiveDirectory
```

![[../../99-Captures/TP12/04-module.png]]
_Module Active Directory_

---

## 5. Lister les utilisateurs

Afficher les utilisateurs du domaine :

```powershell
Get-ADUser -Filter *
```

Afficher uniquement :

```powershell
Get-ADUser -Filter * |
Select-Object Name, SamAccountName
```

![[../../99-Captures/TP12/05-utilisateurs.png]]
_Liste des utilisateurs_

---

## 6. Exporter les utilisateurs

Exporter les utilisateurs dans un fichier CSV.

Créer le dossier :

```
C:\Exports
```

Puis exécuter :

```powershell
Get-ADUser -Filter * -Properties DisplayName, EmailAddress |
Select-Object Name, DisplayName, EmailAddress |
Export-Csv C:\Exports\utilisateurs.csv -NoTypeInformation -Encoding UTF8
```

Ouvrir ensuite le fichier CSV afin de vérifier son contenu.

![[../../99-Captures/TP12/06-export.png]]
_Export CSV_

---

## 7. Créer un utilisateur avec PowerShell

Créer un nouvel utilisateur :

```powershell
New-ADUser `
    -Name "Marie Martin" `
    -SamAccountName "mmartin" `
    -UserPrincipalName "mmartin@lab.local" `
    -Path "OU=Production,DC=lab,DC=local" `
    -AccountPassword (ConvertTo-SecureString "MotDePasse123!" -AsPlainText -Force) `
    -Enabled $true
```

Vérifier sa création :

```powershell
Get-ADUser mmartin
```

![[../../99-Captures/TP12/07-create-user.png]]
_Création d'un utilisateur_

---

## 8. Ajouter un utilisateur à un groupe

Ajouter l'utilisateur au groupe Production :

```powershell
Add-ADGroupMember `
-Identity "GRP-Production-RW" `
-Members "mmartin"
```

Vérifier les membres du groupe :

```powershell
Get-ADGroupMember "GRP-Production-RW"
```

![[../../99-Captures/TP12/08-groupes.png]]
_Ajout à un groupe_

---

## 9. Comptes inactifs

Lister les comptes n'ayant pas ouvert de session depuis 90 jours :

```powershell
$Date = (Get-Date).AddDays(-90)

Get-ADUser `
-Filter {LastLogonDate -lt $Date} `
-Properties LastLogonDate |
Select-Object Name, SamAccountName, LastLogonDate
```

Observer le résultat.

![[../../99-Captures/TP12/09-inactifs.png]]
_Comptes inactifs depuis 1 jour_

---

## 10. Création d'un script

Créer le dossier :

```
C:\Scripts
```

Créer un fichier :

```
Inventaire.ps1
```

Y copier :

```powershell
Get-ComputerInfo |
Select-Object WindowsProductName, OsArchitecture

Get-PSDrive -PSProvider FileSystem

Get-Service |
Where-Object {$_.Status -eq "Stopped" -and $_.StartType -eq "Automatic"}
```

Enregistrer puis exécuter le script :

```powershell
.\Inventaire.ps1
```

![[../../99-Captures/TP12/10-script.png]]
_Premier script PowerShell_

---

## Validation

- [v] PowerShell est fonctionnel
- [v] Les informations système sont affichées
- [v] Les services Windows sont listés
- [v] Le module Active Directory est chargé
- [v] Les utilisateurs sont exportés au format CSV
- [v] Un utilisateur est créé en PowerShell
- [v] L'utilisateur est ajouté à un groupe
- [v] Les comptes inactifs sont affichés
- [v] Un premier script PowerShell est créé

---

## Progression

| Étape | Lien |
| ----------------- | ------------------------------------------ |
| Prérequis | [[TP11-GPO]] |
| Suite recommandée | → [[../../05 - Sécurité/Cours - Sauvegardes]] |
| Branches | [[../Cours - PowerShell Scripts AD]] |
| Théorie | [[../Cours - PowerShell Bases]] · [[../Cours - PowerShell Scripts AD]] · [[../Cours - PowerShell Scripts Administration]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]