# DHCP

> Voir aussi : [[Cours - DNS]] · [[../../06 - Réseau/Cours - Réseaux]] · [[TP/TP09-DHCP]] · [[00 - Administration du parcours/Préparation entretiens#03 - DNS et DHCP]]

## Définition

Le DHCP (Dynamic Host Configuration Protocol) attribue automatiquement une configuration réseau aux clients.

## Fonction

Attribuer automatiquement :
- Adresse IP
- Masque de sous-réseau
- Passerelle par défaut
- Serveurs DNS

## Processus DORA

```
Discover  →  Le client cherche un serveur DHCP
Offer     →  Le serveur propose une IP
Request   →  Le client accepte
Acknowledge → Le serveur confirme
```

## Concepts

### Scope (étendue)

Plage d'adresses disponibles.

Exemple : `192.168.1.100` à `192.168.1.200`

### Bail (lease)

Durée pendant laquelle une IP est attribuée à un client.

### Réservation

Adresse IP fixe liée à une adresse MAC.

### Options DHCP

- Option 003 : passerelle
- Option 006 : serveurs DNS
- Option 015 : nom de domaine

## Bonnes pratiques

- Exclure les adresses des serveurs de la plage dynamique
- Utiliser des réservations pour les serveurs et imprimantes
- Documenter les scopes et exclusions
- Surveiller l'utilisation de la plage (alerte à 80 %)

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[Cours - DNS]] |
| Suite recommandée | → [[../../04 - Gestion Windows/Cours - GPO]] |
| TP associé | [[TP/TP09-DHCP]] |

> Suivi : [[00 - Administration du parcours/Progression]]
