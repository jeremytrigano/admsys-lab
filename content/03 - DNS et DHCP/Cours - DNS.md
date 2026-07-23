# DNS

> Voir aussi : [[../../02 - Active Directory/Cours - Active Directory]] · [[Cours - DHCP]] · [[TP/TP08-DNS]] · [[00 - Administration du parcours/Préparation entretiens#03 - DNS et DHCP]]

## Définition

Le DNS (Domain Name System) traduit un nom de domaine en adresse IP.

## Fonction

```
srv-fichiers.acme.local  →  192.168.1.10
```

## Enregistrements

| Type  | Description                          |
| ----- | ------------------------------------ |
| A     | Nom → IPv4                           |
| AAAA  | Nom → IPv6                           |
| CNAME | Alias vers un autre nom              |
| PTR   | IP → Nom (reverse DNS)               |
| MX    | Serveur de messagerie                |
| SRV   | Service (ex. contrôleurs de domaine) |

## Zones

- **Zone directe** : nom → IP
- **Zone inverse** : IP → nom

## Intégration Active Directory

AD intègre DNS pour enregistrer automatiquement les services du domaine (SRV records).

## Commandes utiles

```powershell
nslookup acme.local
ping srv-fichiers.acme.local
Resolve-DnsName acme.local
ipconfig /flushdns
```

## Bonnes pratiques

- Configurer des DNS secondaires
- Documenter les enregistrements manuels
- Vérifier la résolution interne et externe
- Ne pas modifier les enregistrements SRV AD sans comprendre l'impact

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[../../02 - Active Directory/Cours - Active Directory]] · [[../../06 - Réseau/Cours 01 - Fondamentaux réseau]] |
| Suite recommandée | → [[Cours - DHCP]] |
| TP associé | [[TP/TP08-DNS]] |

> Suivi : [[00 - Administration du parcours/Progression]]
