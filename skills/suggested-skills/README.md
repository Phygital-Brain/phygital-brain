# Suggested skills

Skills made by other people that work well with your brain. A skill teaches your agent how to do a job; to give it access to an app, like Gmail or Canva, see [Suggested apps](../suggested-apps/README.md). They aren't part of Phygital Brain and aren't installed with it: you choose the ones you want. Each page says what you need, how to install it and how to connect it to your brain. How skills fit in your brain: [Add more skills](../../docs/add-skills.md).

| Skill | What it does | Good for | What you need | Page |
|---|---|---|---|---|
| HyperFrames | Makes videos and animations in your brand | People who make videos, reels or motion for their work or clients | A computer, Node.js 22 or newer and FFmpeg | [hyperframes.md](hyperframes.md) |
| Impeccable | Reviews and polishes the design of your websites and apps | People who build or run a website or app | A computer and an agent that can work on code | [impeccable.md](impeccable.md) |
| last30days | Researches what people said about a topic in the last 30 days, with links | People who follow trends, research their market or write about a field | A computer, an agent that can run commands, and Python 3.12 or newer | [last30days.md](last30days.md) |
| GEO-SEO | Checks how easy a website is to find in AI search and Google, with a fix list | People who sell through a website, or do websites or marketing for clients | A computer, Claude Code, Python 3.10 or newer and Git | [geo-seo.md](geo-seo.md) |
| Agent Skills | Makes your agent plan, build, test and review software step by step | People who build software, apps or tools | A computer and an agent that can work on code | [agent-skills.md](agent-skills.md) |
| Document skills | Makes Word documents, PowerPoint decks, Excel spreadsheets and PDFs from your notes | People who send proposals, quotes, reports or decks | Nothing in the Claude app (paid plans); a computer elsewhere | [document-skills.md](document-skills.md) |
| Skill Creator | Turns something you do often into your own skill, and tests it | People with a task they repeat every week, like a client update | Nothing in the Claude app (paid plans); a computer elsewhere | [skill-creator.md](skill-creator.md) |
| Public Relations | Finds your story angles, writes pitches and press releases, and prepares you for podcasts and press questions | People who want press coverage for their work, a launch or a studio | A computer, an agent that can run commands, and Node.js | [public-relations.md](public-relations.md) |
| Marketing Psychology | Uses behavioural science to explain why people buy, and improves your copy, pricing and offers | People who sell a product or service, or write marketing for clients | A computer, an agent that can run commands, and Node.js | [marketing-psychology.md](marketing-psychology.md) |
| Diagram Design | Draws clean diagrams in your brand: flowcharts, timelines, journeys, org charts and more | People who explain processes, plans or ideas to clients or a team | A computer and an agent that can work with files | [diagram-design.md](diagram-design.md) |
| Taste Skill | Builds web pages with a real design direction, so they don't look AI-made | People who build or run a website, landing page or portfolio | A computer, Node.js 22 or newer and Chrome, Edge or Chromium | [taste-skill.md](taste-skill.md) |
| Ponytail | Makes your agent write the smallest code that works, and reviews code in plain words | People who build software, apps, sites or tools with an agent | A computer and an agent that can work on code | [ponytail.md](ponytail.md) |

## For your agent

- **At the end of setup** (`../brain-setup/SKILL.md`, Step 4.1), the suggested skills and the suggested apps in `../suggested-apps/README.md` are offered together, in one list. Read what you know about the person (their answers and the About files you just built) and keep only what clearly fits their "Good for", at most 5 in all. Leave out apps that are already connected in this chat and skills you already have. If nothing fits clearly, show nothing.
- **Describe each one for them**, in their language, in one or two sentences: what it does, and what it would do for their own work, named from their answers. Not "for your reels", but "HyperFrames (skill): turns a script into a short video in your brand colours, so you can make the weekly reels for your bakery without a video editor."
- **When they ask "what can I add to my brain?"**: show both whole tables, the ones that fit them first.
- **Either way:** leave out the ones that need a computer when they're on a phone, and the ones their agent can't run.
- For each skill they pick, follow its page: check what it needs, ask before installing anything, run an install two picks share only once, then write `Skills/{skill-name}/notes.md` from the page's example and add a row for it in `Skills/CLAUDE.md`.

## Add a skill to this list

One page per skill, named in kebab-case (`hyperframes.md`), with the same sections as the others: what you need, install it, connect it to your brain, use it, change it yourself, good to know. Then add a row to the table above, with a "Good for" line that says plainly who it helps.
