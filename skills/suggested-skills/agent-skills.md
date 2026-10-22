# Build software with Agent Skills

[Agent Skills](https://github.com/addyosmani/agent-skills) is an open-source set of 25 skills by Addy Osmani (MIT) that make your agent work like a careful senior engineer. It follows the same steps every time: write down what to build, plan it in small tasks, build one piece at a time, test it, review it and ship it. Each step has its own command, like `/spec`, `/plan`, `/build`, `/test`, `/review` and `/ship`. Agent Skills isn't part of Phygital Brain; this is how to use the two together.

## What you need

- An agent that works on code on your computer, like Claude Code (the Claude desktop app's Code tab, or the terminal), Cursor, Codex, Gemini CLI or GitHub Copilot.
- A software project to work on, in its own folder.
- Node.js, only if you install with `npx` (below).

## Install it

In Claude Code:

```
claude plugin marketplace add addyosmani/agent-skills
```

```
claude plugin install agent-skills@addy-agent-skills
```

With another agent:

```
npx skills add addyosmani/agent-skills
```

Steps for each agent are in the [Agent Skills guide](https://github.com/addyosmani/agent-skills#quick-start). Then, in a chat on your brain folder, say **"Add Agent Skills to my brain."**

## Connect it to your brain

Agent Skills writes its specs, plans and tests in the project's own code folder. Your brain keeps why you're building it and what you decided.

Your agent writes `Skills/agent-skills/notes.md`. A good one looks like this:

```
Before a spec or plan, read:
- About/goals.md and About/customers.md: why I build things and for whom
- the project's README.md in the brain: what it must do

Where:
- the code, the spec and the plan live in the project's code folder,
  not in the brain (write its path in the project's README.md)

Save:
- big decisions (a tool, a design, something dropped) as a short note
  in Memory/decisions/, with a link from the project's README.md

Style:
- small steps, explain each change in plain words
```

## Use it

In a chat on your project's code folder:

- "/spec a booking page for my studio site."
- "/plan it, then /build the first task."
- "/review what we built today before I publish it."

Your agent reads your goals and the project from your brain, follows the steps, and saves the decisions in your brain. It logs one line in today's daily note.

## Change it yourself

1. Read the spec or the plan in the code folder and change anything you disagree with.
2. Back in the chat: "I changed the plan. Build from the new version."

## Good to know

- It's made for writing software. For notes, posts or designs, the other suggested skills fit better.
- In Claude Code, some commands share a name with built-in ones, like `/review`. Use `/agent-skills:review` for this one.
- Problems with Agent Skills itself go to [its repository](https://github.com/addyosmani/agent-skills), not to Phygital Brain.
