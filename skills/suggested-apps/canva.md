# Make designs with Canva

[Canva](https://www.canva.com) is a design app for posts, flyers, covers, presentations and more. Its **AI Connector** lets your agent work in your Canva account: find your designs, make new ones, edit them, resize them for each platform and export them. With your brain, the designs use your brand and what your projects say. It works with a free Canva account. Canva isn't part of Phygital Brain; this is how to use the two together.

## What you need

- A Canva account. The free plan works. Brand Templates and Autofill need a paid Canva plan, and some AI actions use your monthly Canva AI credits.
- An agent that takes connectors or MCP servers, like the Claude app (web, desktop or phone), Claude Code, ChatGPT or Gemini.
- On a Canva team, your admin may need to allow the AI Connector.

## Check first

If Canva already shows up as a connector in this chat, it's connected: skip to the last line below and say "Add Canva to my brain."

## Install it

In the Claude app:

1. Open **Settings**, then **Connectors**.
2. Find **Canva**, select it, and sign in to your Canva account.
3. In a new chat, check Canva is turned on in the chat's connector settings.

In Claude Code:

```
claude mcp add --transport http canva https://mcp.canva.com/mcp
```

The first time you use it, you sign in to Canva. Other agents: follow [Canva's setup guide](https://www.canva.com/help/mcp-agent-setup/). Then, in a chat on your brain folder, say **"Add Canva to my brain."**

## Comes with: Canvas Design

When someone picks Canva, your agent also sets up [Canvas Design](https://github.com/anthropics/skills/tree/main/skills/canvas-design), a skill by Anthropic (Apache 2.0). It draws a design itself and saves it as a PNG or PDF, with no account. Use Canva for designs you want to keep editing, and Canvas Design for a quick poster or visual when Canva's credits run out or you don't need to edit it later.

- **In the Claude app** (paid plans): it's already there.
- **In Claude Code:** it comes with Anthropic's example skills, the same install as Skill Creator:

```
claude plugin marketplace add anthropics/skills
```

```
claude plugin install example-skills@anthropic-agent-skills
```

## Connect it to your brain

Your agent writes `Skills/canva/notes.md`, for both Canva and Canvas Design. A good one looks like this:

```
Before a design, read:
- About/brand.md: colours, fonts and the look I like
- the project's README.md: what the design is for and where it's used

Save:
- the design stays in Canva; put its link in the project's README.md
- exported files in Projects/{project}/assets/, named {what}-{size}
  (like cover-1080x1350.png)
- Canvas Design files in the same folder, named the same way

Style:
- calm and clear, my brand colours, no stock-photo look
```

## Make a design

In a chat on your brain folder:

- "Make an Instagram post for the picture book launch, in my brand."
- "Resize the picture book cover for Instagram, Pinterest and my website."
- "Turn my notes on the shoot into a 5-slide presentation in Canva."

Your agent reads your brand and the project, makes the design in your Canva account, shows you a preview, and saves the link (and any export) in the project. It logs one line in today's daily note.

## Change it yourself

1. Open the design in **Canva**, on your computer or phone, and change what you like.
2. Back in the chat: "I changed the cover in Canva. Export it again for Instagram."

## Good to know

- Your designs live in your Canva account. Your brain keeps the links and the exported files.
- Big image files make your cloud drive slow to sync. Export only what you need.
- Images, fonts and music you use need the right licences. Canva's own licence covers what's in its library.
- Problems with Canvas Design go to [its repository](https://github.com/anthropics/skills).
- Problems with Canva itself go to [Canva's help center](https://www.canva.com/help/), not to Phygital Brain.
