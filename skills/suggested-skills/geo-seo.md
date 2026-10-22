# Get found in AI search with GEO-SEO

[GEO-SEO](https://github.com/zubair-trabzada/geo-seo-claude) is an open-source skill by Zubair Trabzada (MIT). It checks how easy a website is to find and quote in AI search (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews) and in normal search. It gives the site a score from 0 to 100 and a list of fixes, starting with the quick wins. It can also write a report you can send to a client. GEO-SEO isn't part of Phygital Brain; this is how to use the two together.

## What you need

- **Claude Code** (the Claude desktop app's Code tab, or the terminal). This skill is made for Claude Code only.
- **Python 3.10 or newer** and **Git**. On Windows, also Git for Windows, which comes with Git Bash. Your agent can help install them.
- A website to check. It can be yours or a client's.

## Install it

Download it and run its installer (Mac or Linux):

```
git clone https://github.com/zubair-trabzada/geo-seo-claude.git
```

```
cd geo-seo-claude && ./install.sh
```

On Windows, run the same two lines in **Git Bash** (not PowerShell), with `./install-win.sh` in place of `./install.sh`. The installer puts the skill in `~/.claude/skills/` and its Python tools in a separate folder there, so the rest of your computer isn't touched. The [GEO-SEO page](https://github.com/zubair-trabzada/geo-seo-claude#quick-start) also has a one-line install. Then, in a chat on your brain folder, say **"Add GEO-SEO to my brain."**

## Connect it to your brain

Your agent writes `Skills/geo-seo/notes.md`. A good one looks like this:

```
Before an audit, read:
- About/business.md and About/services.md: what I do and what I sell
- About/brand.md: my voice, for any text it suggests
- the client's page in Relationships/Clients/, if it's for a client

Save:
- the audit summary and the fix list in Projects/{project}/research/,
  named geo-audit-{date}.md
- client reports in the client's project, never in About/

Style:
- quick wins first, in plain words I can send to a client
```

## Check a website

In a chat on your brain folder:

- "Run a GEO audit on my portfolio site and tell me the three fixes that matter most."
- "Quick check: can ChatGPT and Perplexity read my client's website?"
- "Make a client report from last month's audit and compare it with today."

Your agent reads your business and the project, runs the right command (like `/geo audit` or `/geo quick`), and saves the summary in the project. It logs one line in today's daily note.

## Change it yourself

1. Open the saved audit and mark the fixes you've done.
2. Back in the chat: "I fixed the first three. Check the site again and tell me what changed."

## Good to know

- Its client tools (`/geo prospect`, `/geo proposal`) keep their own list of clients and proposals in a `.geo-prospects` folder in your home folder, outside your brain. Your brain stays the place for what you know about each client.
- It only reads public web pages. Changing the website is up to you or your agent, in the website's own folder.
- Problems with GEO-SEO itself go to [its repository](https://github.com/zubair-trabzada/geo-seo-claude), not to Phygital Brain.
