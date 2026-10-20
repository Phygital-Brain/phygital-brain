# Install

Pick your agent and click. Then open a chat on your brain folder and say **"Set up my second brain."**

Every way gives your agent the same setup, forms, 41 languages and Brain Keeper. Your agent writes your notes itself, in the folder you choose.

<p align="center">
<a href="https://github.com/Phygital-Brain/phygital-brain/releases/latest/download/phygital-brain.mcpb"><img src="images/buttons/claude-desktop.png" width="240" alt="Add to Claude desktop"></a>
<a href="#claude-code"><img src="images/buttons/claude-code.png" width="240" alt="Install in Claude Code"></a>
<a href="https://cursor.com/en/install-mcp?name=phygital-brain&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsInBoeWdpdGFsLWJyYWluIl19"><img src="images/buttons/cursor.png" width="240" alt="Add to Cursor"></a>
<br>
<a href="https://insiders.vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522phygital-brain%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522-y%2522%252C%2522phygital-brain%2522%255D%257D"><img src="images/buttons/vscode.png" width="240" alt="Add to VS Code"></a>
<a href="#codex"><img src="images/buttons/codex.png" width="240" alt="Set up in Codex"></a>
<a href="#hermes-agent-and-openclaw"><img src="images/buttons/other-agents.png" width="240" alt="Set up in Hermes Agent or OpenClaw"></a>
</p>

```mermaid
flowchart LR
    C[Click the button<br>for your agent] --> A[Your agent installs<br>Phygital Brain]
    A --> F[Open a chat on your<br>brain folder]
    F --> S["Say: Set up my<br>second brain"]
```

## What you need

- **Claude desktop, or the plugin in Claude Code:** nothing more.
- **Every other way:** [Node.js](https://nodejs.org) on your computer. Download the version marked LTS and install it like any app. You only do this once.
- **Only a phone, no computer:** nothing to install. Follow [Phone only](phone-only.md). The setup is quicker and easier on a computer, but your phone can do it too (tested with Claude).

**On this page:** [Claude desktop](#claude-desktop) · [Claude Code](#claude-code) · [Cursor](#cursor) · [VS Code](#vs-code) · [Codex](#codex) · [Hermes Agent and OpenClaw](#hermes-agent-and-openclaw) · [Any other agent](#any-other-agent) · [Terminal, any agent](#terminal-any-agent) · [What the connector does](#what-the-connector-does) · [Updating](#updating) · [Removing](#removing)

## Claude desktop

1. Click **Add to Claude desktop** above. It downloads `phygital-brain.mcpb`.
2. Double-click the file. The Claude app opens and asks to install **Phygital Brain**. Click **Install**.
3. In a chat on your brain folder, say "Set up my second brain."

Nothing else to install. If double-clicking doesn't open Claude, open Claude's settings, go to **Extensions**, and drag the file in.

## Claude Code

The plugin is the best fit here: the skills load directly.

```
/plugin marketplace add Phygital-Brain/phygital-brain
```

```
/plugin install phygital-brain@phygital-brain
```

Or, as a connector, in a terminal:

```bash
claude mcp add phygital-brain -- npx -y phygital-brain
```

## Cursor

Click **Add to Cursor** above. Cursor opens and asks to install the **phygital-brain** server. Click **Install**.

By hand: add this to Cursor's `mcp.json`.

```json
{
  "mcpServers": {
    "phygital-brain": {
      "command": "npx",
      "args": ["-y", "phygital-brain"]
    }
  }
}
```

## VS Code

Click **Add to VS Code** above. VS Code opens and asks to install the **phygital-brain** server. Click **Install**. It works with the agent mode of VS Code's chat.

By hand: run **MCP: Add Server** from the Command Palette, choose **Command (stdio)**, and enter `npx -y phygital-brain`.

## Codex

In a terminal:

```bash
codex mcp add phygital-brain -- npx -y phygital-brain
```

Or add this to Codex's config file, `~/.codex/config.toml`:

```toml
[mcp_servers.phygital-brain]
command = "npx"
args = ["-y", "phygital-brain"]
```

Restart Codex, open it on your brain folder, and say "Set up my second brain."

## Hermes Agent and OpenClaw

Both can use MCP servers. Add Phygital Brain as a **stdio** server in their MCP settings, with:

- **Command:** `npx`
- **Arguments:** `-y phygital-brain`

The settings file and its format are in each agent's own docs. Point the agent at your brain folder, and say "Set up my second brain." If it doesn't read `CLAUDE.md` by itself, start each chat with "Read CLAUDE.md first." See [Other agents](other-agents.md).

## Any other agent

Any agent that takes MCP servers works the same way: a stdio server with the command `npx -y phygital-brain`. Many use this format:

```json
{
  "mcpServers": {
    "phygital-brain": {
      "command": "npx",
      "args": ["-y", "phygital-brain"]
    }
  }
}
```

No MCP? Download this repository, open your agent on your brain folder, and say: "Set up my second brain. Follow skills/brain-setup/SKILL.md in {where you put it}."

## Terminal, any agent

For agents that use skills, like Claude Code, Codex, Cursor and Gemini CLI, one line in a terminal adds Phygital Brain to the ones you pick:

```bash
npx skills add Phygital-Brain/phygital-brain
```

It uses the [skills](https://github.com/vercel-labs/skills) installer, which asks which agents to add it to.

## What the connector does

Most buttons above add a connector: a small program (an MCP server) that runs on your computer and hands your agent Phygital Brain's files. It only reads its own files. It never opens your notes, and it sends nothing anywhere. In Claude Code, the plugin does the same job by loading the skills straight into the agent.

## Updating

- **Connector (Cursor, VS Code, Codex, Hermes Agent, OpenClaw):** nothing to do. It gets the newest version by itself when your agent starts.
- **Terminal line:** `npx skills update`.
- **Claude desktop file:** download the new `phygital-brain.mcpb` from the latest release and install it over the old one.
- **Claude Code plugin:** `/plugin marketplace update phygital-brain`.

Then say "Upgrade my second brain" in a chat on your brain folder.

## Removing

Remove Phygital Brain in your agent's plugin, extension or MCP settings. Your brain folder stays as it is: it's plain files in your own cloud drive.
