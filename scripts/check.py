"""Checks for Phygital Brain. Run from the repository root: python3 scripts/check.py

No installs needed. It checks:
- every link between files in the docs points to a file that exists (templates are skipped)
- every file a skill names (templates/..., forms/..., ../brain-keeper/...) exists
- no long dashes (em dashes) anywhere in the text files
- the four forms have balanced HTML tags, and no "--" inside a comment
- the plugin files are valid JSON with the same version as CHANGELOG.md
- every language in languages/ is complete and built (scripts/i18n.py check)
- skills/brain-setup/translating.md lists every folder and note name in languages/en.json
"""
import glob
import json
import os
import re
import sys
from urllib.parse import unquote
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
problems = []

text_files = [f for f in glob.glob("**/*", recursive=True)
              if os.path.isfile(f) and f.endswith((".md", ".html", ".json", ".txt", ".yml", ".cff", ".py", ".mjs"))]
text_files += [".gitignore", ".gitattributes"]

# 1. Links in Markdown files
for f in glob.glob("**/*.md", recursive=True):
    if "/templates/" in f:
        continue  # templates show link examples on purpose
    for target in re.findall(r"\]\(([^)\s]+)\)", open(f, encoding="utf-8").read()):
        path = unquote(target.split("#")[0])
        if not path or path.startswith(("http://", "https://", "mailto:")):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), path))):
            problems.append(f"{f}: broken link to {target}")

# 2. Files named in the skills
for skill in glob.glob("skills/*/SKILL.md"):
    base = os.path.dirname(skill)
    for ref in set(re.findall(r"`((?:templates|forms|\.\./[a-z-]+)/[A-Za-z0-9_./-]+)`", open(skill, encoding="utf-8").read())):
        if not os.path.exists(os.path.normpath(os.path.join(base, ref))):
            problems.append(f"{skill}: names {ref}, which doesn't exist")

# 3. Em dashes
for f in text_files:
    if f == "scripts/check.py" or not os.path.exists(f):
        continue
    for n, line in enumerate(open(f, encoding="utf-8"), 1):
        if "—" in line:
            problems.append(f"{f}:{n}: em dash")

# 4. Forms
VOID = {"input", "br", "img", "path", "meta"}
for f in glob.glob("skills/brain-setup/forms/*.html"):
    src = open(f, encoding="utf-8").read()
    for comment in re.findall(r"<!--(.*?)-->", src, re.S):
        if "--" in comment:
            problems.append(f"{f}: '--' inside a comment")
    stack, bad = [], []

    class P(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag not in VOID:
                stack.append(tag)

        def handle_endtag(self, tag):
            if tag in VOID:
                return
            if stack and stack[-1] == tag:
                stack.pop()
            else:
                bad.append(tag)

    P().feed(re.sub(r"<!--.*?-->", "", src, flags=re.S))
    if bad or stack:
        problems.append(f"{f}: unbalanced tags {bad or stack}")

# 5. Plugin files and version
versions = set()
for f in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", "package.json"):
    try:
        data = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        problems.append(f"{f}: not valid JSON ({e})")
        continue
    versions.add(data.get("version") or data["plugins"][0]["version"])
changelog = re.search(r"^## (\d+\.\d+\.\d+)", open("CHANGELOG.md", encoding="utf-8").read(), re.M)
if changelog:
    versions.add(changelog.group(1))
if len(versions) != 1:
    problems.append(f"versions don't match: {sorted(versions)}")

# 6. Translations
names = json.load(open("languages/en.json", encoding="utf-8"))["paths"]
tr = open("skills/brain-setup/translating.md", encoding="utf-8").read().split("## The names", 1)[-1]
missing = [n for n in names if f"`{n}`" not in tr]
if missing:
    problems.append("skills/brain-setup/translating.md: names missing from The names: " + ", ".join(missing))
import subprocess
r = subprocess.run([sys.executable, "-I", "scripts/i18n.py", "check"], capture_output=True, text=True)
if r.returncode != 0:
    problems.append("translations:\n" + r.stdout.strip())

if problems:
    print("\n".join(problems))
    print(f"\n{len(problems)} problem(s).")
    sys.exit(1)
print("All checks passed.")
