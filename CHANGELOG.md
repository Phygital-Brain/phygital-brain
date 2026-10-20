# Changelog

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
- [Baalda](https://github.com/naveedharri/baalda) is the notes app.
- A cloud drive (Google Drive, Nextcloud, Dropbox or any drive your agent can connect to) and Baalda are part of the setup unless you say no. The setup checks for them and helps you set them up, so you can use your brain from your phone ([phone guide](docs/phone.md)).
- Ready in 11 languages (English, Chinese, Hindi, Spanish, Arabic, French, Portuguese (Brazil), Russian, Indonesian, German, Japanese): forms, rules, folder and note names, the Brain Keeper and messages, translated once and built by `scripts/i18n.py`. Any other language works with live translation and English folder names.
- The `add-language` skill makes a full set for a new language, or switches a brain to another language.
- At the end, your agent writes a short text for your agent's settings, so it talks the same way in every chat.
