# Main rules

The file `CLAUDE.md` at the top of your brain holds the rules your agent follows everywhere. Your agent reads it at the start of every chat. This page explains it in plain words.

The real file: [root-CLAUDE.md](../../skills/brain-setup/templates/root-CLAUDE.md).

## What your agent does at the start of every chat

Without saying anything, it reads:

1. The newest daily note, to know what happened lately.
2. `About/me.md`, to know who you are and how you like to work.
3. `Daily/tasks.md`, to know what's still open.

Then it answers you. It never says "loading" or "I read your files".

## Where things go

Everything has one home. There's no "misc" pile.

| You tell your agent... | It goes to... |
|---|---|
| How you like to work, your habits | `About/me.md` |
| A goal | `About/goals.md` |
| Something about your business, prices or customers | `About/` |
| News about a project | `Projects/` |
| Something about a person or company | `Relationships/` |
| A decision, research, money, an application | `Memory/` |
| A prompt or template you'll use again | `Library/` |
| What happened today | `Daily/` |

## How your agent talks to you

It talks the way you chose in the setup (for example "short and plain"), and in your language. You can change this anytime: "From now on, give me longer answers."

## The rules, in plain words

**Saving**
- After real work (not small talk), it writes a short line in today's daily note.
- It saves small updates (a date, a new fact) to a note that already exists, then tells you in one line.
- It **asks first** before it makes a new note or folder, rewrites a note, or moves, renames or deletes anything.
- Before deleting or moving, it checks which notes link to that one and tells you what would break.
- It never makes files at the very top of your brain. Everything goes in a folder.

**Writing notes**
- Every person, company and project gets a `[[link]]`, inside the sentence.
- Every note can stand on its own, like a Lego block.
- Notes sound like a teammate wrote them: real names, real dates, real next steps. Not "the project is going well".
- No long dashes, ever. Periods, commas and colons instead.
- No AI-sounding words like "delve", "seamless" or "game-changer". Your own voice wins.
- For writing other people will read (emails, posts, bios), it shows you the AI-sounding bits it found and lets you choose before it changes them.

**Doing only what you asked**
- It does what you asked, nothing extra. If it has an idea, it tells you and waits.
- Quick asks (a prompt, a short message, a rewrite) come straight in the chat, with no files.
- Comparisons are fair: each option is judged on its own, not on what fits you, unless you ask.

**Projects and decisions**
- A project's planning stays in one note until you actually start building it.
- Big decisions go in `Memory/decisions/`, with the reason why.
- A finished project only moves to the archive when you say so.

**Your private things**
- Tax numbers, bank details, card numbers, your full legal name and your birth date live in one note only. Your agent never copies them anywhere else, and never repeats them in a reply. At most it shows the last 4 digits.
- Passwords, keys and codes never go in a note. Use a password manager.
- If a link is broken, it never makes a blank note to "fix" it. The real note might still be syncing from Google Drive.

**Time**
- It checks your computer's clock and time zone first, in case you're travelling.

**If you sell things**
- Chat messages to clients are short and friendly: no bullet lists, 3 or 4 short paragraphs at most.
- It never promises a price or a proposal before it understands the whole job. It asks for the details first.

## Your own rules

When you correct your agent ("don't do that", "always do this"), it saves your correction as a new rule at the bottom of the file, under your name. It doesn't ask. These are yours, and upgrades never change them.

## Things your agent never reads

The file `.claudeignore` lists what your agent must not open unless you ask for that exact file:

- Password and key files (`.env`, `*.key`, `*.pem`, `credentials/`, `secrets/`)
- `Memory/finances/`, your money folder

You can add your own private folders, like `health/` or `journal/`.

## Work habits your agent follows

- If something is unclear, it asks instead of guessing.
- It picks the simplest way that works.
- It only changes what it needs to.
- It checks its own work before it says it's done.
