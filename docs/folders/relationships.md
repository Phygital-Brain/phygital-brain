# Relationships

## What it's for

`Relationships/` holds the people and companies you work with. Each one gets one note. Your agent uses these notes to remember who's who, what you did together and when you last talked.

The rules your agent follows here: [relationships-CLAUDE.md](../../skills/brain-setup/templates/relationships-CLAUDE.md) and [relationships-subfolder-CLAUDE.md](../../skills/brain-setup/templates/relationships-subfolder-CLAUDE.md).

## What's inside

There's a folder for each kind of person. You only get the ones you picked in the setup.

| Folder | Who goes there |
|---|---|
| `Clients/` | People and companies you do paid work for (only if you sell things) |
| `Collaborators/` | Creative partners, swapping help, no money |
| `Team/` | People who work with you or for you: freelancers, assistants |
| `Partners/` | Organisations you're growing with: press, venues, platforms |

If you picked "just me", there are no folders yet. They appear when the first person does.

`Clients/` can also have `_Leads.md`: people who might become clients.

## Inside, one by one

Every folder here has its own small rule file. It says who belongs there and how their note is built. Every note uses the same shape (see "How a person's note looks" below). Only the `type` changes: `client`, `collaborator`, `team` or `partner`.

### `Clients/`: people you do paid work for

**What it's for:** everyone who pays you, or might soon. Companies and people.

**Who goes here:** a publisher you make covers for, a bakery that wants a logo, a person who buys a portrait.

**What goes in each note:** who they are, the contact people there, how you met, every job you did together with month and year, and notes like "pays on time" or "next chance: their spring list".

**You say:** "New client: a bakery in Lisbon wants a logo." "What have I done for Penguin Kids?" "Marta from Penguin Kids called."

**Good to know:** a company's people (an editor, a manager) are written inside the company's note, not as their own notes. To mention them elsewhere, your agent writes `[[Penguin Kids|Marta]]`, so the link goes to the company.

Only made if you sell things.

### `Clients/_Leads.md`: people who might become clients

**What it's for:** people who showed interest but aren't clients yet, so nobody gets forgotten.

**What goes in:** two lists, **New** and **Keep warm**. One line each: date, name, what they want, where they came from.

```
## New

- 2026-10-20: Casa do Pão, logo for a bakery, found me on Instagram

## Keep warm

- 2026-09-02: Galeria Azul, maybe a show next year, met at the fair
```

**You say:** "A bakery asked about a logo, nothing firm yet." "The gallery said maybe next year."

**Good to know:** when a lead sends a real brief, books a call or asks for a quote, it leaves this list and gets its own note in `Clients/` with `status: prospect`.

### `Collaborators/`: creative partners

**What it's for:** people you make things with, where you swap help and no money changes hands.

**Who goes here:** a writer you make a book with, a musician who scores your video, a friend you share a stand with at a fair.

**You say:** "I'm making a zine with Rita, she writes and I draw." "When did I last work with Rita?"

### `Team/`: people who work with you or for you

**What it's for:** the people on your side: freelancers you hire, an assistant, a studio partner.

**Who goes here:** a colourist you pay per page, a person who does your accounts, a studio mate.

**What goes in each note:** what they do for you, how you work together, rates if you pay them, and every job with month and year.

**You say:** "I hired Leo to colour the book." "How much did I pay Leo last time?"

### `Partners/`: organisations you grow with

**What it's for:** places and groups that help you be seen: press, galleries, venues, festivals, platforms.

**Who goes here:** a magazine that wrote about you, a book fair, a shop that sells your prints, an online platform.

**You say:** "The Bologna fair accepted my portfolio." "Which magazines have I worked with?"

### New kinds of people

If someone fits none of these folders, your agent asks before making a new one, like `Relationships/Students/`.

## How a person's note looks

```
---
type: client
status: active
last-contact: 2026-10
tags: [relationship, client, publishing, uk]
description: "Children's publisher. Ana's main client since 2025."
---

Penguin Kids publishes picture books for ages 3 to 7.

## Contacts

Marta Silva: marta@example.com (editor, prefers email)

## How it started

Met at the Bologna book fair, 2025.

## Work together

- 2026-10: Picture book about the sea
- 2025-06: Two book covers

## Notes

Pays on time. Next chance: their spring list.
```

The parts are always the same: who they are, contacts, how it started, the work you did together (with month and year), and notes.

## The status of a person

| Status | Means |
|---|---|
| `active` | You worked or talked in the last 12 months |
| `prospect` | You're talking, but you never worked together |
| `dormant` | No contact for more than 12 months |
| `closed` | It ended for good |

`last-contact` is the last month you really talked or worked together, like `2026-10`.

## How to use it

- "I met João at the fair, he runs a small press in Porto."
- "Marta emailed, she wants two more covers."
- "Who haven't I talked to in a while?"
- "What did I do with Penguin Kids last year?"

## Examples

| You say | What happens |
|---|---|
| "New client: a bakery in Lisbon wants a logo." | Your agent checks the name isn't already there, asks first, then makes their note in `Clients/` with `status: prospect`. |
| "Had a call with Marta today." | Penguin Kids' `last-contact` becomes this month. Today's daily note gets a line. |
| "A gallery said maybe next year." | One line under **Keep warm** in `_Leads.md`. |
| "Write to Marta about the delay." | Your agent reads the note, then drafts it in your voice. You read it and send it yourself. |

## Rules

- **No doubles.** Before making a note, your agent searches for the name and other spellings. If it finds one, it uses it and adds the new spelling as an alias.
- **Truth at the top.** Who they are and where things stand now at the top, the dated history below.
- **Contact people** at a company (an editor, an agent) are written inside the company's note. They don't get their own note or link.
- **Private details** (phone, email, home address) stay only in that person's note. They're never copied into daily notes or anywhere else.
- A new kind of folder only appears when a new kind of person shows up. Your agent asks first.

## What the Brain Keeper does here

- **Every day:** changes `active` to `dormant` when there's been no contact for 12 months (in safe fix mode). It fixes info blocks.
- **Check-up:** flags two notes for the same person, and notes where old news hides the current truth.
