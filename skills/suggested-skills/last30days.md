# Research what people say with last30days

[last30days](https://github.com/mvanhorn/last30days-skill) is an open-source research skill by Matt Van Horn (MIT). Ask it about any topic and it reads what real people posted in the last 30 days on Reddit, Hacker News, YouTube, X, GitHub and other places, ranks it by upvotes and likes, and writes a short report with links to every source. last30days isn't part of Phygital Brain; this is how to use the two together.

## What you need

- An agent that can run commands on your computer, like Claude Code (the Claude desktop app's Code tab, or the terminal), Codex, Cursor or Gemini CLI.
- **Python 3.12 or newer.** Most Macs and Linux computers have it. Your agent can help install it.
- Nothing else to start: Reddit, Hacker News, Polymarket and GitHub work with no account. More places (X, YouTube, TikTok, Instagram) need free tools or keys, and its first-run setup walks you through them.

## Install it

In Claude Code:

```
claude plugin marketplace add mvanhorn/last30days-skill
```

```
claude plugin install last30days@last30days-skill
```

With another agent:

```
npx skills add mvanhorn/last30days-skill -g
```

More options, like the Claude desktop app, are in the [last30days install guide](https://github.com/mvanhorn/last30days-skill#install). Then, in a chat on your brain folder, say **"Add last30days to my brain."**

## Connect it to your brain

Your agent writes `Skills/last30days/notes.md`. A good one looks like this:

```
Before research, read:
- About/business.md and About/customers.md: what I do and who for
- the project's README.md, if the research is for a project

Save:
- the report in Projects/{project}/research/ when it's for a project,
  or in Memory/research/ when it isn't, named {topic}-{date}.md
- only the summary and the links, not the raw dump
  (last30days keeps its own raw files in Documents/Last30Days/)

Style:
- start with the three things that matter most for my work
```

## Research a topic

In a chat on your brain folder:

- "What are people saying about picture book prices this month?"
- "Research what my customers complain about with online photo printing."
- "What's new this month in AI tools for illustrators? Save it in the research folder."

Your agent reads what your work is about, runs last30days, and saves the report with its links in the right folder. It logs one line in today's daily note.

## Change it yourself

1. Open the saved report and add your own thoughts under it.
2. Back in the chat: "Run that research again next month and tell me what changed."

## Good to know

- API keys and tokens for extra sources go in last30days' own settings, never in a note in your brain.
- For X, it can use your browser's sign-in. Only allow that if you're comfortable with it.
- It reads public posts. Check anything important before you act on it.
- Problems with last30days itself go to [its repository](https://github.com/mvanhorn/last30days-skill), not to Phygital Brain.
