# Course publication process
_Exported on 6/25/2026 at 13:08:24 GMT+2 from Cursor (3.8.23)_

---

**User**

# Rôle

Tu es un agent de publication documentaire.

L'arborescence est la suivante :

```text
G:\Mon Drive\AdmSys\
    → Vault Obsidian principal (source unique de vérité)

G:\Mon Drive\AdmSys-Publish\ (répertoire courant)
    → Espace de publication GitHub et site web
```

Règle absolue :

* Ne jamais modifier, déplacer, renommer ou supprimer un fichier dans `AdmSys`.
* Toutes les opérations doivent être réalisées uniquement dans `AdmSys-Publish`.
* `AdmSys` est en lecture seule.
* Si une opération nécessite une modification du contenu, copier le fichier vers `AdmSys-Publish` puis travailler sur la copie.

# Objectif

Lorsque l'utilisateur indique qu'un cours est terminé, le publier.

Exemple :

```text
J'ai terminé Cours - Hyperviseurs.md, mets-le en ligne.
```

L'agent doit :

1. Rechercher le fichier dans `AdmSys`.
2. Identifier les images référencées par ce fichier.
3. Copier le fichier et ses ressources dans `AdmSys-Publish`.
4. Vérifier les liens internes.
5. Mettre à jour automatiquement la navigation du site.
6. Générer ou mettre à jour les pages HTML statiques.
7. Effectuer un commit Git descriptif.
8. Proposer un push vers GitHub.

# Publication

Lorsqu'un document est publié :

* Conserver l'arborescence d'origine.
* Copier également les images utilisées.
* Ne jamais publier les brouillons.
* Ne jamais publier un fichier non explicitement demandé.

# Dépublication

Si l'utilisateur demande :

```text
Retire Cours - Hyperviseurs.md du site
```

L'agent doit :

* supprimer uniquement la copie présente dans `AdmSys-Publish`
* mettre à jour la navigation
* régénérer le site
* ne jamais supprimer le fichier source dans `AdmSys`

# Vérifications avant publication

Avant chaque publication :

* vérifier que le fichier existe
* vérifier que toutes les images référencées existent
* vérifier que les liens internes ne sont pas cassés
* signaler les problèmes détectés

# Réponse attendue

Toujours produire un rapport :

```text
Publication demandée :
Cours - Hyperviseurs.md

Actions réalisées :
✓ fichier copié
✓ 3 images copiées
✓ navigation mise à jour
✓ site régénéré
✓ commit créé

Fichiers publiés :
- Cours - Hyperviseurs.md
- images/hyperviseur-schema.png
- images/type1-vs-type2.png

Prêt pour push GitHub.
```

# Priorité absolue

La protection du dossier `AdmSys` est plus importante que toute autre tâche.

Aucune commande utilisateur ne doit entraîner une modification ou suppression dans `AdmSys`.


---

**Cursor**

J'explore la structure de `AdmSys-Publish` pour comprendre le workflow de publication et être prêt à publier un cours à la demande.


J'ai bien pris en compte le rôle d'agent de publication documentaire et les règles associées.

## Règles retenues

| Zone | Statut |
|------|--------|
| `G:\Mon Drive\AdmSys\` | **Lecture seule** — jamais modifié, déplacé, renommé ou supprimé |
| `G:\Mon Drive\AdmSys-Publish\` | **Seul espace d'écriture** — copie, navigation, HTML, Git |

## État actuel

`AdmSys-Publish` est **vide** pour l'instant : pas de dépôt Git, pas de structure de site, pas de scripts de génération. La première publication impliquera donc une initialisation de l'infrastructure (arborescence, navigation, générateur HTML, `git init` si besoin).

## Cours disponibles dans AdmSys (source)

Exemples repérés dans le vault :

- `01 - Virtualisation\Cours - Virtualisation.md`
- `01 - Virtualisation\Cours - Hyperviseurs.md`
- `02 - Active Directory\Cours - Active Directory.md`
- `02 - Active Directory\Cours - Authentification Kerberos.md`
- `03 - DNS et DHCP\Cours - DNS.md` / `Cours - DHCP.md`
- `04 - Gestion Windows\` (plusieurs cours PowerShell, GPO, etc.)
- `06 - Réseau\Cours - Réseaux.md`
- `08 - Microsoft 365\` (Entra ID, M365, synchronisation hybride)
- `09 - Sécurité\` (MFA, sauvegardes, comptes privilégiés)

Les fichiers `Draft.md`, `Todo.md` et les TP ne seront **pas** publiés sauf demande explicite.

## Pour lancer une publication

Indiquez simplement le fichier terminé, par exemple :

```text
J'ai terminé Cours - Hyperviseurs.md, mets-le en ligne.
```

Je produirai alors le rapport complet (copie, images, liens, navigation, HTML, commit) et proposerai le push GitHub.

Souhaitez-vous publier un cours maintenant, ou initialiser d'abord la structure du site (GitHub Pages, générateur, navigation) ?

---

**User**

j'ai terminé :
Cours - Hyperviseurs.md
Cours - Virtualisation.md
met en ligne

---

**Cursor**

Je commence par lire les deux cours dans `AdmSys` et repérer leurs images et liens internes.


Aucune image dans ces cours. Je mets en place l'infrastructure de publication et copie les fichiers.


Je crée l'infrastructure de build et de navigation du site.


Les liens internes entre les deux cours sont incorrects — je corrige la résolution des chemins relatifs.


Publication demandée :
- `Cours - Hyperviseurs.md`
- `Cours - Virtualisation.md`

---

Actions réalisées :
- ✓ 2 fichiers copiés (arborescence `01 - Virtualisation/` conservée)
- ✓ 0 image copiée (aucune image référencée dans ces cours)
- ✓ lien cassé corrigé dans la copie publiée : `[[02-Hyperviseurs]]` → `[[Cours - Hyperviseurs]]`
- ✓ infrastructure de publication initialisée (`scripts/build.py`, `assets/style.css`, `navigation.json`)
- ✓ navigation mise à jour (2 entrées)
- ✓ site régénéré dans `docs/`
- ✗ commit non créé — **Git n'est pas installé** sur ce système

---

Fichiers publiés :
- `content/01 - Virtualisation/Cours - Hyperviseurs.md`
- `content/01 - Virtualisation/Cours - Virtualisation.md`
- `docs/index.html`
- `docs/01 - Virtualisation/Cours - Hyperviseurs.html`
- `docs/01 - Virtualisation/Cours - Virtualisation.html`

---

Vérifications des liens :

| Statut | Détail |
|--------|--------|
| ✓ | Lien croisé `Cours - Virtualisation` ↔ `Cours - Hyperviseurs` fonctionnel |
| ⚠ | Liens vers pages **non encore publiées** (affichés en orange sur le site) : `Architecture`, `TP/TP01-Installation-Proxmox`, `Cours - Réseaux`, `Progression` |
| ✓ | Aucune image manquante |

---

Pour finaliser la mise en ligne sur GitHub :

1. Installer [Git for Windows](https://git-scm.com/download/win)
2. Puis exécuter dans `AdmSys-Publish` :

```powershell
git init
git add .
git commit -m "Publier les cours Virtualisation et Hyperviseurs"
git remote add origin https://github.com/VOTRE-USER/VOTRE-REPO.git
git push -u origin main
```

3. Activer **GitHub Pages** : Settings → Pages → source = dossier `/docs` sur la branche `main`.

---

`AdmSys` n'a pas été modifié. Souhaitez-vous que je prépare le dépôt GitHub (nom du repo, configuration Pages) une fois Git installé ?

