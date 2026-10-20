---
name: brain-setup
description: Build a Phygital Brain second brain in the selected folder through four short forms, then set up its daily Brain Keeper. Use when the person says "set up my second brain", "build my brain", "upgrade my second brain", "set up my team", or the same in another language.
---

# Phygital Brain: Setup

Version 0.1.1. Everything below is for the agent. Follow it step by step, and check each step before moving on.

## What you are building

A second brain: a folder of notes that is both the person's knowledge base and your operating system. You show four short forms, then build the folders, the rule files (`CLAUDE.md`), their first notes and the Brain Keeper. When a new chat opens in this folder later, you read those rules and follow them.

Files you use, all in this skill's folder:

| File | What |
|---|---|
| `forms/form-1-about-you.html` ... `form-4-files.html` | The four forms, as HTML for the form window |
| `forms/questions.md` | The same questions as plain text, for when the form window can't open |
| `templates/` | Every file the brain gets, with `{placeholders}` |

The Brain Keeper lives in the next skill: `../brain-keeper/SKILL.md`.

## Principles

- **One window per step.** Each form is one window: the person clicks, types short answers, drops files and presses one button. You get all the answers at once. Then the next form opens. No chat between forms.
- **About 10 minutes.** No follow-up questions inside a form. Accept whatever they give. Skipped questions stay empty.
- **Adapt.** Skip what you already know. Skip business questions for people who don't sell anything.
- **Real content only.** Never write placeholders like `[name]` or `TBD`. No information for a section: leave the section out. No information for a file: don't create it.
- **Their words.** Keep their exact names, numbers and phrases.
- **Plain language.** Short sentences, everyday words, no jargon, in every question and every file.
- **"Your agent", never a product name,** in every question and message the person sees.
- **Never use em dashes** in anything you write. Use periods, commas or colons.
- **Work quietly.** Don't narrate each file. One short message at the end.

## Which agent you are

The brain's rule files are `CLAUDE.md`. If you are Claude, read them as they are.

If you are another agent and your tool loads a different rule file (for example `AGENTS.md` in Codex), then at the end of the build, next to each `CLAUDE.md`, add that file with one line: `Read CLAUDE.md in this folder and follow it.` One set of rules, never two copies. Skip this if your tool already reads `CLAUDE.md`.

## Step 0: Checks

1. Confirm you can write to the selected folder. No folder selected: ask them to pick their brain folder (the one inside their cloud drive, see the Getting started guide) and send the message again.
2. If a `CLAUDE.md` exists in the folder root, read its first line:
   - `<!-- Phygital Brain, version X, language: xx -->`: a Phygital Brain is already here. Ask one question (header `Setup`): `Upgrade my brain` (only if X is older than this skill's version, goes to **Step U**) · `Update my answers` (keep everything, redo the forms, refresh the About files) · `Cancel`.
   - Any other `CLAUDE.md`: this folder already has rules from something else. Don't build here. Ask them to pick an empty folder for their brain.

   Never delete or overwrite existing notes.
3. If the folder has other files, don't touch them. Build around them and mention them at the end.
4. **Cloud drive and Baalda.** Both are part of the brain unless the person says they don't want them. A cloud drive lets them use the brain from their phone, so it matters most. Check each one, and for anything missing, say in one line why it helps and ask (click options):
   - **Is the folder inside a cloud drive?** Look at the folder's path. Common signs: on a Mac, `~/Library/CloudStorage/` (Google Drive, Dropbox, OneDrive), `~/Library/Mobile Documents/` (iCloud), a `Nextcloud` or `Dropbox` folder in the home folder; on Windows, a `G:` drive (`My Drive`), or a `Dropbox`, `OneDrive` or `Nextcloud` folder. If you can't tell, ask: "Is this folder synced to a cloud drive?" If not: `Help me move it to a cloud drive` (ask which drive they use, walk them through Getting started step 2: install the drive's desktop app, make the folder inside it, then pick that folder for a new chat and say "Set up my second brain" again; then stop) · `Continue without a cloud drive` (the brain stays on this computer only; add "No cloud drive: this brain is on one computer only." to `About/tools.md` later).
   - **Is the drive connected to your agent?** It must be able to read, edit and create files in the drive from the agent's phone or web app. If you have no tools for their drive in this chat: `I'll connect it now` (in Claude with Google Drive: Settings, then Connectors, then Google Drive; with another drive, its connector or MCP server; wait, then go on) · `Later` (mention it again in the finish message).
   - **Is Baalda installed?** Ask: `Yes` · `Install it now` (give the link https://github.com/naveedharri/baalda, wait, then go on) · `Not now`.
5. **Form window.** Check whether you can show an HTML form window (in Claude, the `show_widget` tool). Remember the answer. If you can't, use `forms/questions.md` in Step 2: click questions where you have them (AskUserQuestion, up to 4 questions per call), otherwise numbered options in chat.

## Step 1: Language

Ask one question with click options, in the language of their first message (English if unclear): **"Which language should your brain speak?"** The ready languages, each with its code:

`English` (en) · `中文` (zh-CN) · `हिन्दी` (hi) · `Español` (es) · `العربية` (ar) · `Français` (fr) · `Português (Brasil)` (pt-BR) · `Русский` (ru) · `Bahasa Indonesia` (id) · `Deutsch` (de) · `日本語` (ja) · Other

If the click tool takes only 4 options, offer the 3 most likely from their first message plus Other, and accept any of the names above typed in.

### A ready language (a folder `i18n/{code}/` exists in this skill)

The brain is built fully in that language, once, from files that are already translated. Don't translate anything yourself.

- **Forms:** use `i18n/{code}/forms/` instead of `forms/`.
- **Templates:** use `i18n/{code}/templates/` instead of `templates/`, and pass `i18n/{code}/keeper/` to the Brain Keeper (3.8) as its templates.
- **Messages:** say the setup's messages from `i18n/{code}/strings.json` (`messages`), and use its `features` names for the Brain Keeper, morning brief and the rest.
- **Folder and note names:** `i18n/{code}/strings.json` (`paths`) maps every English name to its name in that language. Wherever this file names a brain path in English (`About/me.md`, `Skills/brain-keeper/`, `[[goals]]`), use the mapped names. The templates in `i18n/{code}/` already use them.
- **Folder map:** at the end of the root `CLAUDE.md`, add a `## Folder map` section: a two-column table, English name and the brain's name, for every entry in `paths`, with one line above it: "For Phygital Brain upgrades and skills only. Daily work uses the names in this brain." This is the only place the English names appear in the brain.

### Any other language

Use the English `forms/` and `templates/`, and translate as you go: before showing a form, translate only the text people see (questions, option labels, placeholders, the header and the buttons). Write every message and note in their language. Folder and note names stay in English, and no Folder map is needed. Say once: "Your brain's folders will have English names. To make a full set for your language, say 'translate Phygital Brain into my language'."

### In every language

These stay in English, so the rules and the Brain Keeper work the same everywhere:

- The file names `CLAUDE.md`, `README.md` and `.claudeignore`, and the `.backups/` and `Skills/no-ai-slop/` folders.
- Info block (frontmatter) keys and values: `type: daily`, `status: active`, `day: Monday`, every tag. The one exception is `description:`, a sentence in their language.
- Every `data-name` and `data-value` in the forms, so the answers come back the same in every language.

Portuguese always means Brazilian Portuguese (pt-BR). Names they give (their projects, people, companies) stay exactly as they wrote them.

## Step 2: The forms

Send one short message first: "About 10 minutes: mostly clicks, a few short answers. Skip anything you like."

For each form: read the file, take out every `<!-- ... -->` comment and the blocks the comments tell you to remove, translate if needed, and show it. Wait for the answers before the next form.

### Form 1: About you (`forms/form-1-about-you.html`)

Show as it is.

**Switches**, from the answers:

- **BUSINESS** = on if `selling` is `Yes, services or clients`, `Yes, products` or `Not yet, planning to`. Otherwise off.
- **BRIEF** = on if `help` includes `Organise projects` or `Goals and decisions`. Otherwise off.
- **WRITE** = on if `help` includes `Write for me`.

If they gave a link, read it (web fetch) and pull facts from it: services, clients, bio, tone. Don't ask them to confirm each fact.

**Time zone:** from the city (Lisbon gives `Europe/Lisbon`, São Paulo gives `America/Sao_Paulo`). No city: the computer's time zone.

### Form 2: Your work (`forms/form-2-your-work.html`)

Before showing it:

1. **Job questions.** Replace the `JOB QUESTIONS` block with 3 questions written for what they do (from `name` and `you` in form 1, and the link if you read one). Follow the example in the block: one choice question about the kind of work, one text question about who they work with or for, one choice question about how they charge or measure their work. Every choice question gets an `Other` option. Header: "your work as {what they do}". Use `data-name` values `job_type`, `job_clients`, `job_pricing`. If they picked `Personal projects`, ask about the projects instead (what kind, who's involved, how much time they have).
2. Keep the `BUSINESS ON` block if BUSINESS = on, otherwise the `BUSINESS OFF` block. Remove the other.

### Form 3: Your days and people (`forms/form-3-days-and-people.html`)

Before showing it: remove the `Clients` option if BUSINESS = off. Remove the `VOICE` block unless BUSINESS = on and WRITE = on. Remove the `BRIEF` block if BRIEF = off.

### Form 4: Files (`forms/form-4-files.html`)

Show as it is. Read every file they drop and every link they paste.

If `brief_time` is `No brief`, set BRIEF = off.

**Check before building:** you have their name, BUSINESS, BRIEF, the language and the time zone. If the name is missing, ask for it once in chat.

## Step 3: Build

### 3.1 Folders

Always create:

```
About/
Daily/
Projects/
Memory/decisions/
Memory/research/
Memory/finances/
Memory/archive/
Library/
Skills/brain-keeper/
Skills/no-ai-slop/
Skills/import/
Skills/meeting-prep/
Skills/thinking/
Skills/connected-apps/
Relationships/
```

If BRIEF = on, also `Skills/morning-brief/`. The Brain Keeper's files go in `Skills/brain-keeper/` in 3.8. `Memory/finances/` is private: it's listed in `.claudeignore`.

Relationships subfolders only for what they picked in form 3 (`people`):

| Picked | Folder |
|---|---|
| Clients | `Relationships/Clients/` |
| Collaborators | `Relationships/Collaborators/` |
| Team or freelancers | `Relationships/Team/` |
| Partners, press or venues | `Relationships/Partners/` |

`Just me` or nothing: no subfolders yet. A key person who fits none of the picked types: create the matching folder anyway.

Never create empty extra folders "just in case". Project subfolders, `Memory/applications/` and `Memory/competitors/` appear later, when content needs them.

### 3.2 Rule files

| File | Template |
|---|---|
| `CLAUDE.md` (root) | `templates/root-CLAUDE.md` |
| `About/CLAUDE.md` | `templates/about-CLAUDE.md` |
| `Projects/CLAUDE.md` | `templates/projects-CLAUDE.md` |
| `Daily/CLAUDE.md` | `templates/daily-CLAUDE.md` |
| `Memory/CLAUDE.md` | `templates/memory-CLAUDE.md` |
| `Library/CLAUDE.md` | `templates/library-CLAUDE.md` |
| `Skills/CLAUDE.md` | `templates/skills-CLAUDE.md` |
| `Relationships/CLAUDE.md` | `templates/relationships-CLAUDE.md` |
| `Relationships/{Subfolder}/CLAUDE.md`, one per subfolder | `templates/relationships-subfolder-CLAUDE.md` |
| `Skills/morning-brief/morning-brief.md` (only if BRIEF = on) | `templates/morning-brief.md` |
| `.claudeignore` | `templates/claudeignore.txt` |
| `Skills/import/import.md` | `templates/import.md` |
| `Skills/meeting-prep/meeting-prep.md` | `templates/meeting-prep.md` |
| `Skills/thinking/thinking.md` | `templates/thinking.md` |
| `Skills/connected-apps/connected-apps.md` | `templates/connected-apps.md` (see 3.7b) |
| `Skills/no-ai-slop/SKILL.md`, `eval.md`, `LICENSE` | `bundled/no-ai-slop/`, copied unchanged (not a template: no placeholders, no edits) |

Some templates start with an `ADAPTING` comment for you: follow it, then leave it out of the file. In every template:

- Replace `{Name}` with their first name, `{Time zone}` with their time zone, `{Language}` with the language name and `{lang}` with its code (`en`, `pt-BR`, `es`...).
- Remove table rows and rules for files or folders that weren't created, unless the row says "created on first use".
- Keep everything under "Always stays in English" (Step 1) in English. Write the rest in their language.

**Check:** every file in the table exists, and none of `{Name}`, `{Time zone}`, `{Language}` or `{lang}` is left. Path patterns in routing tables (`Projects/{name}/`, `{title}`, `{topic}`, `{skill-name}`, `{client-name}`) stay as they are.

### 3.3 About files (only when there's real information)

Use `templates/about-file.md` for the shape: current truth at the top, dated evidence below, newest first.

| File | Create when | Category tag | Fill from |
|---|---|---|---|
| `me.md` | Always | `identity` | Name, what they do, city, time zone, strengths, values and work they say no to, how they take things in, when they focus and what drains them, work days, the link, the job answers from form 2 when BUSINESS = off |
| `goals.md` | Always | `goals` | The 12-month goal (and their own words), the areas that matter most (BUSINESS = off), the projects that serve it, what's worrying them now |
| `business.md` | BUSINESS = on | `business` | What they sell, how they work, how customers find them, the job answers from form 2 |
| `services.md` | They named services, products or prices | `business` | Each offer: what it is, who it's for, how they charge |
| `customers.md` | BUSINESS = on and customers answered | `customers` | Who buys, how they find them, past clients from form 2 |
| `pain-points.md` | "What slows you down" answered | `customers` (BUSINESS on) or `goals` (off) | Their own pains, in their words |
| `brand.md` | Voice answered, social media given, or a link showed a clear tone | `brand` | Voice, words they use, words to avoid, social media accounts |
| `tools.md` | Comms, notes or tools answered | `tools` | Where they talk to people, where notes and work live today, social media accounts |
| `cv.md` | They dropped a CV or a link listed their history | `career` | Work history, education, press, awards, newest first |
| `biography.md` | They dropped an About page or bio with their story | `identity` | Their story in their words |

In `me.md`, also add a **How I want my agent to work** section:

- Their style choice, for example "Short and plain: a few short sentences, everyday words, no jargon."
- How they take things in, for example "Short lists and examples."
- `Language: {Language}.`
- `Time zone: {Time zone}.`
- `Work days: {days}.` and when they focus best.

If a file gave their full date of birth, it goes only in `me.md` (root rule 25).

Anything from form 4's `anything_else` box goes where it fits by the table above (a preference in `me.md`, a goal in `goals.md`, a project in 3.4). Old notes from form 4 are not filed during the build: the finish message offers to bring them in.

### 3.4 Projects

For each project from form 2 (`projects`), create `Projects/{Project-Name}/README.md` from `templates/project-readme.md`. Their project name, with hyphens instead of spaces.

### 3.5 People

Key people from form 3 (`key_people`), and real people or companies named in answers, files or links. One note each, in the right Relationships subfolder, with the info block from `templates/relationships-CLAUDE.md` and the profile structure from `templates/relationships-subfolder-CLAUDE.md`. Search first so you never make two notes for the same person. Never invent people.

### 3.6 Their own rules

If they named work they say no to (form 1, `values`), add it as the first rule under `{Name}'s Rules` in the root `CLAUDE.md`, in their words: "33. Work {Name} says no to: ..." (31 if BUSINESS = off).

### 3.7 First daily note

`Daily/YYYY-MM-DD.md` (today, in their time zone) from `templates/daily-note.md`. Don't create `Daily/tasks.md` yet: it's created when the first task comes up.

### 3.7b Connected apps

Look at which connectors you have in this chat for the apps {Name} named in form 3 (`comms`, `notes_now`): email (for example Gmail or Outlook), calendar (Google Calendar or Outlook), and their cloud drive. Then ask one question (click options, multi): "Which of these should your brain read from?" with one option per connected app, and `None for now`. Write the ones picked into `Skills/connected-apps/connected-apps.md` under Connected, read only, in the shape its ADAPTING note shows. An app {Name} uses but hasn't connected: mention it in the finish message with the guide link https://github.com/Phygital-Brain/phygital-brain/blob/main/docs/connect-your-apps.md.

### 3.8 Brain Keeper

Set it up now, so nobody has to come back for it. Follow `../brain-keeper/SKILL.md` from its Step 2, without its questions:

- **Run time:** one hour before the morning brief time from form 3. BRIEF = off: 8:00 on their work days.
- **Fix mode:** `safe fixes`.
- **Where it runs:** on this computer, as a scheduled task. If your app can create cloud routines (in Claude: routines) and the brain is in a cloud drive with a cloud connector, ask one question: `On this computer` · `In the cloud, even with my computer off`. For the cloud, follow `../brain-keeper/SKILL.md` Step 3, cloud.

If BRIEF = on, also schedule the morning brief (the Schedule part of `Skills/morning-brief/morning-brief.md`) at that time, on their work days, without asking again.

The Brain Keeper's check-up (`check-up.md`) has no schedule: it runs when they ask.

### 3.9 Check your work

Fix anything that fails, then check it again.

- No file has leftover placeholders (`[name]`, `TBD`, `{Name}`, `{Time zone}`, `{Language}`, `{lang}`, `{Fix mode}`, `{keeper time}`, `{brief time}`, `{n}`) or em dashes. Path patterns in routing tables stay.
- Every routing table lists only folders and files that exist, except rows marked "created on first use".
- Every note links to at least one other note.
- No files in the folder root except `CLAUDE.md`, `.claudeignore`, `.backups/` (and the other agent's rule file, if you added one).
- The root `CLAUDE.md` starts with the version line and has the Language section.
- Every note has a complete info block, keys and values in English.
- Rule numbers in the root `CLAUDE.md` run with no gaps, and `{Name}'s Rules` is the last section.
- No `[[link]]` to a file was translated.
- The Brain Keeper checks in `../brain-keeper/SKILL.md` Step 2 and Step 3 pass.

## Step 4: Finish

One short message, no recap:

1. **What was built:** folders, About pages, projects, and how many people pages. One or two lines.
2. **Open it in Baalda:** open Baalda (https://github.com/naveedharri/baalda) and open this folder.
3. **How to use it every day:** open a chat on this folder and talk normally. For example: "I had a call with X, here's what we agreed", "New project: ...", "Write a reply to this email". Your agent files everything in the right place.
4. **Keep it healthy:** the Brain Keeper tidies every day at {keeper time}. Say "check up my brain" anytime.
5. **Only if BRIEF = on:** your morning brief comes at {brief time} on work days. Say "morning brief" anytime.
6. **On your phone** (if the brain is in a cloud drive): "Your brain is in your cloud drive, so you can use it from your phone." One line on each: ask about your notes in your agent's phone app with the drive connected, and send tasks to your computer if your agent can (in Claude, Dispatch). Point to the phone guide: https://github.com/Phygital-Brain/phygital-brain/blob/main/docs/phone.md. If the drive isn't connected yet, say how to connect it.
7. **Instructions for every chat:** "Want your agent to talk like this in every chat, not only in your brain? Copy this into your agent's settings." Then the text in a box they can copy (see below), and where it goes: in Claude, the personal instructions box in Settings; in other agents, their custom instructions.
8. **Only if they gave old notes in form 4:** "Want me to bring in your old notes now?" If yes, follow `Skills/import/import.md`.
9. **One line on the extras:** "You can also say 'prep me for Marta', 'challenge my idea', or 'undo the last change'."

Then stop.

### The instructions text

Write it in their language, 3 to 5 short sentences, from their answers. No names, no private details, nothing about this folder. Build it like this:

1. How to talk, from `style`: for example "Use simple, plain words and no jargon. Keep replies short, no walls of text."
2. How they take things in, from `learning`, if answered: for example "Use short lists and examples."
3. Always: "Work step by step and check each step before moving on. Do only what I asked."
4. Only if their language isn't English: "Always answer in {Language}."

Example for "Short and plain" and "Short lists":

```
Use simple, plain words and no jargon. Keep replies short, no walls of text. Use short lists and examples. Work step by step and check each step before moving on. Do only what I asked.
```

## Step U: Upgrade an existing brain

When Step 0 found an older Phygital Brain and they picked `Upgrade my brain`.

1. **Read first, change nothing.** Read every `CLAUDE.md`, `.claudeignore`, `About/me.md`, and the files in `Skills/brain-keeper/`. Note their name, their language (the Language section, or the language their notes are in) and their time zone (from `me.md` or their city; ask once if neither exists).
2. **Count their own rules** under `{Name}'s Rules` in the root `CLAUDE.md` (in a translated brain, the same heading in its language: the last section of the file). Write the number down. You check it again at the end.
3. **Make the list.** Compare their files with `templates/`. List what's new for them in plain words, one line each, grouped by file. Use the CHANGELOG entries newer than their version as a guide.
4. **Ask** (header `Upgrade`): `Upgrade everything` · `Show me each change` · `Cancel`.
5. **Apply, keeping what's theirs:**
   - Add missing sections, routing rows, rules and files, including `Skills/no-ai-slop/` (copied unchanged from `bundled/no-ai-slop/`), `Skills/import/`, `Skills/meeting-prep/`, `Skills/thinking/` and `Skills/connected-apps/` (ask 3.7b's question), and `.backups/` in `.claudeignore`.
   - Make a backup of every file you'll change before you change it (Backups and Undo).
   - Replace the numbered base rules with the new list (1 to 32, or 1 to 30 when they don't sell). Their own rules stay under `{Name}'s Rules`, word for word and in the same order, renumbered to follow on. If one of their rules says the same as a new base rule, keep theirs and mention it.
   - Keep their own routing rows, folders and anything else they wrote that isn't in the templates.
   - Never rewrite notes to new info blocks. Old notes get them the next time they're edited.
   - Replace the version line at the top of the root `CLAUDE.md` with this skill's version: `<!-- Phygital Brain, version X, language: {lang} -->`.
   - **Folder names.** If the root `CLAUDE.md` has a `## Folder map`, use it for every path in the new templates, and the matching `i18n/{code}/` set if one exists. Add map rows for any new folders or notes in this version (from `i18n/{code}/strings.json`, or ask once what to call them).
   - **Brain Keeper.** Update it (follow `../brain-keeper/SKILL.md`, its Step 0.4 keeps `queue.md` and the reports). If it isn't installed, install it from its Step 1.
6. **Check:** the same number of their own rules as in step 2, word for word; every check in 3.9 that applies; nothing deleted.
7. **Finish:** one line in today's daily note, then 2 or 3 lines on what changed.

## Step T: Set up a team

When {Name} says "set up my team". The guide for people is https://github.com/Phygital-Brain/phygital-brain/blob/main/docs/teams.md.

1. **Check the folder is shared.** Ask whether the brain is already shared through Baalda's cloud (or another sync service the team uses). If not, point them to the guide and stop. Don't move or copy the folder yourself.
2. **Ask who's on the team** (one chat message): each person's name, role, and which folders they may change. The person asking is the owner unless they say otherwise.
3. **Back up** the root `CLAUDE.md` (Backups and Undo).
4. **Replace the short Team section** of the root `CLAUDE.md` with the one from `templates/team-section.md`, filled in. Ask first (root rule 9): show the section, then write it after the yes.
5. **For each person:** a note in `Relationships/Team/` (search first, create the folder and its `CLAUDE.md` if needed), and their daily notes folder `Daily/{person}/` (created when their first note is written).
6. **Brain Keeper:** ask whose agent, or which cloud routine, runs it. Only one may. Remove any other schedule. In `Skills/brain-keeper/daily.md`, note under Settings that daily notes are per person, in `Daily/{person}/`.
7. **Finish:** one short message: who's in, what each can change, and that permissions themselves are set in Baalda.

