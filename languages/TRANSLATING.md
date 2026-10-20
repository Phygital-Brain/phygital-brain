# Translating Phygital Brain

How a language is made. Read this before you translate or review.

## What you make

For a language with code `{code}` (for example `pt-BR`):

| File | What |
|---|---|
| `languages/{code}.json` | Folder and note names, feature names, setup messages and every form text. Same keys as `languages/en.json`. |
| `languages/{code}/templates/*.md`, `claudeignore.txt` | Every file in `skills/brain-setup/templates/`, translated |
| `languages/{code}/keeper/*.md` | Every file in `skills/brain-keeper/templates/`, translated |
| `languages/{code}/GLOSSARY.md` | The words you chose and why: register (formal or informal "you"), feature names, folder names |

Then `python3 scripts/i18n.py build {code}` turns it into the set the setup copies, in `skills/brain-setup/i18n/{code}/`, and `python3 scripts/i18n.py check {code}` checks it.

## The one rule about paths

**Leave every path in English, exactly as it is**: `About/me.md`, `Skills/brain-keeper/daily.md`, `[[goals]]`, `` `Projects` ``. The build script swaps them for your folder and note names, so they're spelled the same in every file. If you translate a path by hand, it won't match.

You choose the names once, in the `paths` section of `{code}.json`.

## Folder and note names

- Short, everyday words a person would use for that folder. Not a dictionary translation if people say it differently.
- Safe as file names on Mac, Windows and phones: no `/ \ : * ? " < > |`, no spaces at the start or end. Letters with accents and non-Latin scripts are fine.
- Top folders (`About`, `Daily`, `Projects`, `Relationships`, `Memory`, `Library`, `Skills`) start with a capital letter where the language has capitals. Subfolders and note names are lowercase where the language has case, with hyphens between words.
- One name per idea: `research` is the same word as a folder in Projects and in Memory.
- Keep these in English, they aren't in the list: `CLAUDE.md`, `README.md`, `.claudeignore`, `.backups/`, `no-ai-slop`, `SKILL.md`, `eval.md`, `LICENSE`.

## What stays English

- Paths and `[[links]]` to fixed notes (the script handles them).
- Placeholders in curly braces: `{Name}`, `{Language}`, `{lang}`, `{Time zone}`, `{Fix mode}`, `{keeper time}`, `{brief time}`, `{n}`, `{name}`, `{person}`, `{title}` and the rest. Copy them as they are.
- Info blocks (the lines between `---`): keys and values stay English (`type: daily`, `status: active`, `tags: [...]`). Only the `description:` sentence is translated.
- YAML and other code examples: same rule.
- `<!-- ADAPTING ... -->` comments: they're instructions for the agent, removed before anything reaches the person. Leave them in English.
- In forms: the `&#10;` marks (line breaks in examples) stay where they are.

## Trigger phrases

Sentences a person says, in quotes, like "check up my brain" or "prep me for {name}". Write what a person would naturally say in your language, then keep the English one after it: `"faz um check-up no meu cérebro", "check up my brain", or the same in {Language}`. So both work.

## Writing

- Natural, everyday speech. Read each sentence out loud: if a native speaker wouldn't say it that way, rewrite it. Adapt, don't translate word for word.
- About an 8th-grade reading level. Plain and clear, never childish.
- Pick one register and keep it: what popular consumer apps in your language use (for example informal "du" in German apps, informal "você" in Brazilian Portuguese). Write the choice in `GLOSSARY.md`.
- "your agent", never a product name, in anything a person sees.
- No long dashes (the em dash). Use periods, commas, colons or parentheses.
- Keep every fact, rule, number and step. Don't add or remove rules.
- Feature names (Brain Keeper, morning brief, meeting prep, thinking tools, check-up, Writing Check) get a natural name in your language. Phygital Brain stays in English.
- Example names (Ana, Marta, Penguin Kids, Lisbon) can become local names if that reads more naturally. Keep them consistent within the language.

## Review

A second person (or agent) who didn't translate it reads everything as a native speaker would, fixes anything stiff, odd or wrong, and translates a sample back to English to catch changes in meaning. Set `"status": "reviewed-by-ai"` when that's done, and `"reviewed"` only after a native speaker has read it.
