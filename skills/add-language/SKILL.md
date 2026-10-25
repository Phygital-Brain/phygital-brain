---
name: add-language
description: Make a full Phygital Brain set in a new language (forms, rule files, folder and note names, Brain Keeper), or switch an existing brain to another language. Use when the person says "translate Phygital Brain into my language", "add my language", "switch my brain to Spanish", or the same in another language.
---

# Phygital Brain: Add a language

Version 0.1.12. Everything below is for the agent. Follow it step by step, and check each step before moving on.

Two jobs:

- **A. Add a language** that has no ready set yet: translate everything once, so every brain in that language is built in it.
- **B. Switch a brain** to another language that has a ready set: rename its folders and notes, and swap its rule files, keeping everything the person wrote.

Ask which one if it isn't clear. The ready languages are the folders in `../brain-setup/i18n/`.

## Principles

- **Translate once, never while running.** A brain reads only its own files. No step here leaves the brain looking up translations later.
- **Natural, not literal.** Write what a native speaker would say to a friend who isn't technical. Read each sentence out loud in your head; rewrite anything stiff.
- **Paths are made by the script.** Translators leave paths in English; `scripts/i18n.py` swaps them for the language's names, so they match in every file.
- **Plain language, no em dashes, "your agent"** in anything a person sees.

## A. Add a language

### A1. Get a working copy

This job writes files into the Phygital Brain repository, not into the person's brain. You need a copy you can write to:

- If you're working in a clone of the repository, use it.
- Otherwise ask the person to download it (on GitHub: Code, then Download ZIP, then unzip it) and open a chat on that folder, then start again.

Read `languages/TRANSLATING.md` (the rules) and `languages/en.json` (every text, with keys). Pick the language code: a standard tag like `it`, `ko`, `tr`, `pt-PT`, `es-MX`. If `languages/{code}.json` exists, this is an update: change only what's missing or wrong.

### A2. Choose the words first

Ask the person three things in one message, in their language:

1. Formal or informal "you", the way apps in their language usually talk. Suggest the usual one.
2. The 7 main folder names. Suggest natural ones for About, Daily, Projects, Relationships, Memory, Library and Skills, and let them change any.
3. Names for the Brain Keeper and the morning brief. Suggest natural ones.

Write `languages/{code}/GLOSSARY.md` with the answers, the remaining folder and note names (all of `paths` in `en.json`), and the feature names.

### A3. Translate

1. `languages/{code}.json`: same keys as `en.json`. `"language"`: code, the language's own name, its English name, and `"dir": "rtl"` for right-to-left scripts. `"status": "translated"`. Every value in `paths`, `features`, `messages` and `forms` translated, placeholders like `{Name}` and `{n}` kept as they are, `&#10;` kept where it is.
2. `languages/{code}/templates/`: every file in `skills/brain-setup/templates/`, translated, same file names.
3. `languages/{code}/keeper/`: every file in `skills/brain-keeper/templates/`, translated, same file names.

Follow `TRANSLATING.md` exactly: paths and `[[links]]` to fixed notes in English, info block keys and values in English (except `description:`), YAML and `<!-- ADAPTING -->` comments as they are, trigger phrases in the new language followed by the English one.

For a long job, work file by file and keep going until every file is done.

### A4. Build and check

Run:

```
python3 scripts/i18n.py build {code}
python3 scripts/i18n.py check {code}
python3 scripts/check.py
```

Fix every problem and run them again until they pass. If you can't run Python here, ask the person to run the three lines, or do it on a computer that can.

### A5. Review

Read the whole set again as a native speaker who didn't translate it: the forms first, then the messages, then the rule files. Fix anything stiff, wrong or unclear. Translate five random paragraphs back into English and compare them with the originals; fix any change in meaning. Then set `"status": "reviewed-by-ai"`, build and check again.

Tell the person: "A native speaker should read it before we call it final." When one has, they set `"status": "reviewed"`.

### A6. Use it and share it

- **To use it now:** open a chat on an empty brain folder and say "Set up my second brain. Follow skills/brain-setup/SKILL.md in {path to this copy}." The new language shows up in the setup's list.
- **To share it with everyone:** open a pull request on github.com/Phygital-Brain/phygital-brain with `languages/{code}.json`, `languages/{code}/` and `skills/brain-setup/i18n/{code}/`. See `CONTRIBUTING.md`.

Finish with one short message: the language, the main folder names, what's left to review, and the two lines above.

## B. Switch a brain to another language

Only for a language with a ready set in `../brain-setup/i18n/{code}/`. If there isn't one, offer job A first. If they say just "Portuguese" or "Chinese", ask which one first (`Português do Brasil` · `Português de Portugal`, or `简体中文` · `繁體中文`), as the setup's Step 1 does.

1. **Read first, change nothing.** The root `CLAUDE.md` (its version line, Language section and `## Folder map` if there is one), every folder's `CLAUDE.md`, and `{Name}'s Rules`. Count {Name}'s own rules.
2. **Make the list.** From the current names (the Folder map, or the English names if there's none) to the new ones in `i18n/{code}/strings.json` (`paths`). One line per folder and fixed note that will be renamed.
3. **Ask** (click options when possible): `Switch everything` · `Show me the list first` · `Cancel`. Renaming needs this yes (root rule 21).
4. **Back up** every rule file and every note whose links will change (Backups and Undo in the root `CLAUDE.md`).
5. **Rename** the folders and fixed notes, deepest first. Then update every `[[link]]` to a renamed note, in every note.
6. **Swap the rule files** for the ones in `i18n/{code}/templates/` and `i18n/{code}/keeper/`, filled in like the setup does (name, time zone, choices from `About/me.md`). Keep every routing row, folder and rule {Name} added, translated into the new language without changing their meaning, and {Name}'s own rules word for word in the same order (translate them only if {Name} says yes).
7. **Update** the version line's `language:`, the Language section, and the `## Folder map` with the new names. Update the scheduled tasks or routines if their prompts name a renamed path.
8. **Check:** the same number of {Name}'s own rules; no `[[link]]` points to a name that no longer exists; no path in any `CLAUDE.md` names a folder that doesn't exist; nothing deleted.
9. **Finish:** one line in today's daily note, then two or three lines: the new language, that notes {Name} wrote stay in the language they were written in, and "undo the last change" if they want to go back within 10 days.
