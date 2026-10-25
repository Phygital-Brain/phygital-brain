# Fast search with Phygital Engram

When your brain grows past a few thousand notes, your agent can look things up faster with [Phygital Engram](https://github.com/Phygital-Brain/phygital-engram), a separate search add-on.

## Do you need it?

Probably not yet. A brain of a few hundred notes works well as it is, because the folders, names and links do most of the finding. Think about Phygital Engram when:

- your agent is slow to answer questions about your past work
- it misses a note that you know is there
- you have years of daily notes, decisions and projects

You can start without it and add it later. Nothing in your brain has to change.

## What it does

Phygital Engram searches your brain's notes and gives your agent a short list of the best matches. Each one shows its note, its heading and its date, so you can see where an answer came from. Your agent reads that list instead of opening dozens of notes.

It only reads your notes. It never writes, moves or deletes one. It keeps its own files in a separate folder, which you can delete at any time without touching your brain. It collects nothing and sends nothing anywhere.

## What your brain already gives it

A Phygital Brain is a good fit, because it already has what Phygital Engram looks for:

- **A `CLAUDE.md` at the top.** Phygital Engram needs this file at the top of the notes folder before it indexes. Your brain has it. It counts more in the ranking too.
- **A `.claudeignore`.** Phygital Engram skips everything listed there, so `Memory/finances/` stays out of the search.
- **Dates, status and tags** in each note's info block. Newer notes rank higher. Notes marked `done` or `archived` rank lower, and notes in an `archive` folder rank lower still.

We ran it on the example brain in this repository, with an empty `CLAUDE.md` added. It skipped the finances folder, and it found a decision note from a question in plain words (2026-10-25).

## What to know first

- **It is a first release.** Version 0.1.0 has the search, a connector for your AI app and a server version. The pages in its repository say what was and was not tested.
- **Its default folder levels are general.** A rules file (`CLAUDE.md`) counts more, and so does a folder named `Context/`. Notes in any `decisions` folder never fade, so your `Memory/decisions/` is covered. `Library/` and `archive` folders count less. `Memory/finances/` is private by default, and your `.claudeignore` lists it too. Your `About/` folder is not boosted. You can add it in its settings: see [Folder levels and hints](https://github.com/Phygital-Brain/phygital-engram/blob/main/docs/settings.md#folder-levels-and-hints). Test your own questions before and after, because a change can help one question and hurt another. In our small check on the example brain, extra weight on `About/` pushed a note about services above the decision we were looking for.
- **It searches by words,** not by meaning, in the same way your agent does today. It is just much faster on a big brain.

## Set it up

1. Build your brain with Phygital Brain, as usual.
2. Install Phygital Engram and point it at your brain's folder: [Set up on your computer](https://github.com/Phygital-Brain/phygital-engram/blob/main/docs/setup-computer.md).
3. Connect it to your AI app: [Connect your AI app](https://github.com/Phygital-Brain/phygital-engram/blob/main/docs/connect-your-ai.md). For your phone, there is a version that runs on a server you own: [Set up on your own server](https://github.com/Phygital-Brain/phygital-engram/blob/main/docs/setup-own-server.md).
4. Add one rule to your brain, as described next.

## The rule to add

Your agent follows the rules in your brain's main `CLAUDE.md`. Add this line at the end, under your own rules (the last section of the file, called "Your name's Rules"):

> Before answering about my past work, projects, decisions, people or notes, search with Phygital Engram first, then open the best results. If it finds nothing or is not available, read the files instead.

You can ask your agent to add it for you. When you upgrade your brain later, your own rules stay word for word, so this line stays.

The second sentence matters. If Phygital Engram is not installed, is switched off or finds nothing, your agent reads files as it always did. Nothing breaks.

## What does not change

- Your agent still asks before it creates, moves, renames or deletes a note. Phygital Engram never writes to your brain.
- The Brain Keeper reads your notes the normal way and does not use Phygital Engram. If you remove it, the Brain Keeper works as before.
- Your notes stay in your cloud drive, in plain Markdown. You own them, with or without the search.

More about Phygital Engram in [its repository](https://github.com/Phygital-Brain/phygital-engram), including [how it works with a Phygital Brain](https://github.com/Phygital-Brain/phygital-engram/blob/main/docs/with-phygital-brain.md).
