# Make your own skills with Skill Creator

[Skill Creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) is a skill by Anthropic (Apache 2.0) that helps you make your own skills. Tell it about something you do often, like writing a client update or planning a post, and it turns that into a skill your agent follows every time. It can also test a skill and make it better. With your brain, the new skill can use what your notes already know about how you work. Skill Creator isn't part of Phygital Brain; this is how to use the two together.

## What you need

- **In the Claude app** (web, desktop or phone, on a paid plan): nothing. It's already there.
- **In Claude Code:** a computer. Testing a skill uses Python, and your agent can help install it.

## Install it

In the Claude app, skip this step.

In Claude Code:

```
claude plugin marketplace add anthropics/skills
```

```
claude plugin install example-skills@anthropic-agent-skills
```

This adds Skill Creator together with Anthropic's other example skills. Then, in a chat on your brain folder, say **"Add Skill Creator to my brain."**

## Connect it to your brain

Your agent writes `Skills/skill-creator/notes.md`. A good one looks like this:

```
Before making a skill, read:
- About/me.md and About/brand.md: how I work and how I write
- the notes the skill is about (for example the client page or the project)

Save:
- each new skill in Skills/{skill-name}/, with its SKILL.md,
  and a row for it in Skills/CLAUDE.md
- never put passwords, keys or private details in a skill

Style:
- short steps, plain words, ask me before anything is sent or deleted
```

## Make a skill

In a chat on your brain folder:

- "Make a skill for my weekly client update, from how I wrote the last three."
- "Turn the way I plan a photo shoot into a skill."
- "Test my client update skill and make it better."

Your agent asks a few questions, writes the skill in your brain, tries it with you, and adds it to the list. It logs one line in today's daily note.

## Change it yourself

1. Open the skill's `SKILL.md` and change any step in plain words.
2. Back in the chat: "I changed my client update skill. Check it still works."

## Good to know

- A skill you make is yours, so you can edit its `SKILL.md`. Skills from other people stay unedited, and you change them with `notes.md`.
- Problems with Skill Creator itself go to [its repository](https://github.com/anthropics/skills), not to Phygital Brain.
