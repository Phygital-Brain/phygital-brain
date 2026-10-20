<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove the Morning Brief row if BRIEF = off.
-->

Notities en voorkeuren voor de skills die de agent gebruikt, plus de Opruimhulp.

## Opbouw

```
Skills/{skill-name}/
  {skill-name}.md of SKILL.md   wat de skill doet
  notes.md                      de stem en voorkeuren van {Name} voor deze skill
  references/                   voorbeelden en langer materiaal
```

## Geïnstalleerd

| Skill | Map | Wat het doet |
|---|---|---|
| Opruimhulp | `brain-keeper/` | Ruimt elke dag vanzelf op, en doet een check-up als {Name} erom vraagt |
| Ochtendoverzicht | `morning-brief/` | Een kort plan voor de dag, op verzoek of elke werkdag |
| Import | `import/` | Haalt notities uit andere apps binnen, met een plan dat {Name} eerst goedkeurt |
| Meetingvoorbereiding | `meeting-prep/` | Een korte voorbereiding voor een call, uit de notities van het brein |
| Denktools | `thinking/` | Een idee op de proef stellen, patronen vinden, notities vinden die elkaar tegenspreken |
| Gekoppelde apps | `connected-apps/` | Uit welke apps het brein leest, en de regels daarvoor |
| No AI Slop | `no-ai-slop/` | De Schrijfcheck: past tekst aan zodat hij menselijk klinkt, of wijst AI-patronen aan (van Peter Yang, MIT-licentie, nooit bewerkt) |

## Regels

- Eén map per skill, in kebab-case (kleine letters met koppeltekens).
- Komt er een nieuwe skill bij, voeg dan een rij toe aan de tabel hierboven.
- Een `SKILL.md` die van iemand anders komt, wordt nooit bewerkt. Wil je een skill aanpassen, zet dan een `notes.md` in de map.
- `brain-keeper/daily.md` wordt gelezen door een geplande taak. Pas het alleen aan als de dagelijkse ronde iets anders moet doen, en houd het eenvoudig: geen links, geen callouts.
