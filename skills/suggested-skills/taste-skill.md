# Build websites that look designed with Taste Skill

[Taste Skill](https://github.com/Leonxlnx/taste-skill) is an open-source design skill by Leonxlnx (MIT). It helps your agent build web pages that don't look like every other AI-made site. It picks a clear direction from a study of 247 award-winning websites (the idea, the layout, the type, the colours and the pictures), follows strict style rules, then opens the page in a real browser, looks at it and fixes what's off. It works on landing pages, portfolios, shop pages and app screens like dashboards. Taste Skill isn't part of Phygital Brain; this is how to use the two together.

## What you need

- An agent that can work on code on your computer, like Claude Code (the Claude desktop app's Code tab, or the terminal), Codex or Cursor.
- **Node.js 22 or newer**, and Chrome, Edge or Chromium installed. Your agent can help install them.
- A website to build or change, in its own folder.
- No accounts or API keys. It goes online only to find free pictures.

## Install it

In Claude Code:

```
claude plugin marketplace add Leonxlnx/taste-skill
```

```
claude plugin install taste-skill@taste-skill
```

With another agent:

```
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

More options are in the [Taste Skill install guide](https://github.com/Leonxlnx/taste-skill#install). Then, in a chat on your brain folder, say **"Add Taste Skill to my brain."**

## Connect it to your brain

Your agent writes `Skills/taste-skill/notes.md`. A good one looks like this:

```
Before design work, read:
- About/brand.md: voice, colours and fonts
- About/business.md: what I sell and who it's for
- the project's README.md: what the page must do

Where:
- the website's code lives in its own folder, not in the brain
  (write its path in the project's README.md)

Save:
- a short summary of the direction it chose, and why,
  in the project's notes/ folder

Style:
- my brand colours win over the direction's colours
```

## Use it

In a chat on your website's folder, or on your brain folder with the website's path:

- "Build a one-page site for my ceramics studio, in my brand."
- "My portfolio home page looks generic. Give it a real direction."
- "Design the dashboard screen for the client project."

Your agent reads your brand and the project, picks a direction, builds the page, checks it in the browser and fixes what it sees. It saves a short summary in the project and logs one line in today's daily note.

## Change it yourself

1. Open the page in your browser and note what you don't like.
2. Back in the chat: "The hero is too dark. Try the second direction instead."

## Good to know

- A full page build takes a while, about 30 to 45 minutes, and uses a lot of your plan's usage. Start with one page.
- It works on code: websites and app screens. It doesn't edit images or videos.
- Pictures it finds come from free libraries, with their credit. Check the credit before you publish.
- For reviewing and polishing a site you already have, see [Impeccable](impeccable.md). The two work well together.
- Problems with Taste Skill itself go to [its repository](https://github.com/Leonxlnx/taste-skill), not to Phygital Brain.
