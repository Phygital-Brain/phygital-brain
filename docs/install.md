# Install

Pick your agent and click. Every way gives your agent the same thing: Phygital Brain's setup, forms, templates, 11 languages, the Brain Keeper and the add-language skill. Your agent still writes your notes itself, in the folder you choose.

<p align="center">
<a href="https://github.com/Phygital-Brain/phygital-brain/releases/latest/download/phygital-brain.mcpb"><img src="https://img.shields.io/badge/Add%20to-Claude%20desktop-F05AB8?logo=anthropic&logoColor=white&labelColor=0B0D12&style=for-the-badge" alt="Add to Claude desktop"></a>
<a href="#claude-code"><img src="https://img.shields.io/badge/Install%20in-Claude%20Code-5AC8FA?logo=anthropic&logoColor=white&labelColor=0B0D12&style=for-the-badge" alt="Install in Claude Code"></a>
<a href="https://cursor.com/en/install-mcp?name=phygital-brain&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImdpdGh1YjpQaHlnaXRhbC1CcmFpbi9waHlnaXRhbC1icmFpbiJdfQ=="><img src="https://img.shields.io/badge/Add%20to-Cursor-F05AB8?logo=cursor&logoColor=white&labelColor=0B0D12&style=for-the-badge" alt="Add to Cursor"></a>
<a href="https://insiders.vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522phygital-brain%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522-y%2522%252C%2522github%253APhygital-Brain%252Fphygital-brain%2522%255D%257D"><img src="https://img.shields.io/badge/Add%20to-VS%20Code-F05AB8?labelColor=0B0D12&style=for-the-badge" alt="Add to VS Code"></a>
<a href="#codex"><img src="https://img.shields.io/badge/Other%20agents-Codex%20%C2%B7%20Hermes%20%C2%B7%20OpenClaw-5AC8FA?labelColor=0B0D12&style=for-the-badge" alt="Other agents: Codex, Hermes Agent, OpenClaw"></a>
</p>

Then open a chat on your brain folder and say **"Set up my second brain."**

```mermaid
flowchart LR
    C[Click the button<br>for your agent] --> A[Your agent installs<br>Phygital Brain]
    A --> F[Open a chat on your<br>brain folder]
    F --> S["Say: Set up my<br>second brain"]
```

**On this page:** [Claude desktop](#claude-desktop) · [Claude Code](#claude-code) · [Cursor](#cursor) · [VS Code](#vs-code) · [Codex](#codex) · [Hermes Agent and OpenClaw](#hermes-agent-and-openclaw) · [Any other agent](#any-other-agent) · [Updating](#updating) · [Removing](#removing)

## Two ways it installs

| Way | What it is | Used for |
|---|---|---|
| **Plugin** | Phygital Brain's skills, loaded straight into the agent | Claude Code (recommended there) |
| **Connector** | A small program, an MCP server, that runs on your computer and hands your agent Phygital Brain's files | Claude desktop, Cursor, VS Code, Codex, Hermes Agent, OpenClaw and other agents that take MCP servers |

The connector only reads its own files. It never opens your notes, and it sends nothing anywhere. It runs with `npx -y github:Phygital-Brain/phygital-brain`, straight from this repository, so it needs **Node.js 18 or newer** on your computer. The Claude desktop file is the exception: the Claude app brings its own Node.js.

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
claude mcp add phygital-brain -- npx -y github:Phygital-Brain/phygital-brain
```

## Cursor

Click **Add to Cursor** above. Cursor opens and asks to install the **phygital-brain** server. Click **Install**.

By hand: add this to Cursor's `mcp.json`.

```json
{
  "mcpServers": {
    "phygital-brain": {
      "command": "npx",
      "args": ["-y", "github:Phygital-Brain/phygital-brain"]
    }
  }
}
```

## VS Code

Click **Add to VS Code** above. VS Code opens and asks to install the **phygital-brain** server. Click **Install**. It works with the agent mode of VS Code's chat.

By hand: run **MCP: Add Server** from the Command Palette, choose **Command (stdio)**, and enter `npx -y github:Phygital-Brain/phygital-brain`.

## Codex

Add this to Codex's config file, `~/.codex/config.toml`:

```toml
[mcp_servers.phygital-brain]
command = "npx"
args = ["-y", "github:Phygital-Brain/phygital-brain"]
```

Restart Codex, open it on your brain folder, and say "Set up my second brain."

## Hermes Agent and OpenClaw

Both can use MCP servers. Add Phygital Brain as a **stdio** server in their MCP settings, with:

- **Command:** `npx`
- **Arguments:** `-y github:Phygital-Brain/phygital-brain`

The settings file and its format are in each agent's own docs. Point the agent at your brain folder, and say "Set up my second brain." If it doesn't read `CLAUDE.md` by itself, start each chat with "Read CLAUDE.md first." See [Other agents](other-agents.md).

## Any other agent

Any agent that takes MCP servers works the same way: a stdio server with the command `npx -y github:Phygital-Brain/phygital-brain`. Many use this format:

```json
{
  "mcpServers": {
    "phygital-brain": {
      "command": "npx",
      "args": ["-y", "github:Phygital-Brain/phygital-brain"]
    }
  }
}
```

No MCP? Download this repository, open your agent on your brain folder, and say: "Set up my second brain. Follow skills/brain-setup/SKILL.md in {where you put it}."

## Updating

- **Connector with npx:** it runs the newest version from GitHub each time it starts.
- **Claude desktop file:** download the new `phygital-brain.mcpb` from the latest release and install it over the old one.
- **Claude Code plugin:** `/plugin marketplace update phygital-brain`.

Then say "Upgrade my second brain" in a chat on your brain folder.

## Removing

Remove Phygital Brain in your agent's plugin, extension or MCP settings. Your brain folder stays as it is: it's plain files in your own cloud drive.
