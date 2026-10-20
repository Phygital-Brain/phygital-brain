Hvert prosjekt er en mappe som vokser etter hvert som det kommer ny informasjon. `README.md` er den eneste inngangen.

## Hvor ting skal ligge

| Innhold | Legges i |
|---|---|
| Oversikt, status, frist, neste steg | `Projects/{name}/README.md` |
| Arbeidsnotatene til {Name} | `Projects/{name}/notes/{topic}.md` |
| Research | `Projects/{name}/research/{topic}.md` |
| Brief, krav, spesifikasjoner | `Projects/{name}/briefs/{name}.md` |
| Utkast, manus, tekster | `Projects/{name}/drafts/{name}.md` |
| Ideer | `Projects/{name}/ideas/{name}.md` |
| Tilbakemeldinger | `Projects/{name}/feedback/{name}.md` |
| Bilder og medier | `Projects/{name}/assets/` |
| Gammelt materiale fra dette prosjektet | `Projects/{name}/archive/` |

Mappenavn skrives med små bokstaver og bindestreker, uten tall foran (`research/`, ikke `01-Research/`). Et prosjekt kan få sin egen mappe når ingen av disse passer.

## Slik ser README-en ut

1. Infoblokk (se under), med en `description`.
2. `## Hva det er`: én eller to linjer, med lenke til [[goals]].
3. `## Status og neste steg`: hvor prosjektet står, og neste steg.
4. `## Det som kjører automatisk`: bare hvis noe automatisk skriver hit (en planlagt oppgave, et skript).
5. `## Hvor ting ligger`: først når det finnes undermapper. En liten tabell med lenke til hver av dem.

## Infoblokk (frontmatter)

```yaml
---
type: notes
date: 2026-10-13
status: active
project: Website-Redesign
tags: [website-redesign, notes]
---
```

- `type`: `project` (README-en, som også har `created`, `updated` og `description`), `notes`, `research`, `brief`, `draft`, `idea`, `feedback`, `plan`.
- `status`: `active`, `paused` eller `done`. Statusen i README-en er statusen til prosjektet.
- `project`: navnet på prosjektmappen.
- `tags`: først prosjektet, så typen.

## Regler

- Et nytt prosjekt er bare en `README.md`. Lag undermapper først når det kommer innhold som trenger dem, og lenk til dem fra README-en.
- README-en er innholdsfortegnelsen. Ikke gjenta det som står i undermappene.
- Ingen `CLAUDE.md` inne i et prosjekt. Regler for ett enkelt prosjekt står under «Regler per prosjekt» lenger ned.
- Skriv `project:` i infoblokken til hvert notat som hører til prosjektet.
- Et ferdig prosjekt flyttes til `Memory/archive/{name}/` bare når {Name} sier det.
- Hvert prosjekt bør hjelpe et mål i [[goals]]. I en helsesjekk: pek ut mål uten prosjekt og prosjekter uten mål.

## Regler per prosjekt

<!-- Rules for one project only. Add a line when a project needs its own rule: "**Project-Name:** the rule." -->
