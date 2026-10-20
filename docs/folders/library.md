# Library

## What it's for

`Library/` holds things you use again and again: prompts, templates, checklists, ways of working, useful links. It's your toolbox. Keep it small.

The rules your agent follows here: [library-CLAUDE.md](../../skills/brain-setup/templates/library-CLAUDE.md).

## What's inside

At first, nothing. Files appear when you save something. When there are several of one kind, they get their own folder:

```
Library/
├── prompts/       prompts you use often
├── templates/     an email you send a lot, a quote layout
└── frameworks/    ways of working, checklists
```

## Inside, one by one

These folders are examples. They only appear when you have a few files of one kind. Until then, files sit right in `Library/`.

### `prompts/`: words you give your agent again and again

**What it's for:** prompts that work well, so you don't have to write them again.

**What goes in:** one prompt per file, with a name that says what it does, like `prompts/cover-ideas.md` or `prompts/instagram-caption.md`.

**You say:** "Save this prompt for cover ideas." "Use my caption prompt for this drawing."

### `templates/`: things you fill in again and again

**What it's for:** the shape of something you make often, so each new one is quick.

**What goes in:** an email you send a lot, a quote layout, a project kickoff list, like `templates/late-payment-email.md` or `templates/quote.md`.

**You say:** "Make a template for my quote emails." "Use my quote template for the bakery."

### `frameworks/`: ways of working

**What it's for:** how you do things, written down: steps, checklists, methods you trust.

**What goes in:** notes such as `frameworks/sending-files-to-print.md` or `frameworks/how-i-price-a-cover.md`.

**You say:** "Write down my checklist for sending files to print." "How do I usually price a cover?"

### Other things worth keeping

Useful links, reference lists, a reading list. A note says where to find things you can download. The library never holds copies of other people's work.

### Your own folders

When you have several files of a new kind, your agent can suggest a folder for them, like `Library/reading/`. It asks first.

## How to use it

- "Save this prompt, I'll use it again."
- "Make a template for my quote emails."
- "Save this checklist for sending files to print."
- "What prompts do I have?"

## Examples

| You say | What happens |
|---|---|
| "Save this prompt for book cover ideas." | A file with a clear name, like `Library/cover-ideas-prompt.md`. |
| "Here's my email for late payments, keep it." | Saved as a template. When there are a few, they move into `templates/`, after your agent asks. |
| "Use my quote template for the bakery." | Your agent reads it from `Library/` and fills it in. |

## Rules

- Each file gets a clear name, so you can find it later.
- Folders appear only when there are several files of one kind.
- Research goes in `Memory/`, project files in `Projects/`. The library links to them and doesn't copy them.
- No copies of other people's work or files you can download. A note says where to get them instead.

## What the Brain Keeper does here

- **Every day:** fixes info blocks, one folder at a time.
- **Check-up:** flags files no other note links to, and the same thing saved twice.
