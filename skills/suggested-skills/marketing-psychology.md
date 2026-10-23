# Understand why people buy with Marketing Psychology

[Marketing Psychology](https://github.com/coreyhaines31/marketingskills/tree/main/skills/marketing-psychology) is a skill from the open-source Marketing Skills library by Corey Haines (MIT). It gives your agent a set of mental models from behavioural science, like social proof, anchoring and loss aversion, and uses them to explain how people decide and to improve your copy, pricing and offers. Marketing Psychology isn't part of Phygital Brain; this is how to use the two together.

## What you need

- An agent that can run commands on your computer, like Claude Code (the Claude desktop app's Code tab, or the terminal), Codex, Cursor or Gemini CLI.
- **Node.js** for the install command. Your agent can help install it.

## Install it

```
npx skills add coreyhaines31/marketingskills --skill marketing-psychology
```

This installs only this skill, not the whole library. More options are in the [Marketing Skills install guide](https://github.com/coreyhaines31/marketingskills#installation). Then, in a chat on your brain folder, say **"Add Marketing Psychology to my brain."**

## Connect it to your brain

Your agent writes `Skills/marketing-psychology/notes.md`. A good one looks like this:

```
Before advice, read:
- About/customers.md: who I sell to and what holds them back
- About/business.md and About/brand.md: what I sell and how I sound
- the project's README.md, if the question is about a project

Save:
- useful findings in Projects/{project}/research/,
  named psychology-{topic}-{date}.md

Style:
- name the principle in plain words, then show the exact change to my text
- never pressure or trick my customers
```

## Use it

In a chat on your brain folder:

- "Why might people hesitate on my pricing page, and what would help?"
- "Which of my three offers should I show first, and why?"
- "Rewrite this product description using what you know about how my customers decide."

Your agent reads who your customers are, picks the few ideas that fit, and shows the change. It logs one line in today's daily note.

## Change it yourself

1. Open the saved note and cross out any idea that doesn't suit your brand.
2. Back in the chat: "Never use scarcity or countdown tricks in my writing."

## Good to know

- These ideas are strong. Use them to help people choose, not to push them.
- Problems with Marketing Psychology itself go to [its repository](https://github.com/coreyhaines31/marketingskills), not to Phygital Brain.
