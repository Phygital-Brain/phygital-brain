# Changelog

## 0.1.8 (2026-10-20)

- Phone-only setup: with no cloud drive connected, your agent now helps you connect one, in your language, after the welcome. Google Drive (with a free account if you need one), Dropbox, OneDrive, Nextcloud or another drive. iCloud can't work from a phone yet, and your agent says so. There's no "later" on a phone, because the brain needs the drive.

## 0.1.7 (2026-10-20)

- The language window shows the main languages (English, Portuguese, Spanish, French, German, Arabic, Japanese, Chinese) and Other. Every other ready language is typed in Other.
- A warmer, shorter finish: your agent welcomes you as your personal assistant, invites you to ask anything, and shows how to start. No list of what was built.
- Baalda is offered at the very end, after the brain is built, and only that once.
- The finish message no longer asks you to copy a text into your agent's settings. Only the phone-only setup still does, because a phone chat needs it to find the brain.

## 0.1.6 (2026-10-20)

- A welcome screen right after the language question: the name, what Phygital Brain is in a few lines, and Continue.
- The language question is a window with every ready language, in its own name.
- The cloud drive check now comes after the language, so it's asked in the person's language. With no drive connected: **Set it up now** (pick Google Drive, Dropbox, OneDrive, Nextcloud, iCloud or another drive, with short steps) or **Set it up later**.
- A test file checks that the drive really sees the brain folder, and is deleted after.
- On a phone, every step uses plain click questions instead of windows.

## 0.1.5 (2026-10-20)

- The Brain Keeper's check-up says when a new version of Phygital Brain is out, and how to get it.

## 0.1.2 (2026-10-20)

- A language that isn't ready is now translated in full during the setup, folder and note names included, without questions. The rules are in `skills/brain-setup/translating.md`.
- Ready languages also count when typed in English (German) or as a code (de).
- Add more skills: a guide to editing images with PhotoCraft, an open-source editor similar to Photoshop.
- A push to main that raises the version now releases it by itself: npm, and the GitHub release with the Claude desktop file.

## 0.1.1 (2026-10-20)

- Install from npm: `npx -y phygital-brain`. The Cursor and VS Code buttons and every connector config use it.
- Each GitHub release now publishes to npm by itself and attaches the Claude desktop file.
- A simpler install guide: what you need first, a one-line install for Codex, and one terminal section.
- A "Yours to keep" section in the README: your notes are yours, they work with any AI, and your agent remembers you.

## 0.1.0 (2026-10-20)

First version.

- The setup asks four one-window forms: about you, your work, your days and people, and files. Most answers are clicks, every choice has an "Other" box, and anything can be skipped.
- Form 2 starts with three questions your agent writes for your own kind of work.
- Seven folders: `About/`, `Daily/`, `Projects/`, `Relationships/`, `Memory/` (with private `finances/`), `Library/` and `Skills/`, each with its own rules.
- The Brain Keeper: a daily tidy that runs by itself, and a check-up when you ask. It's set up with the brain.
- An optional morning brief on your work days.
- Meeting prep, thinking tools (challenge an idea, patterns, contradictions) and import as skills in every brain.
- Backups before big changes, kept 10 days in a hidden `.backups/` folder, with "undo the last change".
- Connected apps, read only: email and calendar notes from the Brain Keeper's daily run.
- The Brain Keeper can run as a cloud routine, through the cloud drive's connector.
- Teams: "set up my team" adds a Team section, for brains shared through Baalda's cloud.
- Every brain gets the no-ai-slop skill by Peter Yang (MIT License) for the Writing Check, and work habits adapted from Andrej Karpathy's guidelines.
- Questions say "your agent", so the brain works with Claude, Codex, Hermes Agent, OpenClaw and other agents. Rule files are `CLAUDE.md`; other agents point their own file at them.
- One-click install: a Claude desktop extension (`.mcpb`), Add to Cursor and Add to VS Code buttons, and a connector (an MCP server with no dependencies) that runs with `npx -y phygital-brain` (npm) for Codex, Hermes Agent, OpenClaw and other agents.
- [Baalda](https://github.com/naveedharri/baalda) is the notes app.
- A cloud drive (Google Drive, Nextcloud, Dropbox or any drive your agent can connect to) and Baalda are part of the setup unless you say no. The setup checks for them and helps you set them up, so you can use your brain from your phone ([phone guide](docs/phone.md)).
- Ready in 11 languages (English, Chinese, Hindi, Spanish, Arabic, French, Portuguese (Brazil), Russian, Indonesian, German, Japanese): forms, rules, folder and note names, the Brain Keeper and messages, translated once and built by `scripts/i18n.py`. Any other language works with live translation and English folder names.
- The `add-language` skill makes a full set for a new language, or switches a brain to another language.
- At the end, your agent writes a short text for your agent's settings, so it talks the same way in every chat.
