# Routage

> Voir aussi : [[Cours 01 - Fondamentaux réseau]] · [[Cours 03 - Commutation et VLAN]] · [[../../Architecture]]

## Qu'est-ce qu'un routeur ?

Un routeur relie plusieurs réseaux IP et prend des décisions de routage en fonction des tables de routage et des adresses de destination.

## Table de routage

Liste des réseaux connus et de la passerelle à utiliser pour les atteindre.

```bash
# Linux
ip route

# Windows
route print
```

## Route par défaut

Route utilisée quand aucune route plus spécifique ne correspond à la destination. Elle pointe généralement vers la passerelle Internet.

## NAT

Permet à un réseau privé d'accéder à Internet en traduisant les adresses privées en adresse publique.

Cas typique : laboratoire `192.168.10.0/24` → box domestique `192.168.1.0/24` → Internet.

## Double NAT

Situation où deux niveaux de NAT se succèdent (box + routeur intermédiaire). Peut compliquer certains accès, mais utile pour isoler un lab.

## Routage entre réseaux

Un routeur doit posséder une interface dans chaque réseau qu'il interconnecte.

Exemple :

```text
Internet
    │
Box Internet
192.168.1.1
    │
WAN
Routeur Linux / pfSense
LAN 192.168.10.1
    │
Switch
    │
Lab
```

## Différence Bridge / NAT dans Proxmox

| Mode | Comportement |
|------|--------------|
| Bridge (vmbr) | La VM est sur le même segment L2 que l'hôte |
| NAT | Proxmox crée un réseau isolé avec traduction d'adresses |

## Pourquoi un réseau de lab est isolé

- Éviter les conflits IP avec le réseau domestique
- Limiter l'impact d'une mauvaise configuration DHCP/DNS
- Reproduire une topologie proche d'un environnement professionnel
- Contrôler l'accès Internet du laboratoire

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[Cours 01 - Fondamentaux réseau]] |
| Suite recommandée | → [[Cours 03 - Commutation et VLAN]] |
| Branches | [[../../01 - Virtualisation/Cours - Hyperviseurs]] |
| TP associé | [[TP/TP17 - Mise en place d'un routeur]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
