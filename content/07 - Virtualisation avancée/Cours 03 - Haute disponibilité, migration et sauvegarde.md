# Haute disponibilité, migration et sauvegarde

> Voir aussi : [[Cours 01 - Architecture avancée de virtualisation]] · [[Cours 02 - Stockage avancé et réseaux virtuels]] · [[../../09 - Sécurité/Cours - Sauvegardes]]

## Objectifs

Mettre en place une infrastructure résiliente.

## 1. Migration de VM

### Migration à froid

VM arrêtée.

```text
Node01
  |
Node02
```

### Migration à chaud

VM active.

Conditions :

- stockage partagé
- CPU compatibles
- réseau configuré

Exemple :

```text
Utilisateur connecté
        VM
Node01 -------- Node02
Migration sans coupure
```

## 2. Haute disponibilité (HA)

Objectif : redémarrer automatiquement une VM en cas de panne.

Exemple :

```text
        Cluster

Node01 X panne

VM déplacée automatiquement

Node02
 VM
```

### Prérequis Proxmox (essentiels)

1. **Stockage partagé** (NFS, Ceph, iSCSI…) — pas `local-lvm` pour les disques des VM HA
2. **Quorum** — avec 2 nœuds, ajouter un **qdevice** (3ᵉ vote) pour éviter le split-brain

Sans ces éléments, le menu HA peut être activé mais **aucune bascule réelle** ne fonctionnera.

## 3. Sauvegarde virtuelle

Types :

### Backup complet

Copie totale.

### Backup incrémental

Uniquement les changements.

Solutions :

- Proxmox Backup Server
- Veeam Backup
- Nakivo

### Règle 3-2-1

- **3** copies
- **2** supports différents
- **1** copie hors site

→ [[../../09 - Sécurité/Cours - Sauvegardes]]

## 4. Monitoring

Surveillance :

- CPU
- RAM
- stockage
- température
- réseau

Solutions :

- Zabbix
- Grafana
- Prometheus

→ prépare le module Supervision.

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[Cours 02 - Stockage avancé et réseaux virtuels]] |
| Suite recommandée | → [[../../08 - Microsoft 365/Cours - Microsoft 365]] |
| Branches | [[../../09 - Sécurité/Cours - Sauvegardes]] · [[../../10 - Supervision]] |
| TP associé | [[TP/TP21 - Quorum device Proxmox]] · [[TP/TP22 - Migration et haute disponibilite Proxmox]] · [[TP/TP23 - Sauvegarde et restauration de VM]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
