Jedes Projekt ist ein Ordner, der wächst, wenn neue Infos dazukommen. `README.md` ist der einzige Einstieg.

## Wo was hinkommt

| Inhalt | Kommt nach |
|---|---|
| Überblick, Stand, Frist, nächste Schritte | `Projects/{name}/README.md` |
| Arbeitsnotizen von {Name} | `Projects/{name}/notes/{topic}.md` |
| Recherche | `Projects/{name}/research/{topic}.md` |
| Briefing, Anforderungen, Vorgaben | `Projects/{name}/briefs/{name}.md` |
| Entwürfe, Skripte, Texte | `Projects/{name}/drafts/{name}.md` |
| Ideen | `Projects/{name}/ideas/{name}.md` |
| Feedback | `Projects/{name}/feedback/{name}.md` |
| Bilder und Medien | `Projects/{name}/assets/` |
| Altes Material aus diesem Projekt | `Projects/{name}/archive/` |

Ordnernamen sind kleingeschrieben, mit Bindestrichen, ohne Nummern davor (`research/`, nicht `01-Research/`). Ein Projekt kann einen eigenen Ordner bekommen, wenn keiner davon passt.

## Aufbau der README

1. Info-Block (siehe unten), mit einer `description`.
2. `## Was es ist`: ein oder zwei Zeilen, mit Link zu [[goals]].
3. `## Stand und nächster Schritt`: wo das Projekt steht, der nächste Schritt.
4. `## So läuft es`: nur, wenn hier etwas automatisch reinschreibt (eine geplante Aufgabe, ein Skript).
5. `## Wo was liegt`: erst, wenn es Unterordner gibt. Eine kleine Tabelle mit einem Link zu jedem.

## Info-Block (Frontmatter)

```yaml
---
type: notes
date: 2026-10-13
status: active
project: Website-Redesign
tags: [website-redesign, notes]
---
```

- `type`: `project` (die README, die außerdem `created`, `updated` und `description` hat), `notes`, `research`, `brief`, `draft`, `idea`, `feedback`, `plan`.
- `status`: `active`, `paused` oder `done`. Der Status der README ist der Status des Projekts.
- `project`: der Name des Projektordners.
- `tags`: zuerst das Projekt, dann der Typ.

## Regeln

- Ein neues Projekt ist erst mal nur eine `README.md`. Leg Unterordner erst an, wenn Inhalte kommen, die sie brauchen, und verlinke sie in der README.
- Die README ist das Inhaltsverzeichnis. Wiederhol darin nicht, was in den Unterordnern steht.
- Keine `CLAUDE.md` in einem Projekt. Regeln für ein einzelnes Projekt kommen unten unter "Regeln pro Projekt".
- Schreib `project:` in den Info-Block jeder Notiz, die dazugehört.
- Ein abgeschlossenes Projekt kommt nur nach `Memory/archive/{name}/`, wenn {Name} das sagt.
- Jedes Projekt sollte einem Ziel in [[goals]] dienen. Markier beim Check-up Ziele ohne Projekt und Projekte ohne Ziel.

## Regeln pro Projekt

<!-- Regeln nur für ein Projekt. Füg eine Zeile hinzu, wenn ein Projekt eine eigene Regel braucht: "**Projekt-Name:** die Regel." -->
