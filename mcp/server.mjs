#!/usr/bin/env node
// Phygital Brain connector: a small MCP server (stdio, no dependencies).
//
// It hands an agent Phygital Brain's skills and files: the setup, the forms, the templates,
// the translated language sets, the Brain Keeper and the add-language skill. It reads only
// this package's own skills/ folder and never touches the person's files: the agent writes
// the brain with its own file tools, in the folder the person chose.
//
// Run it with: npx -y phygital-brain

import { readFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { dirname, join, normalize, relative, sep } from "node:path";
import { fileURLToPath } from "node:url";
import { createInterface } from "node:readline";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = join(HERE, "..");
const SKILLS = join(ROOT, "skills");
const VERSION = JSON.parse(readFileSync(join(ROOT, ".claude-plugin", "plugin.json"), "utf8")).version;
const PROTOCOL_VERSIONS = ["2025-06-18", "2025-03-26", "2024-11-05"];

const JOBS = {
  setup: "brain-setup",
  "brain-keeper": "brain-keeper",
  "add-language": "add-language",
};

const HOW_TO_USE = `This is Phygital Brain ${VERSION}, through its connector.

- The instructions below are a skill. Follow them step by step.
- Where they name a file relative to the skill (for example "forms/form-1-about-you.html", "templates/root-CLAUDE.md", "i18n/pt-BR/strings.json" or "../brain-keeper/SKILL.md"), read it with the phygital_brain_read_file tool. Pass the path from the skills folder: "brain-setup/forms/form-1-about-you.html", "brain-setup/i18n/pt-BR/strings.json", "brain-keeper/SKILL.md".
- This connector only gives you Phygital Brain's files. Write the person's brain yourself, with your own file tools, in the folder they chose. If you can't write files in a folder, say so and stop: the brain needs an agent that can.
- Paths that start with a brain folder (About/, Daily/, Projects/...) are in the person's brain, not here.`;

// Every tool only reads this package's own files: none changes anything, here or in the person's brain.
const READ_ONLY = { readOnlyHint: true, destructiveHint: false, idempotentHint: true, openWorldHint: false };

const TOOLS = [
  {
    name: "phygital_brain_start",
    title: "Start a Phygital Brain job",
    description:
      "Start a Phygital Brain job: returns that job's step-by-step instructions (a skill) as text, for you to follow. It changes nothing by itself: you then build or change the person's brain with your own file tools, in the folder they chose. Call it first when the person says 'set up my second brain', 'upgrade my second brain', 'set up my team', 'set up my brain keeper', 'translate Phygital Brain into my language', 'switch my brain to another language', or the same in another language. Calling it again returns the same instructions. To open a file the instructions name, use phygital_brain_read_file; to see which files exist, use phygital_brain_list_files. An unknown job returns an error naming the valid ones.",
    inputSchema: {
      type: "object",
      properties: {
        job: {
          type: "string",
          enum: Object.keys(JOBS),
          description:
            "Which job: 'setup' (the default; also upgrades a brain and sets up a team), 'brain-keeper' (set up, update or move the scheduled task that tidies the brain) or 'add-language' (make Phygital Brain in a new language, or switch a brain's language).",
        },
      },
      additionalProperties: false,
    },
    annotations: { title: "Start a Phygital Brain job", ...READ_ONLY },
  },
  {
    name: "phygital_brain_read_file",
    title: "Read a Phygital Brain file",
    description:
      "Read one of Phygital Brain's own files and return its full text: a form, a template, a language file or a skill. Use it when the instructions from phygital_brain_start name a file; if you don't know the exact name, list the folder with phygital_brain_list_files first. A missing file, a folder, or a path outside the skills folder returns an error that says so. It reads only Phygital Brain's files, never the person's brain, and changes nothing.",
    inputSchema: {
      type: "object",
      properties: {
        path: {
          type: "string",
          description:
            "The file's path inside Phygital Brain's skills folder, like 'brain-setup/forms/form-1-about-you.html' or 'brain-setup/i18n/ja/templates/root-CLAUDE.md'. Paths that start with a brain folder (About/, Daily/, Projects/...) are in the person's brain, not here.",
        },
      },
      required: ["path"],
      additionalProperties: false,
    },
    annotations: { title: "Read a Phygital Brain file", ...READ_ONLY },
  },
  {
    name: "phygital_brain_list_files",
    title: "List Phygital Brain files",
    description:
      "List what's in one of Phygital Brain's folders: one name per line, sorted, with folders ending in '/'. It doesn't look inside subfolders: list a subfolder to see its files. Use it to find a file's exact name, then open the file with phygital_brain_read_file. A folder that doesn't exist returns an error. It reads only Phygital Brain's files, never the person's brain, and changes nothing.",
    inputSchema: {
      type: "object",
      properties: {
        path: {
          type: "string",
          description:
            "The folder inside Phygital Brain's skills folder, like 'brain-setup/templates' or 'brain-setup/i18n'. Leave empty to list the skills.",
        },
      },
      additionalProperties: false,
    },
    annotations: { title: "List Phygital Brain files", ...READ_ONLY },
  },
];

const PROMPTS = [
  { name: "set-up-my-second-brain", description: "Build a Phygital Brain in the folder you chose.", job: "setup" },
  { name: "brain-keeper", description: "Set up, update or move the Brain Keeper.", job: "brain-keeper" },
  { name: "add-language", description: "Make Phygital Brain in a new language, or switch a brain's language.", job: "add-language" },
];

function safePath(p) {
  const clean = normalize(String(p || "").replace(/^\/+/, ""));
  const full = join(SKILLS, clean);
  const rel = relative(SKILLS, full);
  if (rel.startsWith("..") || rel.includes(`..${sep}`)) throw new Error(`"${p}" is outside Phygital Brain's skills folder.`);
  return full;
}

function startText(job) {
  const dir = JOBS[job || "setup"];
  if (!dir) throw new Error(`Unknown job "${job}". Use one of: ${Object.keys(JOBS).join(", ")}.`);
  const skill = readFileSync(join(SKILLS, dir, "SKILL.md"), "utf8");
  return `${HOW_TO_USE}\n\nThis skill's folder: "${dir}/".\n\n---\n\n${skill}`;
}

function readText(p) {
  const full = safePath(p);
  if (!existsSync(full)) throw new Error(`No file "${p}". Use phygital_brain_list_files to see what's there.`);
  if (statSync(full).isDirectory()) throw new Error(`"${p}" is a folder. Use phygital_brain_list_files.`);
  return readFileSync(full, "utf8");
}

function listText(p) {
  const full = safePath(p);
  if (!existsSync(full) || !statSync(full).isDirectory()) throw new Error(`No folder "${p}".`);
  const items = readdirSync(full)
    .filter((n) => !n.startsWith("."))
    .sort()
    .map((n) => (statSync(join(full, n)).isDirectory() ? `${n}/` : n));
  return items.join("\n");
}

function callTool(name, args = {}) {
  if (name === "phygital_brain_start") return startText(args.job);
  if (name === "phygital_brain_read_file") return readText(args.path);
  if (name === "phygital_brain_list_files") return listText(args.path);
  throw new Error(`Unknown tool "${name}".`);
}

function handle(msg) {
  const { id, method, params = {} } = msg;
  switch (method) {
    case "initialize": {
      const asked = params.protocolVersion;
      return {
        protocolVersion: PROTOCOL_VERSIONS.includes(asked) ? asked : PROTOCOL_VERSIONS[0],
        capabilities: { tools: {}, prompts: {} },
        serverInfo: { name: "phygital-brain", title: "Phygital Brain", version: VERSION },
        instructions:
          "Phygital Brain builds and looks after a second brain: a folder of Markdown notes. When the person asks to set up, upgrade or translate their second brain, call phygital_brain_start first.",
      };
    }
    case "ping":
      return {};
    case "tools/list":
      return { tools: TOOLS };
    case "tools/call": {
      try {
        return { content: [{ type: "text", text: callTool(params.name, params.arguments || {}) }] };
      } catch (e) {
        return { content: [{ type: "text", text: String(e.message || e) }], isError: true };
      }
    }
    case "prompts/list":
      return { prompts: PROMPTS.map(({ name, description }) => ({ name, description })) };
    case "prompts/get": {
      const p = PROMPTS.find((x) => x.name === params.name);
      if (!p) throw { code: -32602, message: `Unknown prompt "${params.name}".` };
      return {
        description: p.description,
        messages: [{ role: "user", content: { type: "text", text: startText(p.job) } }],
      };
    }
    default:
      if (id === undefined) return undefined; // a notification
      throw { code: -32601, message: `Method not found: ${method}` };
  }
}

function send(obj) {
  process.stdout.write(JSON.stringify(obj) + "\n");
}

const rl = createInterface({ input: process.stdin, crlfDelay: Infinity });
rl.on("line", (line) => {
  if (!line.trim()) return;
  let msg;
  try {
    msg = JSON.parse(line);
  } catch {
    send({ jsonrpc: "2.0", id: null, error: { code: -32700, message: "Parse error" } });
    return;
  }
  if (msg.id === undefined) {
    try { handle(msg); } catch { /* notifications get no reply */ }
    return;
  }
  try {
    const result = handle(msg);
    send({ jsonrpc: "2.0", id: msg.id, result: result ?? {} });
  } catch (e) {
    send({ jsonrpc: "2.0", id: msg.id, error: { code: e.code || -32603, message: e.message || String(e) } });
  }
});
