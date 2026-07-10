# Réseau Linux

> Voir aussi : [[../03 - DNS et DHCP/Cours - DNS]] · [[Cours 02 - Administration Linux]]

## Configuration IP

Afficher les interfaces :

```bash
ip addr
```

Afficher les routes :

```bash
ip route
```

## Commandes utiles

| Commande | Description |
|----------|-------------|
| `ip addr` | Configuration IP |
| `ping` | Tester la connectivité |
| `ss -tulpn` | Connexions réseau |
| `traceroute` | Chemin réseau |
| `hostname` | Nom de la machine |

## DNS

Afficher les serveurs DNS :

```bash
cat /etc/resolv.conf
```

Tester la résolution :

```bash
nslookup google.com
dig google.com
```

## SSH

Connexion distante :

```bash
ssh utilisateur@serveur
```

Copie de fichiers :

```bash
scp fichier utilisateur@serveur:/home/utilisateur
```

Le service SSH est généralement fourni par **OpenSSH**.

## Pare-feu

Selon la distribution :

Ubuntu :

```bash
ufw status
```

Red Hat :

```bash
firewall-cmd --list-all
```

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[Cours 02 - Administration Linux]] |
| Suite recommandée | → [[Cours 04 - Services Linux]] |
| Branches | [[../03 - DNS et DHCP/Cours - DNS]] |
| TP associé | [[TPxx - Services et réseau Linux]] |

> Suivi : [[../00 - Administration du parcours/Progression]]
