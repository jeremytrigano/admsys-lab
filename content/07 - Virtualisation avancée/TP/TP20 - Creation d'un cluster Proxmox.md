# TP20 - Création d'un cluster Proxmox

> Théorie : [[../../07 - Virtualisation avancée/Cours 01 - Architecture avancée de virtualisation]]  
> Captures : `99-Captures/TP20/` · Prérequis : [[TP18 - Preparation des noeuds Proxmox nested]] · [[TP19 - Stockage partage NFS Proxmox]]

## Objectif

Créer le cluster `LAB-CLUSTER` à deux nœuds.

## Contexte

Les nœuds **PVE-Node01** (`192.168.10.201`) et **PVE-Node02** (`192.168.10.202`) sont prêts. Le stockage `NFS-Proxmox` est disponible.

> À ce stade : **pas encore de HA**. Avec 2 nœuds seuls, la perte d'un nœud fait perdre le quorum (1 vote sur 2). Le quorum device sera ajouté au [[TP21 - Quorum device Proxmox]].

## Architecture

```text
PVE-Node01 (192.168.10.201)  <--Corosync-->  PVE-Node02 (192.168.10.202)
```

## Prérequis

- [v] [[TP18 - Preparation des noeuds Proxmox nested]] validé
- [v] [[TP19 - Stockage partage NFS Proxmox]] validé
- [ ] Accès Web `:8006` sur chaque nœud

## Étapes

### 1. Créer le cluster

Sur PVE-Node01 :

```bash
pvecm create LAB-CLUSTER
```

Vérification :

```bash
pvecm status
```

### 2. Ajouter PVE-Node02

Sur PVE-Node02 :

```bash
pvecm add 192.168.10.201
```

### 3. Vérifier

```bash
pvecm status
pvecm nodes
```

Résultat attendu :

```text
Quorate: Yes

Nodes:
1 PVE-Node01
2 PVE-Node02
```

Votes typiques à ce stade : **2** (1 par nœud). La HA reste fragile sans 3ᵉ vote.

## Validation

- [v] Cluster `LAB-CLUSTER` créé
- [v] `Quorate: Yes` avec les deux nœuds
- [v] Interface web unifiée (Datacenter) visible depuis les deux nœuds

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[TP18 - Preparation des noeuds Proxmox nested]] · [[TP19 - Stockage partage NFS Proxmox]] |
| Suite recommandée | → [[TP21 - Quorum device Proxmox]] |
| Branches | [[../../Architecture]] · [[../../Inventaire]] |
| Théorie | [[../../07 - Virtualisation avancée/Cours 01 - Architecture avancée de virtualisation]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
