<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove the Morning Brief row if BRIEF = off.
-->

Notater og ønsker for ferdighetene agenten bruker, pluss Ryddehjelperen.

## Oppbygning

```
Skills/{skill-name}/
  {skill-name}.md eller SKILL.md   hva ferdigheten gjør
  notes.md                         stemmen og ønskene til {Name} for denne ferdigheten
  references/                      eksempler og lengre stoff
```

## Installert

| Ferdighet | Mappe | Hva den gjør |
|---|---|---|
| Ryddehjelperen | `brain-keeper/` | Rydder litt hver dag av seg selv, og tar en helsesjekk når {Name} ber om det |
| Morgenoversikt | `morning-brief/` | En kort plan for dagen, på forespørsel eller hver arbeidsdag |
| Import | `import/` | Henter inn notater fra andre apper, med en plan {Name} godkjenner først |
| Møteforberedelse | `meeting-prep/` | En kort oppsummering før en samtale, ut fra notatene i hjernen |
| Tenkeverktøy | `thinking/` | Utfordrer en idé, finner mønstre, finner notater som sier hverandre imot |
| Tilkoblede apper | `connected-apps/` | Hvilke apper hjernen leser fra, og reglene for dem |
| No AI Slop | `no-ai-slop/` | Skrivesjekken: retter tekst så den høres menneskelig ut, eller peker ut KI-mønstre (av Peter Yang, MIT-lisens, redigeres aldri) |

## Regler

- Én mappe per ferdighet, med navn i kebab-case (små bokstaver og bindestreker).
- Når en ny ferdighet legges til, legg til en rad i tabellen over.
- En `SKILL.md` som kommer fra noen andre, redigeres aldri. For å tilpasse en ferdighet, legg til `notes.md` i mappen dens.
- `brain-keeper/daily.md` leses av en planlagt oppgave. Endre den bare for å endre hva den daglige kjøringen gjør, og hold den enkel: ingen lenker, ingen callouts.
