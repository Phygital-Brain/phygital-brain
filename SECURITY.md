# Security policy

Phygital Brain has no program and no server. It's instructions and templates that an AI agent follows to build and look after a folder of notes. So here, "security" means two things: your notes stay private, and your agent keeps following the brain's rules. Reports are welcome.

## What you share with your AI

Phygital Brain is only files and instructions. It doesn't send your notes anywhere by itself. But your agent reads your notes to help you, so **everything it reads goes to the company that runs your AI** (for example Anthropic for Claude, or OpenAI for Codex), and your files are stored by your cloud drive's provider (for example Google for Google Drive, or whoever runs your Nextcloud).

You choose what goes in your brain, and you're responsible for it. Before you start:

- **Check your AI's privacy settings.** Some AI companies may use your chats to train their models, depending on your plan and your settings. Look for a setting about using your data to improve their models, and choose what you're comfortable with.
- **Read their privacy policy** if your work is sensitive: how long they keep your chats, and who can see them.
- **Other people's details are your responsibility too.** Notes about clients, friends or your team hold their names, emails and history. Only keep what you need, and follow the privacy laws where you live and work.
- **Some things should never go in.** Passwords, keys, health records, other people's ID numbers, and anything you've promised to keep secret. `.claudeignore` asks your agent not to read some folders, but that's only a rule your agent follows. It doesn't lock anything.
- **Work for a company?** Check its rules before you put work information in a personal AI or a personal cloud drive.

Phygital-Brain doesn't see, collect or store your notes. It isn't responsible for what you share with your AI provider, your cloud drive's provider or anyone else.

## Supported versions

Only the latest version gets fixes while the project is at 0.x. To get a fix: update the plugin, then say "Upgrade my second brain" in a chat on your brain folder.

| Version | Fixes |
|---|---|
| 0.1.x | Yes |

## Reporting a problem

Please don't open a public issue, discussion or pull request for a security problem.

1. Open [private vulnerability reporting](https://github.com/Phygital-Brain/phygital-brain/security/advisories/new) (the **Security** tab, then **Report a vulnerability**). Only the maintainer sees it.
2. Include what's listed below.

There is no email contact. Use private reporting.

## What to include

- The Phygital Brain version (the first line of your brain's root `CLAUDE.md`, or `CHANGELOG.md`).
- Which agent and app you use (for example Claude desktop app, Claude Code, Codex).
- What you found, and which file it's in if you know: a skill, a template, a form or a doc.
- Steps to reproduce it, using a **test brain** with made-up notes.
- What could go wrong for a real person.

## What not to send

- Your real notes, real names, or anything from `Memory/finances/`.
- Passwords, keys, tokens or private numbers of any kind.

Use a test brain with made-up people and made-up numbers.

## What happens next

We aim to reply within 7 days, and to fix every confirmed problem in the templates or skills. Please keep it private until the fix is out. If you'd like credit, say which name or GitHub account to use. There's no paid bug bounty.

## Scope

In scope:

- A template or skill that copies private details (tax IDs, bank details, card numbers, birth date) into other notes or replies.
- A way for a dropped file, a pasted link or a note to make the agent ignore the brain's rules: for example delete or move notes without asking, read `Memory/finances/`, or send notes somewhere.
- A Brain Keeper step that deletes, moves or rewrites notes, against its hard rules.
- An upgrade that loses a person's notes or their own rules.
- A form that sends answers anywhere other than back to the agent.

Out of scope:

- Problems in your AI app, your cloud drive, Baalda or your computer. Please report those to their makers.
- `.claudeignore` not stopping a determined agent. The agent follows it as a rule, and it doesn't lock anything. Truly private things shouldn't be in the brain folder.
- An AI model that doesn't follow its instructions in general, without a way to make it happen.
- Reports from automated scanners without a real problem.

## Testing in good faith

If you research in good faith and follow this policy, we won't take action against you. Test only with your own test brain. Never use other people's notes.
