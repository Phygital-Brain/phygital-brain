# Other agents

Phygital Brain is plain text files and plain instructions. Any agent that can **read and write files in a folder on your computer** can build it, use it and tidy it. Claude is the easiest, because the setup was made for it, but it isn't the only one.

## What works where

| Part | Claude desktop app | Other agents that work in a folder (like Codex or Claude Code) | Chat apps that can't save files |
|---|---|---|---|
| Build the brain | Yes | Yes | No |
| The four form windows | Yes | Usually no: the same questions come in chat | No |
| Daily use: tell it things, it files them | Yes | Yes | No, they can only read |
| Read your brain from anywhere | Yes, with the Google Drive connector | Depends on the app | Yes, if the app can connect to Google Drive |
| Brain Keeper every day, morning brief | Yes, as scheduled tasks | Only if the app can schedule tasks. Otherwise say "run the brain keeper". | No |
| Check-up | Yes | Yes | No |

## What your agent needs

- **Access to your brain folder,** to read and write files in it.
- **The rule files.** Your agent must read `CLAUDE.md` at the top of your brain at the start of every chat, and the `CLAUDE.md` in a folder before it writes there. Claude does this by itself. For other agents, see "Rule files" below.
- **Web access,** optional. It's used to read a link you give in the setup, and for research.

## Setting up with another agent

1. Get this repository onto your computer. On GitHub, use Code, then Download ZIP, and unzip it somewhere outside your brain folder.
2. Make your brain folder in Google Drive, as in [Getting started](getting-started.md) steps 2 and 5.
3. Open your agent on your brain folder.
4. Say:

   > Set up my second brain. Follow `skills/brain-setup/SKILL.md` from the Phygital Brain repository at {where you unzipped it}.

5. Your agent asks the questions in chat, from `skills/brain-setup/forms/questions.md`. Answer them like you would in the forms.
6. At the end, it sets up the Brain Keeper from `skills/brain-keeper/SKILL.md`. If your app can't schedule tasks, it tells you to say "run the brain keeper" once a day.

## Rule files

The brain's rule files are all called `CLAUDE.md`, because most people use Claude. Some agents look for a different name:

| Agent | Looks for |
|---|---|
| Claude (app and Claude Code) | `CLAUDE.md` |
| Codex | `AGENTS.md` |
| Gemini CLI | `GEMINI.md` |

During the setup, your agent checks which name its own tool needs. If it's not `CLAUDE.md`, it puts a small file with that name next to each `CLAUDE.md`, with one line: "Read CLAUDE.md in this folder and follow it." So there's still only one set of rules, and you never have to keep two copies the same.

If your agent doesn't load any rule file by itself, start each chat with: "Read CLAUDE.md first and follow it."

## The "never read" list

`.claudeignore` is a list of files and folders your agent must not open unless you ask for that exact one, like `Memory/finances/`. It isn't a lock. It works because the main rules tell every agent to respect it. So it works the same with any agent that follows the rules.

For things that must stay truly private, don't put them in the brain folder at all.

## Using two agents on one brain

You can. For example, Claude on your computer and another agent on another one. They read the same rules, so they file things the same way. Two tips:

- Don't let both write at the same time. Google Drive may make a second copy of a note, ending in `(1)`. If that happens, ask your agent to merge them.
- Let only one of them run the Brain Keeper's daily tidy.

## Scheduled tasks

The Brain Keeper's daily tidy and the morning brief are scheduled tasks. If your agent's app can schedule tasks, the setup does it for you. If it can't:

- Say **"run the brain keeper"** once a day.
- Say **"morning brief"** when you start your day.

Both do exactly the same thing as the scheduled version.
