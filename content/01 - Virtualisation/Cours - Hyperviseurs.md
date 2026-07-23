# Hyperviseurs

> Voir aussi : [[Cours - Virtualisation]] · [[TP/TP01-Installation-Proxmox]]

## Définition

Un hyperviseur est le logiciel qui crée et gère les machines virtuelles sur un hôte physique.

## Types

### Type 1 (bare metal)

Installé directement sur le matériel.

- VMware ESXi
- Microsoft Hyper-V
- Proxmox VE

### Type 2 (hébergé)

Installé comme application sur un OS hôte.

- VirtualBox
- VMware Workstation

## Comparaison rapide

| Hyperviseur | Licence | Usage typique |
|-------------|---------|---------------|
| VMware ESXi | Commerciale | Grandes entreprises |
| Hyper-V | Incluse Windows Server | Environnements Microsoft |
| Proxmox | Open source | PME, labos, hébergeurs |

## Concepts Proxmox

- **Node** : serveur physique Proxmox
- **VM** : machine virtuelle complète
- **CT (LXC)** : conteneur Linux léger
- **Storage** : stockage des disques VM
- **Bridge (vmbr0)** : réseau virtuel

## Bonnes pratiques

- Mettre à jour l'hyperviseur régulièrement
- Sauvegarder la configuration de l'hôte
- Monitorer l'utilisation CPU/RAM/disque
- Documenter chaque VM (rôle, IP, propriétaire)

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[Cours - Virtualisation]] |
| Suite recommandée | → [[TP/TP01-Installation-Proxmox]] |
| Branches | [[Architecture]] · [[../../06 - Réseau/Cours 01 - Fondamentaux réseau]] |
| TP associé | [[TP/TP01-Installation-Proxmox]] |

> Suivi : [[00 - Administration du parcours/Progression]]
