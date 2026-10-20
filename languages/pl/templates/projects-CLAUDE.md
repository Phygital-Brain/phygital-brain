Każdy projekt to folder, który rośnie, kiedy dochodzą informacje. `README.md` to jedyny punkt wejścia.

## Co gdzie trafia

| Treść | Dokąd |
|---|---|
| Opis, stan, termin, następne kroki | `Projects/{name}/README.md` |
| Robocze notatki, które pisze {Name} | `Projects/{name}/notes/{topic}.md` |
| Badania | `Projects/{name}/research/{topic}.md` |
| Brief, specyfikacja, wymagania | `Projects/{name}/briefs/{name}.md` |
| Szkice, scenariusze, teksty | `Projects/{name}/drafts/{name}.md` |
| Pomysły | `Projects/{name}/ideas/{name}.md` |
| Opinie | `Projects/{name}/feedback/{name}.md` |
| Obrazy i media | `Projects/{name}/assets/` |
| Stare materiały z tego projektu | `Projects/{name}/archive/` |

Nazwy folderów małymi literami, z łącznikami, bez numerów na początku (`research/`, a nie `01-Research/`). Projekt może dodać własny folder, jeśli żaden z tych nie pasuje.

## Układ README

1. Blok informacji (niżej), z `description`.
2. `## Co to jest`: jedno albo dwa zdania, z linkiem do [[goals]].
3. `## Stan i następny krok`: na jakim etapie jest projekt i co dalej.
4. `## Jak to działa`: tylko jeśli coś automatycznie tu pisze (zaplanowane zadanie, skrypt).
5. `## Gdzie co jest`: dopiero kiedy są podfoldery. Mała tabela z linkiem do każdego.

## Blok informacji (frontmatter)

```yaml
---
type: notes
date: 2026-10-13
status: active
project: Website-Redesign
tags: [website-redesign, notes]
---
```

- `type`: `project` (README, który ma też `created`, `updated` i `description`), `notes`, `research`, `brief`, `draft`, `idea`, `feedback`, `plan`.
- `status`: `active`, `paused` albo `done`. Status README to status całego projektu.
- `project`: nazwa folderu projektu.
- `tags`: najpierw projekt, potem typ.

## Zasady

- Nowy projekt to tylko `README.md`. Podfoldery twórz dopiero wtedy, kiedy przychodzi treść, która ich potrzebuje, i linkuj je z README.
- README to spis treści. Nie powtarzaj w nim tego, co jest w podfolderach.
- Żadnego `CLAUDE.md` w środku projektu. Zasady dla jednego projektu idą do sekcji „Zasady dla poszczególnych projektów” niżej.
- Wpisuj `project:` w bloku informacji każdej powiązanej notatki.
- Zakończony projekt trafia do `Memory/archive/{name}/` tylko wtedy, kiedy {Name} tak powie.
- Każdy projekt powinien służyć jakiemuś celowi z [[goals]]. Podczas przeglądu zgłaszaj cele bez projektu i projekty bez celu.

## Zasady dla poszczególnych projektów

<!-- Zasady tylko dla jednego projektu. Dopisz linię, kiedy projekt potrzebuje własnej zasady: „**Nazwa-Projektu:** zasada.” -->
