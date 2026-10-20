Chaque projet est un dossier qui grandit au fil des infos. `README.md` est la seule porte d'entrée.

## Où ranger quoi

| Contenu | À ranger dans |
|---|---|
| Vue d'ensemble, avancement, date limite, prochaines étapes | `Projects/{name}/README.md` |
| Les notes de travail de {Name} | `Projects/{name}/notes/{topic}.md` |
| Recherches | `Projects/{name}/research/{topic}.md` |
| Brief, cahier des charges, besoins | `Projects/{name}/briefs/{name}.md` |
| Brouillons, scripts, textes | `Projects/{name}/drafts/{name}.md` |
| Idées | `Projects/{name}/ideas/{name}.md` |
| Retours | `Projects/{name}/feedback/{name}.md` |
| Images et médias | `Projects/{name}/assets/` |
| Anciens documents de ce projet | `Projects/{name}/archive/` |

Les noms de dossiers sont en minuscules avec des tirets, sans numéro devant (`research/`, pas `01-Research/`). Un projet peut ajouter son propre dossier quand aucun de ceux-ci ne convient.

## Structure du README

1. Le bloc d'infos (ci-dessous), avec une `description`.
2. `## De quoi il s'agit` : une ou deux lignes, avec un lien vers [[goals]].
3. `## Où on en est et prochaine étape` : où en est le projet, la prochaine étape.
4. `## Comment ça tourne` : seulement si quelque chose d'automatique écrit ici (une tâche programmée, un script).
5. `## Où trouver quoi` : seulement quand il y a des sous-dossiers. Un petit tableau avec un lien vers chacun.

## Bloc d'infos (frontmatter)

```yaml
---
type: notes
date: 2026-10-13
status: active
project: Website-Redesign
tags: [website-redesign, notes]
---
```

- `type` : `project` (le README, qui a aussi `created`, `updated` et `description`), `notes`, `research`, `brief`, `draft`, `idea`, `feedback`, `plan`.
- `status` : `active`, `paused` ou `done`. Le statut du README est celui du projet.
- `project` : le nom du dossier du projet.
- `tags` : le projet, puis le type.

## Règles

- Un nouveau projet, c'est juste un `README.md`. Créez des sous-dossiers seulement quand arrive un contenu qui en a besoin, et mettez un lien vers eux depuis le README.
- Le README sert d'index. N'y répétez pas le contenu des sous-dossiers.
- Pas de `CLAUDE.md` dans un projet. Les règles propres à un projet vont dans « Règles par projet » ci-dessous.
- Mettez `project:` dans le bloc d'infos de chaque note liée.
- Un projet terminé va dans `Memory/archive/{name}/` seulement quand {Name} le dit.
- Chaque projet devrait servir un objectif de [[goals]]. Pendant un bilan, signalez les objectifs sans projet et les projets sans objectif.

## Règles par projet

<!-- Règles pour un seul projet. Ajoutez une ligne quand un projet a besoin de sa propre règle : « **Nom-du-projet :** la règle. » -->
