# Virtualisation

> Voir aussi : [[Cours - Hyperviseurs]] · [[Architecture]] · [[TP/TP01-Installation-Proxmox]]

## Définition

La virtualisation consiste à exécuter plusieurs systèmes d'exploitation sur un même matériel physique.

## Objectifs

- Mutualiser le matériel
- Isoler les services
- Faciliter les sauvegardes
- Réduire les coûts

## Concepts importants

### Hôte

Machine physique qui exécute l'hyperviseur.

### Machine virtuelle (VM)

Ordinateur simulé, avec son propre OS, CPU, RAM et disque virtuels.

### Snapshot

Capture instantanée de l'état d'une VM. Permet un retour arrière rapide avant une modification risquée.

### Hyperviseur

Logiciel qui héberge et gère les VM. Voir [[02-Hyperviseurs]].

## Hyperviseurs connus

- VMware ESXi
- Hyper-V
- Proxmox

## À retenir

Les entreprises utilisent principalement :

- VMware (historique, entreprises matures)
- Hyper-V (écosystème Microsoft)
- Proxmox (open source, adoption croissante)

## Bonnes pratiques

- Toujours faire un snapshot avant une modification majeure
- Ne pas laisser les snapshots s'accumuler (impact performances)
- Dimensionner correctement RAM et CPU
- Séparer les réseaux (management, production, stockage)

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | - |
| Suite recommandée | → [[Cours - Hyperviseurs]] |
| Branches | [[../../06 - Réseau/Cours 01 - Fondamentaux réseau]] |
| TP associé | [[TP/TP01-Installation-Proxmox]] |

> Suivi : [[00 - Administration du parcours/Progression]]
