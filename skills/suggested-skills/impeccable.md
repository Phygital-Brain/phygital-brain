# Design websites and apps with Impeccable

[Impeccable](https://github.com/pbakaus/impeccable) is an open-source design skill by Paul Bakaus (Apache 2.0). It makes your agent better at designing websites, apps and other screens: it reviews a design, finds problems like weak contrast or messy spacing, and polishes the layout, type, colour and motion. It started from Anthropic's frontend design skill. Impeccable isn't part of Phygital Brain; this is how to use the two together.

## What you need

- An agent that can work on code on your computer, like Claude Code (the Claude desktop app's Code tab, or the terminal), Cursor, Codex or Gemini CLI.
- A website or app to work on, in its own folder.
- Node.js, only if you install with `npx` (below). The skill itself needs nothing else.

## Install it

In Claude Code:

```
claude plugin marketplace add pbakaus/impeccable
```

```
claude plugin install impeccable@impeccable
```

With another agent, follow the [Impeccable install guide](https://github.com/pbakaus/impeccable#readme). Its quick start, `npx impeccable install`, puts the skill inside the folder you run it in, so run it in your website's folder, never in your brain folder. Then, in a chat on your brain folder, say **"Add Impeccable to my brain."**

## Connect it to your brain

Impeccable keeps its own notes about a product (`PRODUCT.md` and `DESIGN.md`) in the website's folder, when you run `/impeccable init` there. Your brain holds the rest: your voice, your colours, and why the site exists.

Your agent writes `Skills/impeccable/notes.md`. A good one looks like this:

```
Before design work, read:
- About/brand.md: voice, colours and fonts
- the project's README.md: who the site is for and what it must do

Where:
- the website's code lives in its own folder, not in the brain
  (write its path in the project's README.md)
- run /impeccable init in that folder once, and give it what
  About/brand.md and the project's README.md say

Save:
- a short summary of each review or polish in the project's notes/ folder

Style:
- calm and clear, nothing flashy
```

## Use it

In a chat on your website's folder, or on your brain folder with the website's path:

- "Review the home page of my portfolio site and tell me what to fix first."
- "Polish the contact page before I publish it."
- "The shop page feels too loud. Make it quieter, in my brand colours."

Your agent reads your brand and the project, runs the right Impeccable command (like `/impeccable critique`, `/impeccable polish` or `/impeccable quieter`), shows you what it changed, and saves a summary in the project. It logs one line in today's daily note.

## Change it yourself

1. Edit the page yourself, or tell your agent what you don't like.
2. Back in the chat: "I changed the header. Check it with Impeccable again."

## Good to know

- Impeccable works on code: a website, an app or a design made in HTML. It doesn't edit images or videos.
- It writes working files, like screenshots, in a `.impeccable/` folder inside the website's folder. Keep them there, out of your brain.
- Problems with Impeccable itself go to [its repository](https://github.com/pbakaus/impeccable), not to Phygital Brain.
