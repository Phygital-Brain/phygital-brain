<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove table rows for files that weren't created.
-->

Ce dossier contient l'essentiel sur {Name}. Ces notes font foi pour tout le reste du travail.

## Fichiers

| Fichier | Contenu | Tag de catégorie |
|---|---|---|
| `me.md` | Qui est {Name}, sa façon de travailler, comment {Name} veut que son agent travaille | `identity` |
| `biography.md` | L'histoire de {Name} | `identity` |
| `goals.md` | Objectifs et priorités | `goals` |
| `business.md` | L'activité | `business` |
| `services.md` | Services, produits, offres | `business` |
| `customers.md` | Qui achète, et comment ces clients trouvent {Name} | `customers` |
| `pain-points.md` | Les problèmes à résoudre | `customers` (ou `goals` si {Name} ne vend rien) |
| `brand.md` | Style, ton, mots à utiliser et à éviter | `brand` |
| `tools.md` | Les outils, et où se trouve chaque type de chose | `tools` |
| `cv.md` | Parcours pro, études, presse, prix | `career` |

## Bloc d'infos (frontmatter)

Chaque fichier ici (sauf celui-ci) commence par :

```yaml
---
type: about
status: active
updated: 2026-10-13
tags: [about, identity, working-style]
description: "Qui est {Name} et comment {Name} veut que son agent travaille."
---
```

- `type` : toujours `about`.
- `status` : `active`, ou `outdated` quand on sait qu'une info n'est plus à jour.
- `updated` : la date du dernier changement dans les faits. On n'y touche pas pour une faute de frappe ou une retouche de style.
- `tags` : `about`, puis le tag de catégorie du fichier (tableau ci-dessus), puis des tags de sujet qui disent ce que couvre le fichier (en anglais, en minuscules, avec des tirets). Mettez à jour les tags de sujet quand une section est ajoutée ou supprimée.
- `description` : une phrase, entre guillemets droits, qui dit ce que contient le fichier. Toujours la dernière ligne.

## Règles

- Ces fichiers font foi. Ne recopiez pas leur contenu ailleurs : mettez un lien vers eux.
- Format « vérité en haut » (règle 17 du fichier racine) : la vérité actuelle en haut, les preuves datées en dessous.
- La date de naissance complète de {Name} se trouve uniquement dans `me.md`. Ne la recopiez jamais et ne la citez jamais dans une réponse. L'année de naissance, elle, ne pose pas de problème.
- Créez un nouveau fichier seulement quand un nouveau sujet en a besoin. Demandez d'abord (règle 9 du fichier racine).
- Pendant un bilan, signalez les objectifs de `goals.md` qui n'ont aucun projet actif.
