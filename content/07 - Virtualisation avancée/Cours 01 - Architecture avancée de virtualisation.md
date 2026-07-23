# Architecture avancée de virtualisation

> Voir aussi : [[../../01 - Virtualisation/Cours - Virtualisation]] · [[../../01 - Virtualisation/Cours - Hyperviseurs]] · [[Cours 02 - Stockage avancé et réseaux virtuels]]

## Objectifs du chapitre 07

À la fin de ce chapitre, l'apprenant doit être capable de :

- Comprendre les architectures de virtualisation avancées
- Administrer un cluster d'hyperviseurs
- Gérer le stockage et les réseaux virtuels
- Réaliser des migrations de machines virtuelles
- Mettre en place des mécanismes de haute disponibilité
- Sauvegarder et restaurer des machines virtuelles
- Comprendre les notions utilisées dans les environnements professionnels (datacenter, cloud privé)

## Objectifs du cours

Comprendre les concepts permettant de construire une infrastructure virtualisée professionnelle.

## 1. Rappel - virtualisation classique

Dans une architecture simple :

```text
              Utilisateurs
                  |
              Réseau LAN
                  |
            +-------------+
            | Hyperviseur |
            |  Proxmox    |
            +-------------+
             /           \
            /             \
       VM Windows       VM Linux
```

Un seul serveur physique héberge plusieurs machines virtuelles.

Limites :

- panne du serveur = arrêt de toutes les VM
- ressources limitées au serveur
- maintenance difficile

## 2. Architecture cluster

Un cluster regroupe plusieurs hyperviseurs.

Exemple :

```text
              Cluster Proxmox

        +-------------+
        |   Node 01   |
        | Proxmox     |
        +-------------+
              |
        +-------------+
        |   Node 02   |
        | Proxmox     |
        +-------------+
              |
        +-------------+
        |   Node 03   |
        | Proxmox     |
        +-------------+
```

Avantages :

- haute disponibilité
- migration des VM
- maintenance sans interruption
- répartition de charge

## 3. Hyperviseur de type 1

Un hyperviseur de type 1 fonctionne directement sur le matériel.

Exemples :

- Proxmox VE
- VMware ESXi
- Microsoft Hyper-V Server

Architecture :

```text
Hardware
   |
Hyperviseur
   |
Machines virtuelles
```

Contrairement à :

```text
Hardware
   |
Windows
   |
VirtualBox
   |
VM
```

qui est un hyperviseur de type 2.

## 4. Ressources virtualisées

Un hyperviseur partage :

### CPU

Notions :

- vCPU
- sockets virtuels
- cores
- overcommit CPU

Exemple :

```text
CPU physique : 16 cores

VM1 : 4 vCPU
VM2 : 8 vCPU
VM3 : 8 vCPU

Total : 20 vCPU
```

Cela fonctionne grâce au partage temporel du processeur.

### Mémoire RAM

#### Ballooning

Une VM peut rendre de la mémoire inutilisée à l'hyperviseur.

#### Memory overcommit

Attribuer plus de RAM virtuelle que la RAM physique disponible.

Exemple :

```text
Serveur : 64 Go RAM

VM AD     :  8 Go
VM Linux  : 16 Go
VM SQL    : 32 Go
VM Test   : 16 Go

Total     : 72 Go
```

Possible, mais nécessite une surveillance.

## 5. Notions professionnelles

### Datacenter

Regroupement logique :

- clusters
- stockage
- réseau
- VM

### Provisioning

Création de ressources.

#### Thick provisioning

Réservation immédiate :

```text
Disque VM 500 Go = 500 Go utilisés
```

#### Thin provisioning

Allocation dynamique :

```text
Disque VM 500 Go
Réellement utilisé : 50 Go
```

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[../../01 - Virtualisation/Cours - Hyperviseurs]] · [[../../05 - Linux/TP/TP15 - Services et réseau Linux]] |
| Suite recommandée | → [[Cours 02 - Stockage avancé et réseaux virtuels]] |
| Branches | [[../../Architecture]] |
| TP associé | [[TP/TP18 - Preparation des noeuds Proxmox nested]] · [[TP/TP20 - Creation d'un cluster Proxmox]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
