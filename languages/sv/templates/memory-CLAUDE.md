Kunskap som växer med tiden: beslut, research, ansökningar och arkivet.

## Var allt hamnar

| Innehåll | Hamnar i |
|---|---|
| Ett beslut med motivering, eller en granskning av något utifrån (app, webbplats, kurs, konkurrent) | `decisions/YYYY-MM-DD-{title}.md` |
| Research (marknad, trender, alternativ) | `research/{topic}.md` |
| Ansökningar: jobb, bidrag, priser, öppna utlysningar (skapas första gången de behövs) | `applications/{name}/` |
| Profiler på konkurrenter (skapas första gången de behövs) | `competitors/{name}.md` |
| Pengar: fakturor, skatt, betalningar. Privat | `finances/` |
| Arkiverade beslut | `archive/decisions/` |
| Avslutad eller inaktuell research | `archive/research/` |
| Avslutade projekt | `archive/{name}/` |
| Mötesanteckningar | `decisions/` om ett beslut kom ut av mötet, annars dagsanteckningen för den dagen i `Daily/`. Föreslå en egen mapp för möten bara när de är många. |

## Infoblock (frontmatter)

```yaml
---
type: research
date: 2026-10-13
status: active
tags: [research, pricing]
---
```

- `type`: `decision`, `research`, `application`, `competitor`.
- `date`: datumet då anteckningen skrevs.
- `status`: se nedan för beslut och ansökningar. Allt annat: `active` eller `closed`.
- `tags`: typen, sedan ämnet.
- Valfritt: `project`, `deadline`, `description` (en mening, inom dubbla citattecken, sista raden).

## Beslutsanteckningar

Skriv alltid varför: vem som var med, vad som satte igång det, vilken avvägning som gjordes. Använd `> [!important]` för själva beslutet och `> [!warning]` för kända risker.

Beslut har också `updated:` direkt efter `date:`. `date` är när beslutet skapades, `updated` är senaste gången det sågs över eller ändrades.

```yaml
---
type: decision
date: 2026-09-02
updated: 2026-10-13
status: open
tags: [decision, website]
---
```

- `status`: `open` (håller fortfarande på att bestämmas eller genomföras), `waiting` (väntar på någon annan), `paused`, `closed`.
- Ett beslut vars `updated` är mer än 30 dagar gammalt behöver ses över. Städhjälpen flaggar det tills {Name} behåller det, stänger det eller arkiverar det (alla tre sätter `updated` till den dagen).
- Ett beslut flyttas till `archive/decisions/` bara när {Name} säger det.

## Ansökningar

En mapp per ansökan: `applications/{name}/`, med en `README.md` som innehåller deadline, länken, läget och vad som skickades. Andra filer (svar, personligt brev) ligger bredvid.

- `status`: `draft`, `submitted`, `accepted`, `rejected` eller `withdrawn`.
- Spara svaren i markdown. Stora PDF:er och presentationer ligger kvar utanför hjärnan: sammanfatta dem i en anteckning.

## Regler

- Research är neutral som standard (huvudregel 23).
- Flytta research som ersatts av nyare till `archive/research/` i stället för att radera den.
- `finances/` är privat och står i `.claudeignore`. Öppna den bara när {Name} ber om en viss fil (huvudregel 8).
