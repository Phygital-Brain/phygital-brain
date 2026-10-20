# Translating during the setup

For a language with no ready set in `i18n/`. You translate the whole brain yourself, once, while you build it. Don't ask the person anything about the translation: choose every word yourself, following these rules. The brain then reads only its own files, already in their language.

## 1. Choose the names first

Before the first form, choose a name in their language for every English name in the list at the end of this file. Write the list down for yourself and use exactly the same spelling in every file you write, so every path and `[[link]]` matches.

- Short, everyday words a person would use for that folder. Not a dictionary translation if people say it differently.
- Safe as file names on Mac, Windows and phones: no `/ \ : * ? " < > |`, no spaces at the start or end. Letters with accents and non-Latin scripts are fine. Use the NFC form (composed letters).
- The 7 top folders start with a capital letter where the language has capitals. Subfolders and note names are lowercase where the language has case, with hyphens between words.
- One name per idea: `research` is the same word in Projects and in Memory.
- Two names keep their marks: `_Leads` keeps the `_` at the start, and `PAUSED` stays in capitals where the language has them.
- Every name is different from the others in the same folder.

Choose the feature names too, the same way: Brain Keeper, morning brief, meeting prep, thinking tools, check-up, Writing Check and second brain. Phygital Brain stays in English.

## 2. What you translate

- **Forms:** before you show each form, the text people see: questions, option labels, placeholders, the header and the buttons.
- **Messages:** everything you say during the setup.
- **Files:** every file you write from `templates/`, and the Brain Keeper's files from `../brain-keeper/templates/`, as you write them. Swap every English brain path for your names: `About/me.md`, `Skills/brain-keeper/daily.md`, `[[goals]]`, `` `Projects` ``.

## 3. What stays English

- The file names `CLAUDE.md`, `README.md` and `.claudeignore`, and the `.backups/` and `Skills/no-ai-slop/` folders, and everything inside `no-ai-slop/`.
- Placeholders in curly braces until you fill them in: `{Name}`, `{Time zone}`, `{name}`, `{title}` and the rest.
- Info blocks (the lines between `---`): keys and values (`type: daily`, `status: active`, `day: Monday`, every tag). Only the `description:` sentence is translated.
- YAML and other code examples, and every `data-name` and `data-value` in the forms.
- Names the person gives (their projects, people, companies), exactly as they wrote them.

## 4. Trigger phrases

Sentences a person says to their agent, in quotes, like "check up my brain" or "prep me for {name}". Write what a person would naturally say in their language, then keep the English one after it, so both work: `"{in their language}", "check up my brain", or the same in {Language}`.

## 5. Writing

- Natural, everyday speech. Adapt, don't translate word for word. If a native speaker wouldn't say a sentence that way, rewrite it.
- About an 8th-grade reading level. Plain and clear, never childish.
- One register all through: what popular consumer apps in that language use, often the informal "you".
- "your agent", never a product name, in anything a person sees.
- No long dashes (the em dash). Use periods, commas, colons or parentheses.
- Keep every fact, rule, number and step. Don't add or remove rules.

## 6. Folder map

At the end of the root `CLAUDE.md`, add a `## Folder map` section, the same as a ready language gets: a two-column table, English name and the brain's name, for every name in the list below, with one line above it: "For Phygital Brain upgrades and skills only. Daily work uses the names in this brain." Write that line and the heading in their language. This is the only place the English names appear in the brain.

## 7. Check

Before the setup's own checks (3.9):

- No English name from the list is left in a path or `[[link]]`, outside the Folder map and the things that stay English.
- Every `[[link]]` and path points to a name in your list, spelled the same.
- Every folder you named in a `CLAUDE.md` exists.

## The names

These are every folder and note name a new brain can have.

- **Top folders:** `About`, `Daily`, `Projects`, `Relationships`, `Memory`, `Library`, `Skills`
- **Subfolders and notes:** `Clients`, `Collaborators`, `Team`, `Partners`, `decisions`, `research`, `finances`, `archive`, `applications`, `competitors`, `notes`, `briefs`, `drafts`, `ideas`, `feedback`, `assets`, `prompts`, `templates`, `frameworks`, `brain-keeper`, `morning-brief`, `meeting-prep`, `thinking`, `import`, `connected-apps`, `reports`, `me`, `goals`, `business`, `services`, `customers`, `pain-points`, `brand`, `tools`, `cv`, `biography`, `tasks`, `_Leads`, `daily`, `check-up`, `queue`, `PAUSED`
