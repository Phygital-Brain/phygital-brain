Elk project is een map die groeit naarmate er informatie bijkomt. `README.md` is de enige ingang.

## Waar wat hoort

| Inhoud | Gaat naar |
|---|---|
| Overzicht, stand, deadline, volgende stappen | `Projects/{name}/README.md` |
| Werknotities van {Name} | `Projects/{name}/notes/{topic}.md` |
| Onderzoek | `Projects/{name}/research/{topic}.md` |
| Briefing, specificaties, eisen | `Projects/{name}/briefs/{name}.md` |
| Concepten, scripts, geschreven teksten | `Projects/{name}/drafts/{name}.md` |
| Ideeën | `Projects/{name}/ideas/{name}.md` |
| Feedback | `Projects/{name}/feedback/{name}.md` |
| Afbeeldingen en media | `Projects/{name}/assets/` |
| Oud materiaal van dit project | `Projects/{name}/archive/` |

Mapnamen zijn in kleine letters met koppeltekens, zonder nummers ervoor (`research/`, niet `01-Research/`). Een project mag een eigen map toevoegen als geen van deze past.

## Opbouw van de README

1. Infoblok (hieronder), met een `description`.
2. `## Wat het is`: één of twee regels, met een link naar [[goals]].
3. `## Stand en volgende stap`: hoe het ervoor staat, de volgende stap.
4. `## Hoe het loopt`: alleen als er iets automatisch hierin schrijft (een geplande taak, een script).
5. `## Waar alles staat`: alleen zodra er submappen zijn. Een tabelletje met een link naar elke map.

## Infoblok (frontmatter)

```yaml
---
type: notes
date: 2026-10-13
status: active
project: Website-Redesign
tags: [website-redesign, notes]
---
```

- `type`: `project` (de README, die ook `created`, `updated` en `description` heeft), `notes`, `research`, `brief`, `draft`, `idea`, `feedback`, `plan`.
- `status`: `active`, `paused` of `done`. De status van de README is de status van het project.
- `project`: de naam van de projectmap.
- `tags`: het project, dan het type.

## Regels

- Een nieuw project is alleen een `README.md`. Maak pas submappen als er inhoud komt die ze nodig heeft, en link ernaar vanuit de README.
- De README is de inhoudsopgave. Herhaal er niet wat in de submappen staat.
- Geen `CLAUDE.md` in een project. Regels voor één project staan hieronder bij "Regels per project".
- Zet `project:` in het infoblok van elke notitie die erbij hoort.
- Een afgerond project gaat pas naar `Memory/archive/{name}/` als {Name} dat zegt.
- Elk project hoort bij te dragen aan een doel in [[goals]]. Wijs bij een check-up op doelen zonder project en projecten zonder doel.

## Regels per project

<!-- Regels voor maar één project. Voeg een regel toe als een project een eigen regel nodig heeft: "**Projectnaam:** de regel." -->
