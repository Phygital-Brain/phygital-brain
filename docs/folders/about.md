# About

## What it's for

`About/` holds the facts about you. Your agent reads these to understand you, so it can write like you, plan for you and give advice that fits.

The rules your agent follows here: [about-CLAUDE.md](../../skills/brain-setup/templates/about-CLAUDE.md).

## What's inside

The setup makes a file only when it has something real to put in it. So your `About/` may have fewer files than this list.

| File | What it holds | When it appears |
|---|---|---|
| `me.md` | Who you are, what you do, where you live, your time zone, your strengths, your values, work you say no to, when you focus best, what drains you, your work days, and **how you want your agent to work** | Always |
| `goals.md` | Your main goal for the next 12 months, the areas that matter, what's worrying you, and the projects that help | Always |
| `business.md` | What you sell, how you work, how customers find you | If you sell things |
| `services.md` | Each thing you offer: what it is, who it's for, the price | If you named services or prices |
| `customers.md` | Who buys from you and how they find you | If you sell things |
| `pain-points.md` | What slows you down, in your words | If you answered that question |
| `brand.md` | How you sound: your voice, words you use, words you avoid, your social media | If you chose a voice or gave links |
| `tools.md` | Where you talk to people, and where your notes and work live | If you answered those questions |
| `cv.md` | Your work history, school, press, awards | If you gave a CV or a link with your history |
| `biography.md` | Your story, in your words | If you gave a bio or About page |

## Inside, one by one

### `me.md`: who you are

**What it's for:** your agent reads this first in every chat, so it knows who you are.

**What goes in:** your name, what you do, where you live and your time zone, your strengths, what you stand for, work you say no to, when you focus best, what drains you, your work days, and a link about you.

It also has a part called **How I want my agent to work**: how to talk to you (for example "short and plain"), how you take things in (for example "short lists and examples"), your language, your time zone and your work days.

**You say:** "I moved to Porto." "I focus best at night now." "Stop using bullet points with me."

**Good to know:** your full birth date, if you gave it, lives only here. It's never copied or said back.

### `goals.md`: what you're aiming for

**What it's for:** it tells your agent what matters most, so it can warn you when your work drifts away from it.

**What goes in:** your main goal for the next 12 months, in your words, the areas that matter most, what's worrying you now, and the projects that help reach the goal.

**You say:** "My new goal is to sign a book deal this year." "I'm worried about money this month."

**Good to know:** the Brain Keeper never changes this file by itself. A check-up flags goals with no project.

### `business.md`: your business

**What it's for:** the big picture of how you make money. Only if you sell things.

**What goes in:** what you sell, how you work (alone, with a team, from home), and how customers find you.

**You say:** "I'm starting to sell prints online too." "Most of my work comes from Instagram now."

### `services.md`: what you offer

**What it's for:** a clear list of your offers, so your agent can write quotes and answer clients.

**What goes in:** each service or product: what it is, who it's for, how you charge, and the price if you gave one.

**You say:** "I charge 400 for a cover now." "New service: packaging design."

### `customers.md`: who buys from you

**What it's for:** knowing who your customers are, so your agent can write to them in the right way and find more like them.

**What goes in:** the kinds of customers you have, how they find you, and past clients.

**You say:** "Most of my clients are small publishers." "Schools have started asking for workshops."

**Not here:** one note per client. That's in `Relationships/Clients/`.

### `pain-points.md`: what slows you down

**What it's for:** it helps your agent work on what really gets in your way.

**What goes in:** the problems you named, in your own words, like "admin, quotes and invoices" or "too many ideas, no follow-through".

**You say:** "Invoices take me hours every month." "I keep forgetting to follow up."

### `brand.md`: how you sound

**What it's for:** it makes everything your agent writes for you sound like you.

**What goes in:** your writing voice (for example "warm and personal"), words you use, words you never use, and your social media accounts.

**You say:** "I never say 'creative solutions'." "Here's a post I wrote that sounds like me."

**Good to know:** your voice always wins over the AI-sounding check, except for long dashes. The Brain Keeper never changes this file by itself.

### `tools.md`: where things live

**What it's for:** it tells your agent where to look, and where you talk to people.

**What goes in:** where you talk to people (email, WhatsApp, Slack), where your notes and work live (Google Drive, Notion, a paper notebook), and your social media.

**You say:** "I moved from Notion to Google Docs." "Clients reach me on WhatsApp."

### `cv.md`: your work history

**What it's for:** your agent uses it for bios, applications and pitches, so you don't type your history again.

**What goes in:** jobs, school, press, shows and awards, newest first.

**You say:** "Here's my new CV." (drop the file) "Add the Bologna show to my CV."

### `biography.md`: your story

**What it's for:** the longer story of you, for About pages, interviews and bios.

**What goes in:** your story, in your words, from a bio or About page you gave.

**You say:** "Here's my About page." "Write a short bio from my story."

## How each page is built

Every page has two parts:

1. **The truth today**, at the top. Short and up to date.
2. **Evidence**, at the bottom. A dated line for each change and where it came from, newest first.

When something changes, your agent rewrites the top and adds one line at the bottom. So the top is always current, and you can still see the history.

```
Ana is an illustrator for children's books, based in Lisbon.
She charges per project.

## Evidence

- 2026-11-02: Raised her price for covers (chat).
- 2026-10-20: Setup forms.
```

## How to use it

Tell your agent things about yourself, in any chat on your brain:

- "I moved to Porto."
- "I don't take tobacco clients anymore."
- "My new goal is to sign a book deal this year."
- "I charge 400 for a cover now."
- "Stop using bullet points with me."

## Examples

| You say | What happens |
|---|---|
| "I moved to Porto." | `me.md`: the city and time zone change at the top, and a dated line goes at the bottom. |
| "I now do packaging design too." | `services.md` gets a new service. `business.md` may get a line. |
| "Here's my new CV." (drop the file) | `cv.md` is updated with the new jobs, newest first. |
| "Write a bio for a festival." | Your agent reads `me.md`, `cv.md` and `brand.md`, then writes it in your voice. |

## Rules

- These pages are the main source about you. Other notes link here instead of copying.
- Your full birth date lives only in `me.md`. Your agent never copies it or says it back. The birth year is fine.
- A new file here only when a new topic really needs one. Your agent asks first.
- The info block always starts with `type: about`.

## What the Brain Keeper does here

- **Every day:** fixes missing or broken info blocks. It never changes `goals.md` or `brand.md` by itself.
- **Check-up:** points out goals with no project, pages where old news hides the current truth, and facts that disagree with a newer decision.
