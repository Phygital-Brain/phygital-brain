"""Build the Claude desktop extension: dist/phygital-brain.mcpb. Run from the repository root:

    python3 scripts/build_mcpb.py

A .mcpb file is a zip with manifest.json at the top. It holds the connector (server/index.mjs),
the skills it serves, the plugin file (for the version), the licence and the icon. The Claude
desktop app brings its own Node.js, so people don't need to install anything. Attach the file to
the GitHub release, so the README's "Add to Claude desktop" button can download it.
"""
import json
import os
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
version = json.load(open(".claude-plugin/plugin.json"))["version"]

manifest = {
    "manifest_version": "0.3",
    "name": "phygital-brain",
    "display_name": "Phygital Brain",
    "version": version,
    "description": "A second brain that thinks with you: an OS for your notes, built and kept tidy by your agent.",
    "long_description": "Gives Claude Phygital Brain's setup, forms, templates, 11 language sets, the Brain Keeper and the add-language skill. Say 'Set up my second brain' in a chat on a folder in your cloud drive. Claude writes the notes in that folder; the extension only reads its own files.",
    "author": {"name": "Phygital-Brain", "url": "https://github.com/Phygital-Brain"},
    "homepage": "https://github.com/Phygital-Brain/phygital-brain",
    "documentation": "https://github.com/Phygital-Brain/phygital-brain/blob/main/docs/getting-started.md",
    "support": "https://github.com/Phygital-Brain/phygital-brain/issues",
    "repository": {"type": "git", "url": "https://github.com/Phygital-Brain/phygital-brain"},
    "license": "Apache-2.0",
    "icon": "icon.png",
    "keywords": ["second-brain", "notes", "markdown", "knowledge-base"],
    "server": {
        "type": "node",
        "entry_point": "server/index.mjs",
        "mcp_config": {"command": "node", "args": ["${__dirname}/server/index.mjs"]},
    },
    "tools": [
        {"name": "phygital_brain_start", "description": "Start a job: set up, upgrade, team, Brain Keeper or add a language"},
        {"name": "phygital_brain_read_file", "description": "Read a form, template, language file or skill"},
        {"name": "phygital_brain_list_files", "description": "List Phygital Brain's files in a folder"},
    ],
    "prompts": [
        {"name": "set-up-my-second-brain", "description": "Build a Phygital Brain in the folder you chose", "text": "Set up my second brain with Phygital Brain."},
        {"name": "brain-keeper", "description": "Set up, update or move the Brain Keeper", "text": "Set up my Brain Keeper with Phygital Brain."},
        {"name": "add-language", "description": "Make Phygital Brain in a new language", "text": "Translate Phygital Brain into my language."},
    ],
    "compatibility": {"platforms": ["darwin", "win32", "linux"], "runtimes": {"node": ">=18.0.0"}},
}

os.makedirs("dist", exist_ok=True)
out = "dist/phygital-brain.mcpb"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    z.write("mcp/server.mjs", "server/index.mjs")
    z.write(".claude-plugin/plugin.json", ".claude-plugin/plugin.json")
    z.write("LICENSE", "LICENSE")
    z.write("NOTICE", "NOTICE")
    z.write("docs/images/icon-512.png", "icon.png")
    for base, _, files in os.walk("skills"):
        for f in files:
            if f.startswith("."):
                continue
            path = os.path.join(base, f)
            z.write(path, path)
size = os.path.getsize(out)
print(f"{out}: {size // 1024} KB, version {version}")
