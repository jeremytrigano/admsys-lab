# Fondamentaux réseau

> Voir aussi : [[Cours 02 - Routage]] · [[../../03 - DNS et DHCP/Cours - DNS]] · [[../../03 - DNS et DHCP/Cours - DHCP]] · [[../../Architecture]]

## Définition

Un réseau informatique relie des équipements pour qu'ils puissent échanger des données selon des règles communes (protocoles, adressage, routage).

## Modèle OSI (vision simplifiée)

| Couche | Nom | Exemple |
|--------|-----|---------|
| 7 | Application | HTTP, DNS, SSH |
| 4 | Transport | TCP, UDP |
| 3 | Réseau | IP, routage |
| 2 | Liaison | Ethernet, switch |
| 1 | Physique | Câble, fibre |

## TCP/IP

Suite de protocoles utilisée sur Internet et dans la majorité des réseaux d'entreprise. Elle regroupe notamment IP, TCP, UDP, ICMP, DNS et DHCP.

## IPv4

Format : `192.168.1.10/24`

- **Adresse réseau** : identifie le segment
- **Adresse hôte** : identifie une machine
- **Broadcast** : communication vers tout le segment

## Masque de sous-réseau

Le masque délimite la partie réseau et la partie hôte.

| Notation | Masque | Hôtes utilisables |
|----------|--------|-------------------|
| /24 | 255.255.255.0 | 254 |
| /16 | 255.255.0.0 | 65 534 |

## Passerelle par défaut

Routeur ou équipement qui relie un réseau local à un autre réseau (souvent Internet).

Exemple : `192.168.1.1` ou `192.168.10.254`

## DNS

Traduit un nom en adresse IP.

```text
srv-dc01.lab.local  →  192.168.1.210
```

→ [[../../03 - DNS et DHCP/Cours - DNS]]

## DHCP

Attribue automatiquement une configuration IP aux postes.

→ [[../../03 - DNS et DHCP/Cours - DHCP]]

## Adresses privées / publiques

| Type | Plages courantes |
|------|------------------|
| Privées | 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 |
| Publiques | Toutes les autres (routables sur Internet) |

## NAT

Le NAT (Network Address Translation) permet à plusieurs machines d'un réseau privé de sortir vers Internet via une seule adresse publique.

## CIDR

Notation compacte pour exprimer une adresse et son masque : `192.168.10.0/24`.

## Ports TCP et UDP

| Port | Protocole | Usage |
|------|-----------|-------|
| 80 | TCP | HTTP |
| 443 | TCP | HTTPS |
| 22 | TCP | SSH |
| 3389 | TCP | RDP |
| 53 | TCP/UDP | DNS |
| 67/68 | UDP | DHCP |
| 389/636 | TCP | LDAP/LDAPS |
| 445 | TCP | SMB |
| ICMP | - | ping, diagnostic |

## Protocoles courants

| Protocole | Rôle |
|-----------|------|
| HTTP/HTTPS | Accès Web |
| SSH | Administration distante Linux |
| RDP | Bureau à distance Windows |
| DNS | Résolution de noms |
| DHCP | Attribution d'adresses |
| LDAP | Annuaire (Active Directory) |
| SMB | Partage de fichiers Windows |
| ICMP | Test de connectivité (ping) |

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[../../03 - DNS et DHCP/TP/TP09-DHCP]] · [[../../05 - Linux/TP/TP14 - Administration Linux]] |
| Suite recommandée | → [[Cours 02 - Routage]] |
| Branches | [[../../01 - Virtualisation/Cours - Virtualisation]] · [[../../Architecture]] |
| TP associé | [[TP/TP16 - Analyse du réseau]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
