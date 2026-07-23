# TP16 - Analyse du réseau

> Théorie : [[../../06 - Réseau/Cours 01 - Fondamentaux réseau]] · [[../../06 - Réseau/Cours 04 - Diagnostic réseau]]  
> Captures : `99-Captures/TP16/` · Prérequis : [[../../05 - Linux/TP/TP14 - Administration Linux]]

## Objectif

Comprendre le fonctionnement actuel du laboratoire en analysant la configuration réseau des postes Windows et Linux.

## Contexte

Le lab SER8 est isolé sur `192.168.10.0/24` ([[../../03 - DNS et DHCP/TP/TP09-DHCP]]), distinct du réseau domestique `192.168.1.0/24`. Les machines n'ont pas de passerelle tant que le routeur n'est pas déployé (TP17).

Ce TP cartographie l'existant et explique pourquoi certains tests (ping Internet, `apt update`) échouent encore.

## Prérequis

- [v] [[../../05 - Linux/TP/TP14 - Administration Linux]] validé
- [v] [[../../03 - DNS et DHCP/TP/TP09-DHCP]] validé
- [v] Accès à un poste Windows et à une VM Ubuntu du lab sur `vmbr1`

## Étapes

### 1. Configuration IP Windows

Afficher la configuration :

```powershell
ipconfig /all
```

Identifier :

- adresse IP (`192.168.10.x`)
- masque de sous-réseau (`255.255.255.0`)
- passerelle par défaut (absente ou incorrecte avant TP17)
- serveurs DNS (`192.168.10.210`)

### 2. Configuration IP Ubuntu

Afficher la configuration :

```bash
ip addr
ip route
```

Identifier les mêmes éléments que sur Windows.

### 3. Tests de connectivité

Depuis chaque poste, tester :

```bash
ping 192.168.10.210    # SRV-DC01
ping 192.168.10.100    # autre VM du lab (si disponible)
ping 192.168.10.254    # passerelle (échoue avant TP17)
ping 8.8.8.8           # Internet (échoue avant TP17)
nslookup google.com    # DNS externe (échoue avant TP17)
nslookup lab.local     # DNS interne (doit fonctionner)
```

Adapter les commandes (`ping` / `Test-Connection`, `nslookup` / `Resolve-DnsName`) selon l'OS.

## Validation

- [v] Tests ping et DNS réalisés

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[../../05 - Linux/TP/TP14 - Administration Linux]] · [[../../03 - DNS et DHCP/TP/TP09-DHCP]] |
| Suite recommandée | → [[TP17 - Mise en place d'un routeur]] |
| Branches | [[../../Architecture]] |
| Théorie | [[../../06 - Réseau/Cours 01 - Fondamentaux réseau]] · [[../../06 - Réseau/Cours 04 - Diagnostic réseau]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]
