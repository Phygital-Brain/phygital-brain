# AGENTS.md

Notes for AI agents (Claude Code, Codex, Cursor and others) and people who **change this repository**. Read this before you change a skill, a template, a form or a doc.

> [!NOTE]
> If you are an agent **using** Phygital Brain (building or running someone's brain, not editing this repository), follow [skills/brain-setup/SKILL.md](skills/brain-setup/SKILL.md) to build a brain, or [skills/brain-keeper/SKILL.md](skills/brain-keeper/SKILL.md) for the Brain Keeper. Inside a brain, its own `CLAUDE.md` files are the rules.

## What this is

Phygital Brain builds a second brain: a folder of Markdown notes that works as the person's knowledge base and as the agent's operating system. It's a Claude plugin with two skills. There is no program: everything is instructions, templates and four HTML forms. Licence Apache-2.0. The name and logo are not covered (see [TRADEMARKS.md](TRADEMARKS.md)).

## Layout

```
.claude-plugin/plugin.json        the plugin: name, version, description
.claude-plugin/marketplace.json   lets people add this repo as a plugin marketplace
skills/brain-setup/SKILL.md       the setup: checks, language, four forms, build, finish, upgrade
skills/brain-setup/forms/         the four forms (HTML for the form window) and questions.md (the same in plain text)
skills/brain-setup/templates/     every file a new brain gets, with {placeholders}
skills/brain-keeper/SKILL.md      installs and updates the Brain Keeper
skills/brain-keeper/templates/    daily.md, check-up.md, queue.md, the root CLAUDE.md section
docs/                             for people: getting started, how it works, other agents
docs/folders/                     one page per brain folder, and the main rules in plain words
docs/images/                      the README picture and the logo
languages/                        how other languages work
scripts/check.py                  the checks (no installs needed)
README.md, CHANGELOG.md, NOTICE, LICENSE, TRADEMARKS.md, CONTRIBUTING.md, SECURITY.md, CITATION.cff
```

## How the pieces connect

1. A person says "Set up my second brain". The agent follows `skills/brain-setup/SKILL.md`.
2. It shows the four forms one at a time. Each answer comes back under its `data-name`. Step 2 of the skill sets the switches BUSINESS, BRIEF and WRITE.
3. Step 3 builds the brain from `templates/`, using the answers. Section 3.3 maps each answer to an About file.
4. Step 3.8 runs `skills/brain-keeper/SKILL.md` from its Step 2 to set up the daily tidy.
5. Inside the brain, the agent only follows the brain's own `CLAUDE.md` files. This repository is no longer read.

## Rules that must never break

1. **The templates are the source of truth.** The docs explain the templates in plain words and link to them. When you change a rule in a template, change the matching doc page in the same pull request.
2. **Answer names don't change.** Every `data-name` and `data-value` in a form is read by `SKILL.md`. Rename one only together with every place that reads it. An answer nobody reads is a bug.
3. **English stays English.** Folder names, file names, `[[links]]` to files, and info block keys and values stay in English in every language. Only `description:` is translated.
4. **"Your agent", never a product name,** in anything a person sees. File names like `CLAUDE.md` are fine.
5. **No em dashes,** anywhere. Use periods, commas or colons.
6. **Plain words.** Short sentences, everyday words. The docs are written so a 10-year-old can follow them.
7. **The agent asks before it creates, moves, renames or deletes** a person's notes. Nothing in a skill or template may weaken that.
8. **Private things stay private.** `.claudeignore` keeps `Memory/finances/`. No template may copy private details (tax IDs, bank details, birth date) into other notes or replies.
9. **Upgrades keep what's theirs.** Their notes, their own rules (word for word), their routing rows and their folders survive every upgrade.
10. **Version line.** A brain's root `CLAUDE.md` starts with `<!-- Phygital Brain, version X, language: xx -->`. A new version updates it, the plugin files, the skills' "Version" lines and the CHANGELOG together.
11. **Keep the NOTICE credit:** "Created by Phygital-Brain".

## Placeholders

| Placeholder | Filled with |
|---|---|
| `{Name}` | The person's first name |
| `{Language}`, `{lang}` | The language name and its code (`en`, `pt-BR`) |
| `{Time zone}` | Their time zone, like `Europe/Lisbon` |
| `{Fix mode}` | `safe fixes` or `report only` (Brain Keeper) |
| `{keeper time}`, `{brief time}`, `{n}` | Values in the finish message and first daily note |

Path patterns like `Projects/{name}/`, `{title}`, `{topic}`, `{skill-name}` and `{client-name}` stay in the brain as patterns. They are not filled in.

`<!-- ADAPTING ... -->` comments at the top of a template are instructions for the agent. They never reach the brain.

## Checking a change

1. `python3 scripts/check.py` must pass.
2. For a change to a skill, a form or a template: build a test brain in an empty folder with your change, as two people (one who sells and wants a brief, one who doesn't), and read what was built. For an upgrade change, also upgrade a copy of an older brain.
3. Add a line to `CHANGELOG.md`.
