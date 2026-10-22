<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove the Morning Brief row if BRIEF = off.
-->

Notizen und Vorlieben für die Skills, die der Agent nutzt, dazu der Aufräumhelfer.

## Aufbau

```
Skills/{skill-name}/
  {skill-name}.md oder SKILL.md   was der Skill macht
  notes.md                        Stil und Vorlieben von {Name} für diesen Skill
  references/                     Beispiele und längeres Material
```

## Installiert

| Skill | Ordner | Was er macht |
|---|---|---|
| Aufräumhelfer | `brain-keeper/` | Räumt jeden Tag von allein auf und macht einen Check-up, wenn {Name} danach fragt |
| Morgenbriefing | `morning-brief/` | Ein kurzer Plan für den Tag, auf Nachfrage oder an jedem Arbeitstag |
| Import | `import/` | Holt Notizen aus anderen Apps rein, nach einem Plan, dem {Name} vorher zustimmt |
| Meeting-Vorbereitung | `meeting-prep/` | Ein kurzes Briefing vor einem Call, aus den Notizen im Gehirn |
| Denkwerkzeuge | `thinking/` | Eine Idee auf die Probe stellen, Muster finden, Notizen finden, die sich widersprechen |
| Verbundene Apps | `connected-apps/` | Aus welchen Apps das Gehirn liest und welche Regeln dafür gelten |
| No AI Slop | `no-ai-slop/` | Der Schreibcheck: überarbeitet Texte, damit sie menschlich klingen, oder markiert KI-Muster (von Peter Yang, MIT-Lizenz, wird nie bearbeitet) |

## Regeln

- Ein Ordner pro Skill, in Kleinbuchstaben mit Bindestrichen (kebab-case).
- Wenn ein neuer Skill dazukommt, füg der Tabelle oben eine Zeile hinzu.
- Um einen Skill hinzuzufügen oder eine App zu verbinden, schau zuerst bei den Vorschlägen von Phygital Brain: `suggested-skills/README.md` und `suggested-apps/README.md` über den Phygital-Brain-Connector oder online unter https://github.com/Phygital-Brain/phygital-brain/tree/main/skills. Wenn es dort ist, folge der Seite dazu. Wenn {Name} fragt "was kann ich meinem Gehirn hinzufügen?", "what can I add to my brain?", zeig beide Listen: zuerst das, was zur Arbeit von {Name} passt. Lass Apps weg, die schon verbunden sind, und Skills, die schon installiert sind.
- Eine `SKILL.md`, die von jemand anderem stammt, wird nie bearbeitet. Um einen Skill anzupassen, leg `notes.md` in seinen Ordner.
- `brain-keeper/daily.md` wird von einer geplanten Aufgabe gelesen. Änder die Datei nur, wenn sich ändern soll, was der tägliche Lauf macht, und halte sie schlicht: keine Links, keine Callouts.
