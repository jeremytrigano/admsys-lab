# Commutation et VLAN

> Voir aussi : [[Cours 02 - Routage]] · [[Cours 04 - Diagnostic réseau]] · [[../../Architecture]]

## Switch

Équipement de couche 2 qui transfère les trames Ethernet vers le bon port en fonction des adresses MAC.

## MAC Address

Identifiant physique (ou virtuel) d'une interface réseau. Le switch construit sa table MAC en observant le trafic.

## Broadcast

Trame envoyée à tous les équipements d'un même domaine de diffusion (broadcast domain). Trop de broadcasts dégradent les performances.

## VLAN

Virtual LAN : segmentation logique d'un réseau au niveau couche 2.

| VLAN | Usage type |
|------|------------|
| 10 | Serveurs |
| 20 | Utilisateurs |
| 30 | Management |
| 99 | Invités |

## Trunk

Lien entre switches (ou switch/routeur) transportant plusieurs VLAN avec étiquetage 802.1Q.

## Access Port

Port affecté à un seul VLAN. Utilisé pour connecter un poste, une imprimante ou un serveur.

## Inter-VLAN

Routage entre VLAN. Nécessite un équipement de couche 3 (routeur ou switch L3).

```text
VLAN 10 ──┐
VLAN 20 ──┼── Routeur L3 ── Internet
VLAN 30 ──┘
```

## Quand utiliser un VLAN

- Séparer les flux utilisateurs / serveurs / management
- Isoler un réseau invité
- Réduire la taille des domaines de broadcast
- Appliquer des politiques de sécurité par segment

> Pas de configuration Cisco détaillée dans ce module : uniquement les concepts.

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[Cours 02 - Routage]] |
| Suite recommandée | → [[Cours 04 - Diagnostic réseau]] |
| Branches | [[../../03 - DNS et DHCP/Cours - DHCP]] |
| TP associé | [[TP/TP16 - Analyse du réseau]] · [[TP/TP17 - Mise en place d'un routeur]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
