# TP22 - Migration et haute disponibilité Proxmox

> Théorie : [[../../07 - Virtualisation avancée/Cours 03 - Haute disponibilité, migration et sauvegarde]]  
> Captures : `99-Captures/TP22/` · Prérequis : [[TP19 - Stockage partage NFS Proxmox]] · [[TP20 - Creation d'un cluster Proxmox]] · [[TP21 - Quorum device Proxmox]]

## Objectif

Créer une VM sur stockage partagé, activer la HA, tester migration et bascule réelle.

## Prérequis HA (rappel)

| Élément | Statut requis |
|---------|---------------|
| Cluster 2 nœuds | [[TP20 - Creation d'un cluster Proxmox]] |
| Stockage partagé NFS | [[TP19 - Stockage partage NFS Proxmox]] — **pas** `local-lvm` |
| Quorum (3 votes) | [[TP21 - Quorum device Proxmox]] |

Sans NFS : le nœud survivant ne trouve pas le disque.  
Sans qdevice : le nœud survivant perd le quorum et **ne démarre pas** la VM HA.

## Prérequis

- [v] [[TP19 - Stockage partage NFS Proxmox]] validé
- [v] [[TP20 - Creation d'un cluster Proxmox]] validé
- [v] [[TP21 - Quorum device Proxmox]] validé (`pvecm status` = 3 votes)

## Partie 1 - Créer une VM sur NFS-Proxmox

Depuis pve-node01, créer `VM100` (Linux de test) :

| Paramètre | Valeur |
|-----------|--------|
| VM ID | 100 (exemple) |
| Stockage disque | **NFS-Proxmox** |
| Bridge | vmbr1 |

> Ne pas utiliser `local-lvm` pour une VM destinée à la HA.

Si une VM existe déjà sur `local-lvm`, déplacer le disque :

Interface :

```text
VM → Hardware → Hard Disk → Move Storage → NFS-Proxmox
```

ou CLI :

```bash
qm move_disk 100 scsi0 NFS-Proxmox
```

## Partie 2 - Migration à froid / en ligne

Migration arrêtée :

```text
VM → Migrate → PVE-Node02
```

Migration online (VM démarrée) :

```text
Migrate → Online migration
```

Observer temps de migration et impact réseau.

## Partie 3 - Activer la HA

```text
Datacenter → HA → Add → VM100
```

Vérification :

```bash
ha-manager status
```

Exemple attendu :

```text
quorum OK
vm:100 started PVE-Node01
```

## Partie 4 - Test de bascule

Sur le nœud qui héberge la VM (ex. PVE-Node01) :

```bash
shutdown -h now
```

Attendre environ **1 minute**, puis sur PVE-Node02 :

```bash
ha-manager status
```

Résultat attendu :

```text
vm:100 started PVE-Node02
```

La VM a redémarré sur le nœud survivant grâce au stockage NFS + quorum.

## Validation

- [v] VM sur `NFS-Proxmox` (pas `local-lvm`)
- [v] Migration à froid et/ou online documentée
- [v] HA activée (`ha-manager status`)
- [v] Bascule réelle testée (arrêt d'un nœud → VM sur l'autre)

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[TP19 - Stockage partage NFS Proxmox]] · [[TP20 - Creation d'un cluster Proxmox]] · [[TP21 - Quorum device Proxmox]] |
| Suite recommandée | → [[TP23 - Sauvegarde et restauration de VM]] |
| Branches | [[../../Architecture]] |
| Théorie | [[../../07 - Virtualisation avancée/Cours 03 - Haute disponibilité, migration et sauvegarde]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
