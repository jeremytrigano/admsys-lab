# Scripts Administration

> Voir aussi : [[01-Bases]] · [[02-Scripts-AD]]

## Objectif

Scripts d'administration système courants (hors AD).

## Exemples

### Informations système

```powershell
Get-ComputerInfo | Select-Object WindowsProductName, OsArchitecture, CsTotalPhysicalMemory
```

### Services arrêtés

```powershell
Get-Service | Where-Object {$_.Status -eq "Stopped" -and $_.StartType -eq "Automatic"}
```

### Espace disque

```powershell
Get-PSDrive -PSProvider FileSystem |
    Select-Object Name,
        @{N="Libre(GB)";E={[math]::Round($_.Free/1GB,2)}},
        @{N="Total(GB)";E={[math]::Round(($_.Used+$_.Free)/1GB,2)}}
```

### Test de connectivité

```powershell
Test-Connection -ComputerName 192.168.1.10 -Count 2
Test-NetConnection -ComputerName 192.168.1.10 -Port 445
```

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[02-Scripts-AD]] |
| Suite recommandée | → [[../09 - Sécurité/Cours - Sauvegardes]] |
| Branches | [[../08 - Microsoft 365/Cours - Microsoft 365]] |
| TP associé | - |

> Suivi : [[00 - Administration du parcours/Progression]]
