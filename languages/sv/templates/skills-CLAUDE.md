<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove the Morning Brief row if BRIEF = off.
-->

Anteckningar och önskemål för de skills som agenten använder, plus Städhjälpen.

## Struktur

```
Skills/{skill-name}/
  {skill-name}.md eller SKILL.md   vad skillen gör
  notes.md                         röst och önskemål från {Name} för den här skillen
  references/                      exempel och längre material
```

## Installerade

| Skill | Mapp | Vad den gör |
|---|---|---|
| Städhjälpen | `brain-keeper/` | Städar varje dag av sig själv, och gör en hälsokoll när {Name} ber om det |
| Morgonöversikt | `morning-brief/` | En kort plan för dagen, på begäran eller varje arbetsdag |
| Import | `import/` | Hämtar in anteckningar från andra appar, med en plan som {Name} godkänner först |
| Mötesförberedelse | `meeting-prep/` | En kort sammanfattning inför ett samtal, utifrån hjärnans anteckningar |
| Tankeverktyg | `thinking/` | Utmana en idé, hitta mönster, hitta anteckningar som säger emot varandra |
| Anslutna appar | `connected-apps/` | Vilka appar hjärnan läser från, och reglerna för dem |
| No AI Slop | `no-ai-slop/` | Textkollen: redigerar text så att den låter mänsklig, eller flaggar AI-mönster (av Peter Yang, MIT-licens, redigeras aldrig) |

## Regler

- En mapp per skill, namngiven i kebab-case.
- När en ny skill läggs till, lägg till en rad i tabellen ovan.
- En `SKILL.md` som kommer från någon annan redigeras aldrig. För att anpassa en skill, lägg till `notes.md` i dess mapp.
- `brain-keeper/daily.md` läses av en schemalagd uppgift. Ändra den bara för att ändra vad den dagliga körningen gör, och håll den enkel: inga länkar, inga callouts.
