# Changelog

## 0.1.0 (2026-10-20)

First version.

- The setup asks four one-window forms: about you, your work, your days and people, and files. Most answers are clicks, every choice has an "Other" box, and anything can be skipped.
- Form 2 starts with three questions your agent writes for your own kind of work.
- Seven folders: `About/`, `Daily/`, `Projects/`, `Relationships/`, `Memory/` (with private `finances/`), `Library/` and `Skills/`, each with its own rules.
- The Brain Keeper: a daily tidy that runs by itself, and a check-up when you ask. It's set up with the brain.
- An optional morning brief on your work days.
- Every brain gets the no-ai-slop skill by Peter Yang (MIT License) for the Writing Check, and work habits adapted from Andrej Karpathy's guidelines.
- Questions say "your agent", so the brain works with Claude, Codex and other agents. Rule files are `CLAUDE.md`; other agents point their own file at them.
- [Baalda](https://github.com/naveedharri/baalda) is the notes app.
- A cloud drive (Google Drive, Nextcloud, Dropbox or any drive your agent can connect to) and Baalda are part of the setup unless you say no. The setup checks for them and helps you set them up, so you can use your brain from your phone ([phone guide](docs/phone.md)).
- Works in any language: your agent translates the forms and messages, and file and folder names stay in English.
- At the end, your agent writes a short text for your agent's settings, so it talks the same way in every chat.
