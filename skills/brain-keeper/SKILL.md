---
name: brain-keeper
description: Set up, update, pause or run the Brain Keeper, which looks after a Phygital Brain in two ways, a daily tidy on its own and a full check-up when asked. The brain setup installs it; use this skill on its own when the person says "set up my brain keeper", "update the brain keeper", or the same in another language.
---

# Phygital Brain: Brain Keeper

Version 0.1.6. Everything below is for the agent. Follow it step by step, and check each step before moving on.

The Brain Keeper looks after the brain in two ways:

- **Every day, on its own:** it makes tomorrow's daily note and closes old ones, lists open decisions in today's note, fixes small things (missing info, tags, punctuation, at most 5 a day), and writes a short report plus a list of things only the person can decide. It never deletes, moves or rewrites notes.
- **Check-up, when the person asks** ("check up my brain"): a full look at the whole brain, a list of problems with suggested fixes, and fixes only with their yes.

Templates, in this skill's folder: `templates/daily.md`, `templates/check-up.md`, `templates/queue.md`, `templates/root-CLAUDE-section.md`.

**Language:** if the root `CLAUDE.md` has a `## Folder map` and the brain's language has a ready set (`../brain-setup/i18n/{code}/keeper/`, code from the version line), use those templates instead, and the brain's own folder and note names for every path in this file. If it has a `## Folder map` but no ready set, translate the English templates as you write them, following `../brain-setup/translating.md`, with the brain's names from the Folder map (choose any missing ones the same way, without asking). With no Folder map, use the English templates and write in the brain's language.

**Called from the brain setup** (`../brain-setup/SKILL.md` 3.8): start at Step 2 with the run time and fix mode the setup gives you, skip Step 1, and skip Step 5 (the setup's finish message covers it).

## Principles

- **Clicks over typing.** Use click questions (AskUserQuestion) for every choice. If that tool isn't there, numbered options in chat.
- **Plain language.** Short sentences, everyday words, no jargon. Say "your agent", never a product name.
- **Never use em dashes.** Use periods, commas or colons.
- **Work quietly.** Summarise once at the end.
- **Their brain, their rules.** The root `CLAUDE.md` wins over this file whenever they disagree, except the Hard rules in `daily.md`.

## Step 0: Checks

1. **Is the brain set up?** No `CLAUDE.md` in the folder root: say "This folder doesn't have a second brain yet. Say 'Set up my second brain' first." Then stop.
2. **Which version?** The first line of the root `CLAUDE.md` is `<!-- Phygital Brain, version X, language: xx -->`. If it's missing: say "This folder doesn't have a Phygital Brain yet. Say 'Set up my second brain' first." Then stop. If X is older than this skill's version: say "Your brain needs an upgrade first. Say 'Upgrade my second brain'." Then stop.
3. **Language.** Read the Language section of the root `CLAUDE.md` and write everything in that language. Folder names, file names, `[[links]]` to files, and info block keys and values stay in English.
4. **Already installed?** If `Skills/brain-keeper/daily.md` exists, ask (header `Keeper`): `Update the Brain Keeper` (rewrite `daily.md` and `check-up.md` from the templates with their current settings, keep `queue.md` and the reports) · `Move it to the cloud` (go to Step 3, In the cloud) · `Cancel`. If they said "run the brain keeper in the cloud", go straight to Step 3, In the cloud.
5. **Read their setup.** From the root `CLAUDE.md` and `About/me.md`: their first name, their time zone (root rule 30, or the "How I want my agent to work" section) and their work days.
6. **Scheduled tasks.** Check whether you can create a scheduled task in this app. Remember the answer for Step 3.

## Step 1: Two questions (click questions)

1. **"When should the daily tidy run?"** (header `Run time`)
   - `6:00, early morning (Recommended)`: done before you start your day
   - `8:00, morning`
   - `13:00, lunchtime`
   - `21:00, evening`
2. **"What can it fix on its own?"** (header `Fixes`)
   - `Small safe fixes (Recommended)`: info blocks, tags, em dashes, old note status. At most 5 a day. Everything else goes on a list for you.
   - `Report only`: it only looks after the daily notes and writes a report. Every fix goes on a list for you.

Set FIX MODE to `safe fixes` or `report only`.

3. **"Where should it run?"** (header `Where`), only if this app can create cloud routines and the brain is in a cloud drive with a cloud connector:
   - `On this computer (Recommended)`: runs while the app is open and the computer is awake
   - `In the cloud`: runs even when the computer is off (Step 3, In the cloud)

## Step 2: Build

1. Create `Skills/brain-keeper/daily.md` from `templates/daily.md`. Replace `{Name}`, `{Time zone}` and `{Fix mode}`.
2. Create `Skills/brain-keeper/check-up.md` from `templates/check-up.md`. Replace `{Name}` and `{Language}`.
3. Create `Skills/brain-keeper/queue.md` from `templates/queue.md`, unless it already exists (an upgrade moved the old one). Replace `{Name}`.
4. Don't create `Skills/brain-keeper/reports/` yet. The first run creates it.
5. The root `CLAUDE.md` needs the section from `templates/root-CLAUDE-section.md` once. A new brain already has it. If it's missing, add it right after the Knowledge Routing section, and replace `{Name}` and `{Language}`.
6. `Skills/CLAUDE.md` needs one Installed row: Skill "Brain Keeper", folder `brain-keeper/`, what it does "Daily tidy on its own, and a check-up when {Name} asks". A new brain already has it. If it's missing, add it in the same style as the other rows.

They asked for the install (or the setup did), so these `CLAUDE.md` changes are approved (root rule 9).

**Check:** `daily.md`, `check-up.md` and `queue.md` exist; the root `CLAUDE.md` has the Brain Keeper section once; `Skills/CLAUDE.md` has the row once; no `{Name}`, `{Time zone}`, `{Language}` or `{Fix mode}` left; no em dashes.

## Step 3: Schedule

Two ways to run it. **On this computer** is the default. **In the cloud** keeps it running when the computer is off.

### On this computer

If scheduled tasks are available:

1. Create a scheduled task called `brain-keeper-daily`, at the chosen time, on their work days (every day if unknown), running on this folder, with this prompt:

   > Open my second brain folder. Read `Skills/brain-keeper/daily.md` and do exactly what it says. This is a scheduled run: no questions, no confirmations.

2. **Check:** list the scheduled tasks and confirm it's there, with the right time and folder.

If scheduled tasks aren't available: skip this step, and tell them in the finish message to say "run the brain keeper" once a day.

### In the cloud

Only if {Name} chose it, the agent app can create cloud routines (in Claude: routines, set up with `/schedule` in Claude Code, in the desktop app or on the web), and the brain folder is reachable through a cloud connector for their drive (for example the Google Drive connector). A connector or MCP server that runs only on {Name}'s computer can't be used by a cloud routine.

1. Check the connector can read, edit and create files in the brain folder: read `CLAUDE.md`, then create and delete a test file in `Skills/brain-keeper/` (tell {Name} first). If it can read but not write, say so, and keep the local schedule instead, or offer a cloud run in `report only` mode that writes only its report.
2. Create a routine called `brain-keeper-daily`, at the chosen time, on their work days, with the drive connector turned on, plus the connectors for the apps listed in `Skills/connected-apps/connected-apps.md` (if they're cloud connectors), and this prompt (fill in the folder name):

   > Use the {drive} connector to open the folder "{brain folder}". Read `Skills/brain-keeper/daily.md` in it and do exactly what it says, reading and writing through the connector. This is a scheduled cloud run: no questions, no confirmations. Use the time zone in the root `CLAUDE.md` for dates.

3. Remove the local `brain-keeper-daily` task if there is one, so it doesn't run twice.
4. **Check:** list the routines and confirm it's there with the right time and connectors. Then run it once by hand with "This is a dry run." added to the end of the prompt, so it only writes its report.

The morning brief can move to the cloud the same way, with its own routine. Nobody reads a cloud run's chat, so its prompt says: "Read `Skills/morning-brief/morning-brief.md` and write the brief into today's daily note under 'Morning brief', instead of replying."

Each cloud run starts fresh, with no memory of the last one. Everything it needs is in the brain's files, so that's fine.

## Step 4: Test run

Run the daily tidy once now as a **dry run**: follow `daily.md`, but change nothing except writing the report. Title it "Dry run" and list what the Brain Keeper *would* have done.

**Check:** `Skills/brain-keeper/reports/YYYY-MM-DD.md` exists, has every section of the report shape, and no note other than the report was changed. If something failed, fix the cause and run the dry run again.

## Step 5: Finish

One short message:

1. **What it does:** one line, and the time it runs (or "when you say 'run the brain keeper'").
2. **What it found in the test:** 2 or 3 lines from the dry run.
3. **How to talk to it:** "check up my brain", "pause the brain keeper", "resume the brain keeper", "what did the brain keeper do".
4. **Where things are:** reports in `Skills/brain-keeper/reports/`, things that need you in `Skills/brain-keeper/queue.md`. When something needs you, a line appears in that day's daily note.

Then stop.
