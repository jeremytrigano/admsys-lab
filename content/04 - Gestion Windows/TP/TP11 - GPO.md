# TP11 - GPO

> Théorie : [[../Cours - GPO]]
> Captures : `99-Captures/TP11/` · Prérequis : [[TP10-Serveur-de-fichiers]]

## Objectif

Mettre en place plusieurs stratégies de groupe (GPO) afin de centraliser l'administration des postes du domaine.

À l'issue de ce TP, les utilisateurs disposeront automatiquement :

- d'un lecteur réseau mappé selon leur service ;
- d'un fond d'écran commun à l'entreprise ;
- de restrictions limitant certaines actions sur le poste de travail.

---

## Prérequis

- [v] [[TP10-Serveur-de-fichiers]] validé

---

# Étapes

## 1. Vérification de l'arborescence Active Directory

Ouvrir :

```
Outils
→ Gestion de stratégie de groupe
```

Vérifier que les OU créées précédemment sont présentes.

Exemple :

```
lab.local
│
├── Direction
├── Production
└── Comptabilite
```

![[../../99-Captures/TP11/01-ou.png]]
_Organisation des unités d'organisation_

---

## 2. Création de la GPO "Lecteur réseau"

Créer un nouvel objet GPO, lié à l'OU **Production** et nommé :

```
GPO-Lecteur-Production
```

---

## 3. Mappage automatique du lecteur réseau

Modifier la GPO :

```
Configuration utilisateur
→ Préférences
→ Paramètres Windows
→ Mappages de lecteurs
```

Créer un nouveau lecteur.

Configurer :

| Paramètre | Valeur |
| ---------- | ------ |
| Action | Créer |
| Emplacement | `\\SRV-DC01\Production` |
| Lettre | `P:` |
| Reconnecter | Oui |

![[../../99-Captures/TP11/02-lecteur.png]]
_Création du lecteur réseau_

---

## 4. Déploiement d'un fond d'écran

Créer un dossier partagé contenant une image.

Exemple :

```
D:\Wallpapers
```

Partager ce dossier en lecture.

Copier une image :

```
production.png
```

Modifier la GPO :

```
Configuration utilisateur
→ Stratégies
→ Modèles d'administration
→ Bureau
→ Bureau
```

Configurer :

```
Papier peint du Bureau
```

Chemin :

```
\\SRV-DC01\Wallpapers\production.png
```

Style :

```
Remplir
```

![[../../99-Captures/TP11/03-wallpaper.png]]
_Configuration du fond d'écran_

---

## 5. Désactivation du Panneau de configuration

Toujours dans la même GPO :

```
Configuration utilisateur
→ Stratégies
→ Modèles d'administration
→ Panneau de configuration
```

Activer :

```
Interdire l'accès au Panneau de configuration et aux Paramètres du PC
```

![[../../99-Captures/TP11/04-panneau.png]]
_Restriction du Panneau de configuration_

---

## 6. Application des stratégies

Sur **WIN11-CLIENT01**, ouvrir une invite de commandes.

Exécuter :

```cmd
gpupdate /force
```

Déconnecter puis reconnecter la session.

Vérifier :

- apparition du lecteur `P:`
- application du fond d'écran
- impossibilité d'ouvrir le Panneau de configuration

![[../../99-Captures/TP11/05-test.png]]
_Test de la GPO_

---

## 7. Vérification des GPO appliquées

Toujours sur le client :

```cmd
gpresult /r
```

Vérifier que :

```
GPO-Lecteur-Production
```

apparaît dans les stratégies appliquées.

Ouvrir également :

```cmd
rsop.msc
```

Contrôler les paramètres effectivement appliqués.

![[../../99-Captures/TP11/06-gpresult.png]]
_Résultat des stratégies_

---

## Validation

- [v] Une GPO est créée et liée à une OU
- [v] Le lecteur réseau est créé automatiquement
- [v] Le fond d'écran est appliqué
- [v] Le Panneau de configuration est inaccessible
- [v] `gpresult` affiche la GPO
- [v] `rsop.msc` confirme son application

---

## Pour aller plus loin

Créer d'autres GPO destinée aux OU **Direction** et **Comptabilite**.

---

## Progression

| Étape | Lien |
| ----------------- | ------------------------------------------ |
| Prérequis | [[TP10-Serveur-de-fichiers]] |
| Suite recommandée | → [[TP12-PowerShell]] |
| Branches | [[../../02 - Active Directory/Cours - Active Directory]] |
| Théorie | [[../Cours - GPO]] |

> Suivi : [[../../00 - Administration du parcours/Progression]]