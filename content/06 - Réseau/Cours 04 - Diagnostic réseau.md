# Diagnostic réseau

> Voir aussi : [[Cours 01 - Fondamentaux réseau]] · [[Cours 03 - Commutation et VLAN]] · [[../../05 - Linux/Cours 03 - Réseau Linux]]

## Commandes Windows

| Commande | Description |
|----------|-------------|
| `ipconfig` | Configuration IP |
| `ipconfig /all` | Détail complet |
| `ping` | Test de connectivité |
| `tracert` | Chemin réseau |
| `nslookup` | Résolution DNS |
| `arp` | Table ARP (adresses MAC) |
| `route print` | Table de routage |
| `netstat` | Connexions et ports |

## Commandes Linux

| Commande | Description |
|----------|-------------|
| `ip addr` | Interfaces et adresses |
| `ip route` | Table de routage |
| `ss -tulpn` | Ports en écoute |
| `ping` | Test de connectivité |
| `traceroute` | Chemin réseau |
| `dig` | Requête DNS détaillée |
| `nslookup` | Résolution DNS |

## Méthodologie de dépannage

Diagnostiquer couche par couche :

```text
1. Couche physique    → lien, interface, câble
2. IP                 → adresse, masque, conflit
3. Passerelle         → route par défaut, ping gateway
4. DNS                → résolution de noms
5. Internet           → ping 8.8.8.8, accès externe
6. Service            → port, pare-feu, service applicatif
```

## Exemples de tests

```powershell
# Windows
ipconfig /all
ping 192.168.10.254
ping 8.8.8.8
nslookup google.com
```

```bash
# Linux
ip addr
ping -c 4 192.168.10.254
ping -c 4 8.8.8.8
dig google.com
```

## Bonnes pratiques

- Noter chaque test et son résultat
- Tester du plus proche au plus éloigné (gateway → DNS → Internet)
- Vérifier la configuration DHCP si le poste est en automatique
- Documenter la résolution dans [[../../Architecture]]

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[Cours 03 - Commutation et VLAN]] |
| Suite recommandée | → [[../../12 - Téléphonie IP/Cours - Introduction à la VoIP]] |
| Branches | [[../../05 - Linux/Cours 03 - Réseau Linux]] |
| TP associé | [[TP/TP16 - Analyse du réseau]] · [[TP/TP17 - Mise en place d'un routeur]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
