# Get press coverage with Public Relations

[Public Relations](https://github.com/coreyhaines31/marketingskills/tree/main/skills/public-relations) is a skill from the open-source Marketing Skills library by Corey Haines (MIT). It helps you get written about: finding the story angle, pitching journalists, writing a press release, answering reporter requests, preparing for a podcast, and responding when something goes wrong. Public Relations isn't part of Phygital Brain; this is how to use the two together.

## What you need

- An agent that can run commands on your computer, like Claude Code (the Claude desktop app's Code tab, or the terminal), Codex, Cursor or Gemini CLI.
- **Node.js** for the install command. Your agent can help install it.
- Something worth telling: a launch, a project, a result or an opinion.

## Install it

```
npx skills add coreyhaines31/marketingskills --skill public-relations
```

This installs only this skill, not the whole library. More options are in the [Marketing Skills install guide](https://github.com/coreyhaines31/marketingskills#installation). Then, in a chat on your brain folder, say **"Add Public Relations to my brain."**

## Connect it to your brain

Your agent writes `Skills/public-relations/notes.md`. A good one looks like this:

```
Before writing a pitch, read:
- About/business.md and About/brand.md: what I do and how I sound
- the project's README.md, if the pitch is for a project
- the journalist's page in Relationships/, if I've dealt with them before

Save:
- pitches and press releases in Projects/{project}/press/,
  named {outlet}-{date}.md
- new journalists as a note in Relationships/, with the date and what I pitched

Style:
- short, specific, no hype
- never send anything. Show me the draft first
```

## Get coverage

In a chat on your brain folder:

- "Find three story angles in my new project and tell me which one is strongest."
- "Write a pitch to this journalist about my launch."
- "Prepare me for a podcast interview next week."
- "Someone posted something false about me. Draft a calm holding statement."

Your agent reads your work and your past press notes, drafts in your voice, and saves the draft in the project. It logs one line in today's daily note.

## Change it yourself

1. Open the saved pitch and rewrite any line in your own words.
2. Back in the chat: "Use my version as the model for the next pitches."

## Good to know

- Your agent drafts. You send. It never emails a journalist without your yes.
- Press contacts are people: keep them in `Relationships/`, not in the skill.
- Problems with Public Relations itself go to [its repository](https://github.com/coreyhaines31/marketingskills), not to Phygital Brain.
