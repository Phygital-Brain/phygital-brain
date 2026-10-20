"""Translations for Phygital Brain. Run from the repository root.

    python3 scripts/i18n.py extract   write the English form texts into languages/en.json
    python3 scripts/i18n.py build     build skills/brain-setup/i18n/{code}/ for every language,
                                      and the language window (skills/brain-setup/forms/language.html)
    python3 scripts/i18n.py check     check every language file and build (also run by scripts/check.py)
    add a language code (build pt-BR, check pt-BR) to do only that one

How it works:
- English is the source: skills/brain-setup/templates/, skills/brain-keeper/templates/ and the four forms.
- Each language has languages/{code}.json (folder and note names, form texts, messages, feature names)
  and languages/{code}/templates/ and languages/{code}/keeper/ (the templates, translated by people
  or agents, with every path left in English).
- build copies those translated templates and turns every English path into the language's names,
  so a path is spelled the same way in every file. It also builds the forms from the English forms
  and the form texts. The setup then copies the built set into the person's brain once.
"""
import glob
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

LANG_DIR = "languages"
OUT_DIR = "skills/brain-setup/i18n"
FORMS = sorted(glob.glob("skills/brain-setup/forms/form-*.html"))
LANGUAGE_FORM = "skills/brain-setup/forms/language.html"
SKILL = "skills/brain-setup/SKILL.md"
SRC_TEMPLATES = "skills/brain-setup/templates"
SRC_KEEPER = "skills/brain-keeper/templates"
KEEP = {"CLAUDE.md", "README.md", "SKILL.md", "eval.md", "LICENSE", ".claudeignore", ".backups", "no-ai-slop"}
TOP = ["About", "Daily", "Projects", "Relationships", "Memory", "Library", "Skills"]
PLACEHOLDERS = re.compile(r"\{[A-Za-z][A-Za-z -]*\}")


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


# ---------- forms ----------

TEXT_NODE = re.compile(r">([^<>]*[A-Za-z][^<>]*)<")
PLACEHOLDER_ATTR = re.compile(r'placeholder="([^"]+)"')
COMMENT = re.compile(r"<!--.*?-->", re.S)


def form_texts(src):
    body = COMMENT.sub("", src)
    texts = []
    for t in TEXT_NODE.findall(body) + PLACEHOLDER_ATTR.findall(body):
        t = t.strip()
        if t and t not in texts:
            texts.append(t)
    return texts


def render_form(src, forms, rtl):
    # Split on comments so text inside them stays as it is (it's for the agent).
    parts = re.split(r"(<!--.*?-->)", src, flags=re.S)
    out = []
    for p in parts:
        if p.startswith("<!--"):
            out.append(p)
            continue
        p = TEXT_NODE.sub(lambda m: ">" + _tr(m.group(1), forms) + "<", p)
        p = PLACEHOLDER_ATTR.sub(lambda m: 'placeholder="' + _tr(m.group(1), forms, attr=True) + '"', p)
        out.append(p)
    html = "".join(out)
    if rtl:
        html = html.replace('<form class="elicit">', '<form class="elicit" dir="rtl">')
    return html


def _tr(text, forms, attr=False):
    key = text.strip()
    if key not in forms:
        return text
    lead = text[: len(text) - len(text.lstrip())]
    trail = text[len(text.rstrip()):]
    val = forms[key]
    if attr:
        val = val.replace('"', "&quot;")
    return lead + val + trail


# ---------- paths ----------

PATH_TOKEN = re.compile(r"(?<![\w/:-])((?:[A-Za-z0-9_{}*.-]+/)+[A-Za-z0-9_{}*.-]*(?:\.md)?)")
WIKILINK = re.compile(r"\[\[([^\]|#]+)(\|[^\]]*)?\]\]")
BACKTICK = re.compile(r"`([^`\n]+)`")


def map_segment(seg, paths):
    if not seg or seg in KEEP or PLACEHOLDERS.fullmatch(seg) or "YYYY" in seg or "*" in seg:
        return seg
    if seg.endswith(".md"):
        stem = seg[:-3]
        if stem in KEEP or PLACEHOLDERS.search(stem) or "YYYY" in stem:
            return seg
        return paths.get(stem, stem) + ".md"
    return paths.get(seg, seg)


def map_path(token, paths):
    if "://" in token:
        return token
    first = token.split("/")[0]
    if first == ".backups":
        # .backups/{date-what}/About/me.md: keep the first two parts, map the rest.
        parts = token.split("/")
        return "/".join(parts[:2] + [map_segment(s, paths) for s in parts[2:]])
    if first not in paths and first not in ("Clients", "Team", "Collaborators", "Partners"):
        # Only paths that start with a brain folder (or a Relationships subfolder) are mapped.
        if not any(seg in paths for seg in token.split("/")[:1]):
            return token
    return "/".join(map_segment(s, paths) for s in token.split("/"))


def render_template(text, paths):
    # Leave URLs alone.
    urls = {}

    def keep_url(m):
        k = f"\x00{len(urls)}\x00"
        urls[k] = m.group(0)
        return k

    text = re.sub(r"https?://\S+", keep_url, text)

    def backtick(m):
        inner = m.group(1)
        if "/" in inner:
            return "`" + PATH_TOKEN.sub(lambda t: map_path(t.group(1), paths), inner) + "`"
        if inner in TOP or inner in paths and inner[0].isupper():
            return "`" + paths.get(inner, inner) + "`"
        if inner.endswith(".md") and inner[:-3] in paths:
            return "`" + map_segment(inner, paths) + "`"
        return m.group(0)

    text = BACKTICK.sub(backtick, text)

    # Paths outside backticks (code blocks, plain task files).
    def plain(m):
        return map_path(m.group(1), paths)

    lines = []
    for line in text.split("\n"):
        if "`" not in line:
            line = PATH_TOKEN.sub(plain, line)
        lines.append(line)
    text = "\n".join(lines)

    # Links to the fixed notes.
    text = WIKILINK.sub(lambda m: "[[" + paths.get(m.group(1), m.group(1)) + (m.group(2) or "") + "]]", text)

    for k, v in urls.items():
        text = text.replace(k, v)
    return text


def render_queue_next(text, paths):
    # queue.md ends with the first folder of the sweep as plain text.
    return re.sub(r"(## [^\n]+\n\n)About\s*$", lambda m: m.group(1) + paths.get("About", "About") + "\n", text)


# ---------- commands ----------

ONLY = None


def languages():
    codes = sorted(os.path.basename(p)[:-5] for p in glob.glob(f"{LANG_DIR}/*.json") if not p.endswith("/en.json"))
    return [c for c in codes if ONLY is None or c == ONLY]


def extract():
    en_path = f"{LANG_DIR}/en.json"
    en = load(en_path)
    forms = {}
    for f in FORMS:
        for t in form_texts(open(f, encoding="utf-8").read()):
            forms[t] = t
    en["forms"] = forms
    save(en_path, en)
    print(f"{len(forms)} form texts written to {en_path}")


def build():
    if ONLY is None:
        _write(LANGUAGE_FORM, language_form())
        print(f"built {LANGUAGE_FORM}")
    for code in languages():
        lang = load(f"{LANG_DIR}/{code}.json")
        paths = lang["paths"]
        rtl = lang["language"].get("dir") == "rtl"
        out = f"{OUT_DIR}/{code}"
        for f in FORMS:
            html = render_form(open(f, encoding="utf-8").read(), lang["forms"], rtl)
            _write(f"{out}/forms/{os.path.basename(f)}", html)
        for kind, src in (("templates", SRC_TEMPLATES), ("keeper", SRC_KEEPER)):
            for f in sorted(glob.glob(f"{src}/*")):
                name = os.path.basename(f)
                tr = f"{LANG_DIR}/{code}/{kind}/{name}"
                text = open(tr if os.path.exists(tr) else f, encoding="utf-8").read()
                text = render_template(text, paths)
                if name == "queue.md":
                    text = render_queue_next(text, paths)
                _write(f"{out}/{kind}/{name}", text)
        meta = {k: lang[k] for k in ("language", "status", "paths", "features", "messages")}
        save(f"{out}/strings.json", meta)
        print(f"built {out}")


# ---------- the language window ----------

def language_order():
    """The ready languages in the order SKILL.md Step 1 lists them, then any it doesn't list."""
    step1 = open(SKILL, encoding="utf-8").read().split("## Step 1", 1)[1].split("\n## ", 1)[0]
    listed = re.findall(r"`[^`]+` \(([A-Za-z-]+)\)", step1)
    ready = ["en"] + sorted(os.path.basename(p)[:-5] for p in glob.glob(f"{LANG_DIR}/*.json") if not p.endswith("/en.json"))
    return [c for c in listed if c in ready] + [c for c in ready if c not in listed]


def language_form():
    """The window for Step 1: one card per ready language, in its own name, then Other."""
    header = re.search(r"\n(    <svg viewBox.*?</svg>)\n", open(FORMS[-1], encoding="utf-8").read()).group(1)
    style = ("border-radius:12px; padding:12px 14px; display:flex; flex-direction:column; align-items:flex-start; "
             "text-align:left; min-width:150px; box-shadow:0 1px 2px rgba(0,0,0,0.04)")
    cards = []
    for code in language_order():
        meta = load(f"{LANG_DIR}/{code}.json")["language"]
        name, english = meta["name"], meta.get("english_name", meta["name"])
        sub = f'<span style="font-size:11px; color:var(--text-muted)">{english}</span>' if english != name else ""
        pressed = ' aria-pressed="true"' if code == "en" else ""
        cards.append(f'        <button type="button" class="elicit-pill"{pressed} data-value="{code}" style="{style}">'
                     f'<span style="font-size:13px; font-weight:500">{name}</span>{sub}</button>')
    cards.append(f'        <button type="button" class="elicit-pill" data-value="other" data-other style="{style}">'
                 '<span style="font-size:13px; font-weight:500; color:#F05AB8">Other</span>'
                 '<span style="font-size:11px; color:var(--text-muted)">Type your language</span></button>')
    return "\n".join([
        '<h2 class="sr-only">Setup: which language the brain should speak.</h2>',
        "<!-- Made by scripts/i18n.py build from languages/*.json: don't edit by hand. ADAPTING: before showing it, "
        "move aria-pressed=\"true\" to the language of their first message (English if unclear), and translate the "
        "header, the question, Other, its hint and the buttons into that language. Leave every language name as it is. -->",
        '<form class="elicit">', '  <div class="elicit-header">', header,
        "    <span>Brain details: language</span>", "  </div>", '  <div class="elicit-body">',
        '    <div class="elicit-group">',
        '      <label class="elicit-question">Which language should your brain speak?</label>',
        '      <div class="elicit-pills" data-name="language" data-multi="false">', *cards, "      </div>",
        '      <input type="text" class="elicit-other" data-for="language" placeholder="Català" hidden>',
        "    </div>", "  </div>", '  <div class="elicit-footer">',
        '    <button type="button" class="elicit-submit">Continue</button>', "  </div>", "</form>", ""])


def _write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def check():
    problems = []
    en = load(f"{LANG_DIR}/en.json")
    need = {k: set(en[k]) for k in ("paths", "features", "messages", "forms")}
    src_files = {("templates", os.path.basename(f)): f for f in glob.glob(f"{SRC_TEMPLATES}/*")}
    src_files.update({("keeper", os.path.basename(f)): f for f in glob.glob(f"{SRC_KEEPER}/*")})
    for code in languages():
        lang = load(f"{LANG_DIR}/{code}.json")
        for k, keys in need.items():
            missing = keys - set(lang.get(k, {}))
            if missing:
                problems.append(f"{code}.json: {len(missing)} missing in {k}, e.g. {sorted(missing)[:3]}")
            for key, val in lang.get(k, {}).items():
                if "\u2014" in str(val):
                    problems.append(f"{code}.json: em dash in {k}[{key!r}]")
                src = en.get(k, {}).get(key, "")
                if set(PLACEHOLDERS.findall(str(src))) != set(PLACEHOLDERS.findall(str(val))):
                    problems.append(f"{code}.json: placeholders differ in {k}[{key!r}]")
        names = list(lang.get("paths", {}).values())
        if len(names) != len(set(names)) and len(set(names)) < len(names) - 2:
            problems.append(f"{code}.json: several English names map to the same name")
        for n in names:
            if unicodedata.normalize("NFC", n) != n:
                problems.append(f"{code}.json: path name {n!r} isn't in NFC form (accents stored two ways can break sync)")
            if "/" in n or n.strip() != n or any(c in n for c in '\\:*?"<>|'):
                problems.append(f"{code}.json: path name {n!r} isn't a safe folder or file name")
        for (kind, name), src in src_files.items():
            tr = f"{LANG_DIR}/{code}/{kind}/{name}"
            if not os.path.exists(tr):
                problems.append(f"{code}: {kind}/{name} not translated")
                continue
            t = open(tr, encoding="utf-8").read()
            s = open(src, encoding="utf-8").read()
            if "\u2014" in t:
                problems.append(f"{tr}: em dash")
            if set(PLACEHOLDERS.findall(s)) - set(PLACEHOLDERS.findall(t)):
                problems.append(f"{tr}: placeholders missing {sorted(set(PLACEHOLDERS.findall(s)) - set(PLACEHOLDERS.findall(t)))}")
            for tok in sorted(set(re.findall(r"`([A-Z][A-Za-z]+/[^`]*)`", s))):
                if tok not in t:
                    problems.append(f"{tr}: path `{tok}` changed or missing (keep paths in English)")
            fm_s = re.match(r"---\n(.*?)\n---", s, re.S)
            fm_t = re.match(r"---\n(.*?)\n---", t, re.S)
            if fm_s and (not fm_t or [l.split(":")[0] for l in fm_s.group(1).splitlines()] != [l.split(":")[0] for l in fm_t.group(1).splitlines()]):
                problems.append(f"{tr}: info block keys changed")
        for f in FORMS:
            built = f"{OUT_DIR}/{code}/forms/{os.path.basename(f)}"
            if not os.path.exists(built):
                problems.append(f"{built}: not built (run build)")
                continue
            dv = re.findall(r'data-(?:name|value|for)="[^"]*"', open(f, encoding="utf-8").read())
            if dv != re.findall(r'data-(?:name|value|for)="[^"]*"', open(built, encoding="utf-8").read()):
                problems.append(f"{built}: answer names or values changed")
    if ONLY is None:
        if not os.path.exists(LANGUAGE_FORM) or open(LANGUAGE_FORM, encoding="utf-8").read() != language_form():
            problems.append(f"{LANGUAGE_FORM}: out of date (run build)")
        step1 = open(SKILL, encoding="utf-8").read().split("## Step 1", 1)[1].split("\n## ", 1)[0]
        for code in ["en"] + languages():
            if f"({code})" not in step1:
                problems.append(f"{SKILL}: Step 1 doesn't list {code}")
    if problems:
        print("\n".join(problems))
        print(f"\n{len(problems)} translation problem(s).")
        return 1
    print(f"Translations OK: {', '.join(languages()) or 'none yet'}.")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if len(sys.argv) > 2:
        ONLY = sys.argv[2]
    if cmd == "extract":
        extract()
    elif cmd == "build":
        build()
    else:
        sys.exit(check())
