# TP23 - Sauvegarde et restauration de VM

> Théorie : [[../../07 - Virtualisation avancée/Cours 03 - Haute disponibilité, migration et sauvegarde]] · [[../../09 - Sécurité/Cours - Sauvegardes]]  
> Captures : `99-Captures/TP23/` · Prérequis : [[TP22 - Migration et haute disponibilite Proxmox]]

## Objectif

Mettre en place une stratégie de sauvegarde et de restauration des machines virtuelles.

## Prérequis

- [v] [[TP22 - Migration et haute disponibilite Proxmox]] validé
- [v] Au moins une VM de test (idéalement sur `NFS-Proxmox`)
- [v] Destination de backup disponible (`NFS-Proxmox` ou autre stockage)

## Partie 1 - Backup manuel

```text
VM → Backup → Mode Snapshot
```

Vérifier la présence du fichier de sauvegarde sur le stockage cible.

## Partie 2 - Backup automatique

```text
Datacenter → Backup → Add
```

Paramètres recommandés :

- fréquence quotidienne
- stockage destination
- compression ZSTD

## Partie 3 - Restauration

1. Supprimer (ou renommer) une VM de test
2. Restaurer depuis :

```text
Backup → Restore
```

3. Vérifier le démarrage et la connectivité de la VM restaurée

## Validation

- [v] Sauvegarder et restaurer une VM

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[TP22 - Migration et haute disponibilite Proxmox]] |
| Suite recommandée | → [[../../08 - Microsoft 365/Cours - Microsoft 365]] |
| Branches | [[../../09 - Sécurité/Cours - Sauvegardes]] · [[../../12 - Téléphonie IP/TP/TP43-Installer-un-IPBX]] |
| Théorie | [[../../07 - Virtualisation avancée/Cours 03 - Haute disponibilité, migration et sauvegarde]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
