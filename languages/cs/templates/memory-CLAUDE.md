Znalosti, které se časem nabalují: rozhodnutí, rešerše, přihlášky a archiv.

## Co kam patří

| Obsah | Kam |
|---|---|
| Rozhodnutí s odůvodněním nebo rozbor věci zvenku (aplikace, web, kurz, konkurence) | `decisions/YYYY-MM-DD-{title}.md` |
| Rešerše (trh, trendy, možnosti) | `research/{topic}.md` |
| Přihlášky: práce, granty, ceny, otevřené výzvy (vznikne při prvním použití) | `applications/{name}/` |
| Profily konkurence (vznikne při prvním použití) | `competitors/{name}.md` |
| Peníze: faktury, daně, platby. Soukromé | `finances/` |
| Archivovaná rozhodnutí | `archive/decisions/` |
| Dokončené nebo zastaralé rešerše | `archive/research/` |
| Dokončené projekty | `archive/{name}/` |
| Zápisy ze schůzek | `decisions/`, pokud z nich vzešlo rozhodnutí, jinak denní poznámka z toho dne v `Daily/`. Složku na schůzky navrhni, až když jich je hodně. |

## Informační blok (frontmatter)

```yaml
---
type: research
date: 2026-10-13
status: active
tags: [research, pricing]
---
```

- `type`: `decision`, `research`, `application`, `competitor`.
- `date`: datum, kdy poznámka vznikla.
- `status`: u rozhodnutí a přihlášek viz níže. U všeho ostatního: `active` nebo `closed`.
- `tags`: typ, pak téma.
- Volitelně: `project`, `deadline`, `description` (jedna věta v dvojitých uvozovkách, poslední řádek).

## Poznámky o rozhodnutích

Vždycky uveď proč: kdo se účastnil, co k tomu vedlo, na jaký kompromis se přistoupilo. Pro samotné rozhodnutí použij `> [!important]` a pro známá rizika `> [!warning]`.

Rozhodnutí mají navíc `updated:` hned za `date:`. `date` je den vzniku, `updated` je den, kdy se rozhodnutí naposledy prošlo nebo změnilo.

```yaml
---
type: decision
date: 2026-09-02
updated: 2026-10-13
status: open
tags: [decision, website]
---
```

- `status`: `open` (pořád se o tom rozhoduje nebo se na tom pracuje), `waiting` (čeká se na někoho jiného), `paused`, `closed`.
- Rozhodnutí, jehož `updated` je starší než 30 dní, potřebuje kontrolu. Správce mozku ho označuje, dokud ho {Name} neponechá, neuzavře nebo nearchivuje (každá z těch možností nastaví `updated` na ten den).
- Rozhodnutí se přesouvá do `archive/decisions/` jen tehdy, když to {Name} řekne.

## Přihlášky

Jedna složka na přihlášku: `applications/{name}/`, s `README.md`, kde je termín, odkaz, stav a co se poslalo. Další soubory (odpovědi, motivační dopis) leží vedle.

- `status`: `draft`, `submitted`, `accepted`, `rejected` nebo `withdrawn`.
- Odpovědi drž v markdownu. Velká PDF a prezentace zůstávají mimo trezor poznámek: shrň je v poznámce.

## Pravidla

- Rešerše jsou standardně neutrální (hlavní pravidlo 23).
- Překonané rešerše přesuň do `archive/research/`, nemaž je.
- `finances/` je soukromá a je uvedená v `.claudeignore`. Otevři ji, jen když {Name} chce konkrétní soubor (hlavní pravidlo 8).
