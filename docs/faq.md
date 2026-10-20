# FAQ

Questions people ask about Phygital Brain, grouped by topic. If yours isn't here, open an issue with the **Question** form.

**On this page:** [The basics](#the-basics) · [Before you start](#before-you-start) · [Agents](#agents) · [Cloud drives](#cloud-drives) · [The setup](#the-setup) · [Every day](#every-day) · [The Brain Keeper and the morning brief](#the-brain-keeper-and-the-morning-brief) · [Your phone](#your-phone) · [Privacy and safety](#privacy-and-safety) · [Languages](#languages) · [Changing it](#changing-it) · [Updating and leaving](#updating-and-leaving) · [Cost and licence](#cost-and-licence) · [Problems](#problems)

## The basics

### What is Phygital Brain?

An OS (operating system) for your notes and your AI agent. It builds one folder in your cloud drive with three kinds of things: rule files that tell your agent where everything goes, notes your agent writes as you talk, and the Brain Keeper, which tidies the folder every work day. See [How it works](how-it-works.md).

### Why call it an operating system?

Because each part does a job an operating system does. The rule files are the system rules, the folders are the file system, `About/me.md` holds your settings, the Brain Keeper is a background service, and skills like the morning brief are the apps. Your agent is the part that does the work, and you're the user.

### What's a "second brain"?

A place outside your head where you keep what you know, what you're working on and what you decided, so you can find it later. Phygital Brain is a second brain that your agent can read and write, so you don't have to keep it in order yourself.

### Is it an app?

No. There's nothing to run. Phygital Brain is a set of instructions and templates. Your AI agent follows them to build the folder and look after it.

### Who is it for?

Anyone who works with other people, juggles projects or wants their agent to know them: freelancers, small business owners, people with a job, students, and people with personal projects. The setup asks what you do and builds only the parts you need.

### What does it look like?

A folder with seven folders inside (`About`, `Daily`, `Projects`, `Relationships`, `Memory`, `Library`, `Skills`) and a rule file at the top. Each note is a plain text file. In [Baalda](https://github.com/naveedharri/baalda) you see them as linked pages. See [The folders in your brain](folders/README.md).

## Before you start

### What do I need?

An AI agent that can work in a folder on your computer, a cloud drive your agent can connect to, and a computer. We recommend the Claude desktop app with a paid plan and Google Drive, because that's the pair we tested most. Baalda is part of the setup too, for browsing your notes.

### Do I need to know how to code?

No. You install a few apps, answer four forms and talk in plain words. The only lines that look like code are the two install lines for Claude Code, and you can paste them.

### How long does it take?

About 20 minutes the first time: 10 to get the apps ready and 10 for the setup forms.

### Does it work on Windows?

Yes. It works on Mac and Windows, as long as your agent and your cloud drive have desktop apps there.

### Does it work on Linux?

It can, if your agent and your cloud drive run on Linux. We haven't tested it there.

### Can I use a folder I already have, full of notes?

The setup needs an empty folder, or one without its own rule file. If the folder has other files, the setup leaves them alone and builds around them. To bring old notes in, drop them in form 4, and your agent offers to file them after the build.

## Agents

### Which AI agents does it work with?

Any agent that can read, edit and create files in a folder on your computer. Claude (the desktop app and Claude Code) is what we use and recommend. Codex and similar agents work too. See [Other agents](other-agents.md).

### Why do you recommend Claude?

The setup was built and tested there. It's the only one that shows the setup as form windows with clicks and file drops, it can schedule the Brain Keeper and the morning brief, and with Dispatch you can send it tasks from your phone.

### Does it work with ChatGPT?

The ChatGPT app in a browser can't save files in a folder on your computer, so it can't build or tidy your brain. If it can connect to your cloud drive, it can read your notes. An OpenAI agent that works in a folder, like Codex, can build and use it.

### What's different with another agent?

The questions come in chat instead of form windows, and the Brain Keeper runs only if the app can schedule tasks. Otherwise you say "run the brain keeper" once a day. Everything else is the same, because the rules are plain text files.

### Why are the rule files called CLAUDE.md?

Because most people use Claude. Agents that look for another name, like `AGENTS.md` in Codex or `GEMINI.md` in Gemini CLI, get a one-line file next to each `CLAUDE.md` that points to it. There's still only one set of rules.

### Can I use two agents on the same brain?

Yes. They read the same rules, so they file things the same way. Don't let both write at the same time, and let only one run the Brain Keeper.

## Cloud drives

### Which cloud drives work?

Any drive that keeps a copy of the folder on your computer, and that your agent can connect to so it can read, edit and create files there. Google Drive, Nextcloud, Dropbox and OneDrive are common choices. Check your agent's list of connectors before you choose.

### How does my agent connect to a drive?

Through a connector or an MCP server, a small add-on that lets an agent use another app. Claude has a built-in Google Drive connector. Nextcloud usually connects through an MCP server. For other drives, check what your agent offers.

### Can I use Nextcloud?

Yes. Install the Nextcloud desktop app so the folder syncs to your computer, and connect Nextcloud to your agent through an MCP server. Nextcloud can also run on your own server, so your notes don't sit with a big company.

### Can I use iCloud?

On your computer, yes: an iCloud Drive folder syncs like any other. Reaching it from your agent's phone app depends on whether your agent can connect to iCloud, so check that first.

### Do I need a cloud drive at all?

No, but you lose two things: a backup in the cloud, and using your brain from your phone. If you say no during the setup, the brain stays on one computer. You can move it into a drive later.

### Why should the folder be kept on my computer and not only in the cloud?

Your agent reads the files on your computer. If they only live in the cloud, it may not be able to open them quickly, or at all, while you're offline. Look for "mirror", "available offline" or "always keep on this device" in your drive's settings.

### Can I move my brain to another drive later?

Yes. Move the whole folder, then open it in your agent from the new place. Links between notes use note names, not folder paths, so they keep working.

## The setup

### What does the setup ask?

Four forms. About you: your name, what you do, strengths, values, how you like to work. Your work: three questions written for your job, then customers or interests, your goal, projects and what's worrying you. Your days and people: work days, morning brief time, key people, social media and tools. Files: anything your agent should read first.

### Do I have to answer everything?

No. You can skip any question, or a whole form. Skipped answers mean fewer pages at the start. You can add things later by telling your agent.

### What are the three questions about my job?

Your agent writes them from what you said you do in form 1. An illustrator gets asked what kind of illustration they do, who they've worked with and how they charge. Someone with personal projects gets asked about those projects instead.

### What should I drop in form 4?

Your CV, a bio or About page, a price list, a portfolio link, a project brief, or exports of old notes. Your agent reads them to fill in your pages, so you type less.

### What if I don't sell anything?

The setup skips the business questions and builds no business, services or customer pages, and no client folder. It asks about the areas of your life that matter instead.

### Can I redo the setup?

Yes. Say "Update my answers." The forms open again, and your About pages are refreshed. Your other notes stay as they are.

## Every day

### How do I use it?

Open a chat on your brain folder and talk normally. "I had a call with Marta, we moved the deadline." "New project: a website for my studio." "Write a reply to this email." Your agent files what you say in the right place and links it.

### Do I have to tell it where to save things?

No. The rules say where each kind of information goes. If something doesn't fit anywhere, your agent asks.

### Will it change my notes without asking?

It saves small updates to notes that already exist (a date, a fact, a status) and tells you in one line. It asks first before it makes a new note or folder, rewrites a note, or moves, renames or deletes anything.

### How does it know about me in a new chat?

At the start of every chat it reads your newest daily note, `About/me.md` and your open tasks. It doesn't announce that it did.

### What if it gets something wrong?

Tell it: "Don't do that, do this instead." It saves your correction as a new rule, in your words, and follows it from then on.

### Can I write notes myself?

Yes. They're plain text files. Write in Baalda or any text editor. The Brain Keeper adds a missing info block (the few lines at the top of each note) the next time it passes by.

### What's an info block?

The few lines between `---` marks at the top of each note, like `status: active` and `tags: [...]`. They help your agent find and sort notes. They stay in English in every language.

### Where do my tasks go?

Tasks for a project go on that project's front page. Other tasks go in `Daily/tasks.md`, with the date you added them.

### Can it write emails and posts for me?

Yes, if you picked "Write for me" in the setup. It writes in the voice saved in `About/brand.md`. For writing other people will read, it shows you the AI-sounding bits it found and lets you choose before changing them. It drafts. You send.

## The Brain Keeper and the morning brief

### What does the Brain Keeper do?

Every work day it makes tomorrow's daily note, closes old ones, lists open decisions in today's note, puts tasks open for over 30 days on your list, looks at one folder for problems, fixes up to 5 small things and writes a report. Things only you can decide go in `Skills/brain-keeper/queue.md`. See [Skills](folders/skills.md).

### Can the Brain Keeper delete my notes?

No. It never deletes, moves or renames your notes. The only thing it deletes is its own reports after 60 days.

### When does it run?

One hour before your morning brief, or at 8:00 on your work days if you have no brief. You can change it: "Run the Brain Keeper at 7 instead."

### Why didn't it run?

Scheduled tasks run only while your agent's app is open and your computer is awake. Say "run the brain keeper" to run it now.

### What's the check-up?

The Brain Keeper's other mode. Say "check up my brain" and your agent looks at the whole brain, lists every problem with a suggested fix, and changes nothing until you say yes.

### Can I pause it?

Yes. Say "pause the brain keeper" and later "resume the brain keeper".

### What's in the morning brief?

Six short lines at most: your three most important things today, what you're waiting on from others, one decision to make, and today's events if a calendar is connected. It doesn't write any file.

## Your phone

### Can I use my brain on my phone?

Yes, if your brain is in a cloud drive. Ask things from your agent's phone app with the drive connected. To add things, send a task to your agent on your computer (in Claude, with Dispatch). See [Your brain on your phone](phone.md).

### Can I add notes from my phone?

Yes, through a task sent to your computer, which files it with all the rules. Some connectors can also edit files straight from the phone, but a phone chat doesn't load the brain's rules by itself, so things may land in the wrong place.

### Does my computer need to be on?

To read, no: your agent reads straight from the drive. To add or change things through your computer, yes, and your agent's app must be open.

### Do I need Baalda on my phone?

No. Baalda is for browsing on your computer. On your phone, your drive's app opens notes as plain text.

## Privacy and safety

### Who can see my notes?

The company that runs your AI sees what your agent reads. Your cloud drive's provider stores your files. Phygital Brain itself sees nothing: it has no server and collects nothing. See [What you share with your AI](../SECURITY.md#what-you-share-with-your-ai).

### Will my notes be used to train AI?

That depends on your AI company, your plan and your settings. Some may use chats to train their models. Look for a setting about using your data to improve their models, and choose what you're comfortable with.

### What shouldn't I put in my brain?

Passwords, keys, health records, other people's ID numbers, and anything you've promised to keep secret. Use a password manager for passwords.

### How are private details handled?

Tax IDs, bank details, card numbers, your full legal name and your birth date live only in the one note that needs them. Your agent never copies them into other notes and never repeats them in a reply. At most it shows the last 4 digits.

### What's .claudeignore?

A list of files and folders your agent must not open unless you ask for that exact file: password and key files, and `Memory/finances/`. You can add your own private folders. It's a rule your agent follows, so it doesn't lock anything. Keep truly secret things outside the brain folder.

### Can I keep notes about clients?

Yes, but their details are your responsibility. Keep only what you need, and follow the privacy laws where you live and work. Phone numbers, emails and addresses stay only in that person's note.

### Can I use it for my job?

Check your company's rules first. Many don't allow work information in a personal AI or a personal cloud drive.

### Can a file I drop in make my agent misbehave?

It can happen with any AI agent: a file, email or web page can hide text that tries to give your agent orders. Only drop in files and links you trust, and watch what your agent does after reading something from outside. If a file ever makes it break the brain's rules, report it as [SECURITY.md](../SECURITY.md) explains.

## Languages

### Does it work in my language?

Yes. The setup asks which language your brain should speak first. The forms, messages and notes follow it. See [Languages](../languages/README.md).

### Why are folder names in English?

So the rules work the same in every language. Folder names, file names, links to files and info block words stay in English. Everything you read is in your language.

### Can I change the language later?

Yes. Tell your agent: "From now on, write in Spanish." It asks first, then updates the Language section of your main rules. Notes already written stay in their language.

## Changing it

### Can I add my own folders?

Yes. Ask: "I want a place for my students." Your agent suggests where it fits, asks first, and adds it to the rules.

### Can I add my own rules?

Yes. Say "Add a rule: never book calls on Fridays." Your rules live at the bottom of the main rule file, and upgrades never change them.

### Can I change how the Brain Keeper works?

Yes. Ask in chat, for example "Let the Brain Keeper fix 10 things a day" or "Only report, don't fix anything."

### Can I rename the folders?

You can, but your agent asks first, checks every note that mentions the old name, and updates the rules. Renaming is the change most likely to break things, so do it rarely.

## Updating and leaving

### How do I update?

Update the plugin (in Claude Code, `/plugin marketplace update phygital-brain`; with another agent, download the new version), then say "Upgrade my second brain." Your agent shows what's new and asks first.

### Will an update change my notes?

No. Upgrades add new rules and sections. Your notes, your own rules (word for word) and your own folders stay as they are.

### How do I stop using it?

Uninstall the plugin. Your brain is plain text files in your own cloud drive, and any app that reads Markdown can open it.

### Can I export my notes?

They're already plain files. Copy the folder anywhere.

## Cost and licence

### What does it cost?

Phygital Brain is free and open source. You pay for your AI agent (we recommend a paid Claude plan) and, if you need more than the free space, your cloud drive.

### Can I use it for my business?

Yes. The Apache License 2.0 lets you use it, change it and use it at work.

### Can I sell it, or a setup service built on it?

You can use and change the code and text under the licence, and say your work is "built on Phygital Brain". You can't sell it under the Phygital Brain name or logo. See [TRADEMARKS.md](../TRADEMARKS.md).

### Can I help?

Yes. Bug reports, better questions, clearer docs and translations are all welcome. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Problems

### The form window doesn't open.

Your app can't show form windows. Your agent asks the same questions in chat instead.

### My agent says it can't write to the folder.

Pick your brain folder again when you start the task, and check that your drive's app is running.

### A link is broken.

Right after a sync, wait a few minutes: the note is usually still on its way. Your agent never fixes a broken link by making a blank note, because that could overwrite the real one.

### A note shows up twice.

Your drive made a copy, often ending in `(1)` or "conflicted copy", because the note changed in two places at once. Ask your agent: "Merge these two notes."

### My agent forgot something.

Check that you're in a chat on your brain folder. Your agent only knows your brain there. If the fact should be permanent, tell it, and it saves it in the right note.

More fixes are in [Getting started](getting-started.md#if-something-goes-wrong) and [Your brain on your phone](phone.md#if-something-goes-wrong).
