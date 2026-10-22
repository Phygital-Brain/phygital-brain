# Make documents with the document skills

The [document skills](https://github.com/anthropics/skills) by Anthropic let your agent make and edit Word documents, PowerPoint decks, Excel spreadsheets and PDFs. With your brain, that means proposals, decks, price lists and invoices made from what your notes already say. They're source-available, not open source: you can use them under your agreement with Anthropic. They aren't part of Phygital Brain; this is how to use the two together.

## What you need

- **In the Claude app** (web, desktop or phone, on a paid plan): nothing. They're already there.
- **In Claude Code:** a computer, plus Python and Node.js. Some jobs use extra tools, like LibreOffice for spreadsheets. Your agent can help install them.

## Install it

In the Claude app, skip this step.

In Claude Code:

```
claude plugin marketplace add anthropics/skills
```

```
claude plugin install document-skills@anthropic-agent-skills
```

Then, in a chat on your brain folder, say **"Add the document skills to my brain."**

## Connect it to your brain

Your agent writes `Skills/document-skills/notes.md`. A good one looks like this:

```
Before a document, read:
- About/brand.md: voice, colours and fonts
- About/services.md: what I sell and my prices, for proposals and quotes
- the project's README.md, or the client's page in Relationships/Clients/

Save:
- each document in Projects/{project}/assets/, named {what}-{date}
  (like proposal-2026-10-22.docx)
- never put bank details or tax numbers in a document unless I ask

Style:
- short and plain, my brand colours, one idea per slide
```

## Make a document

In a chat on your brain folder:

- "Make a one-page proposal for the picture book client, as a Word document."
- "Turn my notes on the shoot into a 6-slide deck."
- "Make a spreadsheet of this month's invoices from my notes."

Your agent reads your brand and the project, makes the file, and saves it in the project. It logs one line in today's daily note.

## Change it yourself

1. Open the file in Word, PowerPoint, Excel or any app that opens them, and change what you like.
2. Back in the chat: "I changed the proposal. Read it and make the deck match."

## Good to know

- Big files make your cloud drive slow to sync. Keep large decks outside the brain folder when you can, and link to them.
- Problems with the document skills go to [their repository](https://github.com/anthropics/skills), not to Phygital Brain.
