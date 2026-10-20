Kennis die zich in de loop van de tijd opstapelt: beslissingen, onderzoek, aanvragen en het archief.

## Waar wat hoort

| Inhoud | Gaat naar |
|---|---|
| Beslissing met de redenen, of onderzoek naar iets van buiten (app, website, cursus, concurrent) | `decisions/YYYY-MM-DD-{title}.md` |
| Onderzoek (markt, trends, opties) | `research/{topic}.md` |
| Aanvragen en sollicitaties: banen, subsidies, prijzen, open calls (wordt gemaakt bij het eerste gebruik) | `applications/{name}/` |
| Profielen van concurrenten (wordt gemaakt bij het eerste gebruik) | `competitors/{name}.md` |
| Geld: facturen, belastingen, betalingen. Privé | `finances/` |
| Gearchiveerde beslissingen | `archive/decisions/` |
| Afgerond of verouderd onderzoek | `archive/research/` |
| Afgeronde projecten | `archive/{name}/` |
| Verslagen van meetings | `decisions/` als er een beslissing uit kwam, anders de `Daily/`-notitie van die dag. Stel pas een map voor meetings voor als het er veel zijn. |

## Infoblok (frontmatter)

```yaml
---
type: research
date: 2026-10-13
status: active
tags: [research, pricing]
---
```

- `type`: `decision`, `research`, `application`, `competitor`.
- `date`: de datum waarop de notitie geschreven is.
- `status`: zie hieronder voor beslissingen en aanvragen. Al het andere: `active` of `closed`.
- `tags`: het type, dan het onderwerp.
- Mag erbij: `project`, `deadline`, `description` (één zin, tussen dubbele aanhalingstekens, laatste regel).

## Beslissingsnotities

Zet er altijd het waarom bij: wie erbij betrokken was, wat de aanleiding was, welke afweging er gemaakt is. Gebruik `> [!important]` voor de beslissing zelf en `> [!warning]` voor bekende risico's.

Beslissingen hebben ook `updated:`, direct na `date:`. `date` is wanneer de notitie gemaakt is, `updated` is de laatste keer dat ze bekeken of veranderd is.

```yaml
---
type: decision
date: 2026-09-02
updated: 2026-10-13
status: open
tags: [decision, website]
---
```

- `status`: `open` (er moet nog over besloten worden, of er wordt nog aan gewerkt), `waiting` (wacht op iemand anders), `paused`, `closed`.
- Een beslissing waarvan `updated` meer dan 30 dagen oud is, moet nagekeken worden. De Opruimhulp blijft die beslissing melden tot {Name} kiest: houden, sluiten of archiveren (elk daarvan zet `updated` op die dag).
- Een beslissing gaat pas naar `archive/decisions/` als {Name} dat zegt.

## Aanvragen

Eén map per aanvraag: `applications/{name}/`, met een `README.md` met de deadline, de link, de status en wat er is ingestuurd. Andere bestanden (antwoorden, motivatie) staan ernaast.

- `status`: `draft`, `submitted`, `accepted`, `rejected` of `withdrawn`.
- Bewaar antwoorden in markdown. Grote pdf's en presentaties blijven buiten het brein: vat ze samen in een notitie.

## Regels

- Onderzoek is standaard neutraal (hoofdregel 23).
- Verplaats achterhaald onderzoek naar `archive/research/` in plaats van het te verwijderen.
- `finances/` is privé en staat in `.claudeignore`. Open de map alleen als {Name} om een bepaald bestand vraagt (hoofdregel 8).
