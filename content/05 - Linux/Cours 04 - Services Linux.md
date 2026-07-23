# Services Linux

> Voir aussi : [[Cours 02 - Administration Linux]] · [[Cours 03 - Réseau Linux]]

## systemd

`systemd` est le gestionnaire de services utilisé par la majorité des distributions Linux modernes.

Il gère :

- les services
- le démarrage du système
- les journaux
- les tâches automatiques

## systemctl

Afficher les services :

```bash
systemctl list-units --type=service
```

Démarrer :

```bash
sudo systemctl start service
```

Arrêter :

```bash
sudo systemctl stop service
```

Redémarrer :

```bash
sudo systemctl restart service
```

Activer au démarrage :

```bash
sudo systemctl enable service
```

Vérifier l'état :

```bash
systemctl status service
```

## journalctl

Afficher les journaux :

```bash
journalctl
```

Derniers événements :

```bash
journalctl -xe
```

Pour un service :

```bash
journalctl -u ssh
```

## Logs

Les journaux sont généralement stockés dans :

```text
/var/log
```

Exemples :

- `/var/log/syslog`
- `/var/log/auth.log`
- `/var/log/messages`

## Montage des systèmes de fichiers

Afficher les systèmes montés :

```bash
mount
```

Utilisation du disque :

```bash
df -h
```

Monter un disque :

```bash
mount /dev/sdb1 /mnt
```

Configuration permanente :

```text
/etc/fstab
```

## Services courants

| Service | Fonction |
|----------|----------|
| SSH | Administration distante |
| Apache | Serveur Web |
| Nginx | Serveur Web |
| Samba | Partage de fichiers |
| Docker | Conteneurs |

---

## Progression

| Étape | Lien |
|-------|------|
| Prérequis | [[Cours 03 - Réseau Linux]] |
| Suite recommandée | → [[../06 - Réseau/Cours 01 - Fondamentaux réseau]] |
| Branches | [[../11 - Conteneurisation]] |
| TP associé | [[TPxx - Services et réseau Linux]] |

> Suivi : [[../00 - Administration du parcours/Progression]]
