# Draw diagrams in your brand with Diagram Design

[Diagram Design](https://github.com/cathrynlavery/diagram-design) is an open-source diagram skill by Cathryn Lavery (MIT). Describe what you want and your agent draws a clean diagram in your colours and fonts: a flowchart, a timeline, a process, an org chart, a customer journey, a funnel, a Venn and many more. Each one is a single HTML file you can open in any browser, and you can export it as a PNG or SVG for slides and posts. Diagram Design isn't part of Phygital Brain; this is how to use the two together.

## What you need

- An agent that can work with files on your computer, like Claude Code (the Claude desktop app's Code tab, or the terminal), Codex or Cursor.
- **Node.js**, only if you install with `npx` (below).
- For PNG export, a browser your agent can run, like Chrome. The diagrams themselves need nothing.

## Install it

In Claude Code:

```
claude plugin marketplace add cathrynlavery/diagram-design
```

```
claude plugin install diagram-design@diagram-design
```

With another agent:

```
npx skills add cathrynlavery/diagram-design
```

More options are in the [Diagram Design install guide](https://github.com/cathrynlavery/diagram-design#install). Then, in a chat on your brain folder, say **"Add Diagram Design to my brain."**

## Connect it to your brain

Diagrams come out in black and tangerine until you give the skill your brand. If you have a website, say "Onboard Diagram Design to my website", with its address: it takes your colours and fonts from the site and keeps them for every diagram. If you don't, your agent gives it the colours and fonts from `About/brand.md`.

Your agent writes `Skills/diagram-design/notes.md`. A good one looks like this:

```
Before a diagram, read:
- About/brand.md: colours and fonts
- the project's README.md, if the diagram is for a project

Save:
- the diagram in Projects/{project}/diagrams/ when it's for a project,
  or in Memory/diagrams/ when it isn't, named {topic}-{date}.html
- the PNG next to it, when I ask for one

Style:
- few words on each box, in my language
```

## Use it

In a chat on your brain folder:

- "Draw how a client order moves through my studio, from first email to delivery."
- "Make a timeline of the shop launch for the project, and export it as a PNG."
- "Turn the steps in my onboarding note into a simple flowchart."

Your agent reads your brand and the project, picks the right kind of diagram, draws it, and saves it in the right folder. It logs one line in today's daily note.

## Change it yourself

1. Open the HTML file in your browser and look at it.
2. Back in the chat: "Make the boxes bigger and change the third step to Review."

## Good to know

- The diagrams load their fonts from Google Fonts when you open them, so they look right online. Nothing about your diagram is sent.
- It can also redraw a diagram you already have from draw.io, Mermaid or Excalidraw, in your brand.
- Problems with Diagram Design itself go to [its repository](https://github.com/cathrynlavery/diagram-design), not to Phygital Brain.
