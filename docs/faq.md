# FAQ

Questions people ask about Phygital Brain, grouped by topic. Click a question to see the answer. If yours isn't here, open an issue with the **Question** form. For a word you don't know, see the [Glossary](glossary.md).

**On this page:** [The basics](#the-basics) · [Before you start](#before-you-start) · [Agents](#agents) · [Cloud drives](#cloud-drives) · [The setup](#the-setup) · [Every day](#every-day) · [The Brain Keeper and the morning brief](#the-brain-keeper-and-the-morning-brief) · [Your phone](#your-phone) · [Privacy and safety](#privacy-and-safety) · [Languages](#languages) · [Changing it](#changing-it) · [Updating and leaving](#updating-and-leaving) · [Cost and licence](#cost-and-licence) · [Problems](#problems)

## The basics

<details>
<summary><b>What is Phygital Brain?</b></summary>

An OS (operating system) for your notes and your AI agent. It builds one folder in your cloud drive with three kinds of things: rule files that tell your agent where everything goes, notes your agent writes as you talk, and the Brain Keeper, which tidies the folder every work day. See [How it works](how-it-works.md).
</details>

<details>
<summary><b>Why call it an operating system?</b></summary>

Because each part does a job an operating system does. The rule files are the system rules, the folders are the file system, `About/me.md` holds your settings, the Brain Keeper is a background service, and skills like the morning brief are the apps. Your agent is the part that does the work, and you're the user.
</details>

<details>
<summary><b>What's a "second brain"?</b></summary>

A place outside your head where you keep what you know, what you're working on and what you decided, so you can find it later. Phygital Brain is a second brain that your agent can read and write, so you don't have to keep it in order yourself.
</details>

<details>
<summary><b>Is it an app?</b></summary>

No. There's nothing to run. Phygital Brain is a set of instructions and templates. Your AI agent follows them to build the folder and look after it.
</details>

<details>
<summary><b>Which skills come with it?</b></summary>

Three go into your brain: the Brain Keeper (the daily tidy and the check-up), the morning brief (if you want one), and the [no-ai-slop](https://github.com/petergyang/no-ai-slop) skill by Peter Yang for the Writing Check. The main rules also include work habits adapted from Andrej Karpathy's guidelines for AI assistants ([andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)). You can add more skills in `Skills/`.
</details>

<details>
<summary><b>Who is it for?</b></summary>

Anyone who works with other people, juggles projects or wants their agent to know them: freelancers, small business owners, people with a job, students, and people with personal projects. The setup asks what you do and builds only the parts you need. See [Use cases](use-cases.md) for five examples.
</details>

<details>
<summary><b>Will it replace Notion?</b></summary>

For knowledge in words, it can: notes about people, projects, decisions and how you work. For structured data you sort and filter, like a sales pipeline or a content calendar with many fields, keep Notion or a spreadsheet. Many people use both.
</details>

<details>
<summary><b>Is there a demo?</b></summary>

There's an [example brain](example-brain/README.md) in this repository: a few made-up notes for Ana, the illustrator from the use cases, so you can see what the files look like before you set one up.
</details>

<details>
<summary><b>What does it look like?</b></summary>

A folder with seven folders inside (`About`, `Daily`, `Projects`, `Relationships`, `Memory`, `Library`, `Skills`) and a rule file at the top. Each note is a plain text file. In [Baalda](https://github.com/naveedharri/baalda) you see them as linked pages. See [The folders in your brain](folders/README.md).
</details>

## Before you start

<details>
<summary><b>What do I need?</b></summary>

An AI agent that can work in a folder on your computer, a cloud drive your agent can connect to, and a computer. We recommend the Claude desktop app with a paid plan and Google Drive, because that's the pair we tested most. Baalda is part of the setup too, for browsing your notes.
</details>

<details>
<summary><b>Do I need to know how to code?</b></summary>

No. You install a few apps, answer four forms and talk in plain words. The only lines that look like code are the two install lines for Claude Code, and you can paste them.
</details>

<details>
<summary><b>How long does it take?</b></summary>

About 20 minutes the first time: 10 to get the apps ready and 10 for the setup forms.
</details>

<details>
<summary><b>Does it work on Windows?</b></summary>

Yes. It works on Mac and Windows, as long as your agent and your cloud drive have desktop apps there.
</details>

<details>
<summary><b>Does it work on Linux?</b></summary>

It can, if your agent and your cloud drive run on Linux. We haven't tested it there.
</details>

<details>
<summary><b>Can I use a folder I already have, full of notes?</b></summary>

The setup needs an empty folder, or one without its own rule file. If the folder has other files, the setup leaves them alone and builds around them. To bring old notes in, drop them in form 4, and your agent offers to file them after the build. Or do it any time later: see [Bringing in your old notes](importing.md).
</details>

## Agents

<details>
<summary><b>Which AI agents does it work with?</b></summary>

Any agent that can read, edit and create files in a folder on your computer. Claude (the desktop app and Claude Code) is what we use and recommend. Codex, Hermes Agent, OpenClaw and similar agents work too. See [Other agents](other-agents.md).
</details>

<details>
<summary><b>Why do you recommend Claude?</b></summary>

The setup was built and tested there. It's the only one that shows the setup as form windows with clicks and file drops, it can schedule the Brain Keeper and the morning brief, and with Dispatch you can send it tasks from your phone.
</details>

<details>
<summary><b>Does it work with ChatGPT?</b></summary>

The ChatGPT app in a browser can't save files in a folder on your computer, so it can't build or tidy your brain. If it can connect to your cloud drive, it can read your notes. An OpenAI agent that works in a folder, like Codex, can build and use it.
</details>

<details>
<summary><b>What's different with another agent?</b></summary>

The questions come in chat instead of form windows, and the Brain Keeper runs only if the app can schedule tasks. Otherwise you say "run the brain keeper" once a day. Everything else is the same, because the rules are plain text files.
</details>

<details>
<summary><b>Why are the rule files called CLAUDE.md?</b></summary>

Because most people use Claude. Agents that look for another name, like `AGENTS.md` in Codex or `GEMINI.md` in Gemini CLI, get a one-line file next to each `CLAUDE.md` that points to it. There's still only one set of rules.
</details>

<details>
<summary><b>Can I use another notes app instead of Baalda?</b></summary>

Yes. Your notes are plain Markdown files, so any app that opens a folder of Markdown works, like Obsidian or a plain text editor. Baalda is the one the setup suggests.
</details>

<details>
<summary><b>Can I use two agents on the same brain?</b></summary>

Yes. They read the same rules, so they file things the same way. Don't let both write at the same time, and let only one run the Brain Keeper.
</details>

## Cloud drives

<details>
<summary><b>Which cloud drives work?</b></summary>

Any drive that keeps a copy of the folder on your computer, and that your agent can connect to so it can read, edit and create files there. Google Drive, Nextcloud, Dropbox and OneDrive are common choices. Check your agent's list of connectors before you choose.
</details>

<details>
<summary><b>How does my agent connect to a drive?</b></summary>

Through a connector or an MCP server, a small add-on that lets an agent use another app. Claude has a built-in Google Drive connector. Nextcloud usually connects through an MCP server. For other drives, check what your agent offers.
</details>

<details>
<summary><b>Can I use Nextcloud?</b></summary>

Yes. Install the Nextcloud desktop app so the folder syncs to your computer, and connect Nextcloud to your agent through an MCP server. Nextcloud can also run on your own server, so your notes don't sit with a big company.
</details>

<details>
<summary><b>Can it read my email and calendar?</b></summary>

Yes, read only, if you connect them to your agent. The Brain Keeper notes yesterday's emails with people you have notes on, and tomorrow's meetings. It never sends, deletes or changes anything in your apps. See [Connect your apps](connect-your-apps.md).
</details>

<details>
<summary><b>Can the brain live in more than one drive?</b></summary>

Yes. A team can keep it in Baalda's cloud for real-time sync and also in a drive like Google Drive for phones and cloud routines. Pick one as the main one for edits, and test the second one first: two sync services on one folder can make duplicate copies. See [Teams](teams.md).
</details>

<details>
<summary><b>Can I use iCloud?</b></summary>

On your computer, yes: an iCloud Drive folder syncs like any other. Reaching it from your agent's phone app depends on whether your agent can connect to iCloud, so check that first.
</details>

<details>
<summary><b>Do I need a cloud drive at all?</b></summary>

No, but you lose two things: a backup in the cloud, and using your brain from your phone. If you say no during the setup, the brain stays on one computer. You can move it into a drive later.
</details>

<details>
<summary><b>Why should the folder be kept on my computer and not only in the cloud?</b></summary>

Your agent reads the files on your computer. If they only live in the cloud, it may not be able to open them quickly, or at all, while you're offline. Look for "mirror", "available offline" or "always keep on this device" in your drive's settings.
</details>

<details>
<summary><b>Can I move my brain to another drive later?</b></summary>

Yes. Move the whole folder, then open it in your agent from the new place. Links between notes use note names, not folder paths, so they keep working.
</details>

## The setup

<details>
<summary><b>What does the setup ask?</b></summary>

Four forms. About you: your name, what you do, strengths, values, how you like to work. Your work: three questions written for your job, then customers or interests, your goal, projects and what's worrying you. Your days and people: work days, morning brief time, key people, social media and tools. Files: anything your agent should read first.
</details>

<details>
<summary><b>Does the setup use a lot of my AI plan?</b></summary>

More than a normal chat, because it writes your whole brain in one go. Do it when you're not close to your plan's limit. After the setup, daily use is like any other chat.
</details>

<details>
<summary><b>Do I have to answer everything?</b></summary>

No. You can skip any question, or a whole form. Skipped answers mean fewer pages at the start. You can add things later by telling your agent.
</details>

<details>
<summary><b>What are the three questions about my job?</b></summary>

Your agent writes them from what you said you do in form 1. An illustrator gets asked what kind of illustration they do, who they've worked with and how they charge. Someone with personal projects gets asked about those projects instead.
</details>

<details>
<summary><b>What should I drop in form 4?</b></summary>

Your CV, a bio or About page, a price list, a portfolio link, a project brief, or exports of old notes. Your agent reads them to fill in your pages, so you type less.
</details>

<details>
<summary><b>What if I don't sell anything?</b></summary>

The setup skips the business questions and builds no business, services or customer pages, and no client folder. It asks about the areas of your life that matter instead.
</details>

<details>
<summary><b>Can I redo the setup?</b></summary>

Yes. Say "Update my answers." The forms open again, and your About pages are refreshed. Your other notes stay as they are.
</details>

## Every day

<details>
<summary><b>How do I use it?</b></summary>

Open a chat on your brain folder and talk normally. "I had a call with Marta, we moved the deadline." "New project: a website for my studio." "Write a reply to this email." Your agent files what you say in the right place and links it.
</details>

<details>
<summary><b>Do I have to tell it where to save things?</b></summary>

No. The rules say where each kind of information goes. If something doesn't fit anywhere, your agent asks.
</details>

<details>
<summary><b>Will it change my notes without asking?</b></summary>

It saves small updates to notes that already exist (a date, a fact, a status) and tells you in one line. It asks first before it makes a new note or folder, rewrites a note, or moves, renames or deletes anything.
</details>

<details>
<summary><b>How does it know about me in a new chat?</b></summary>

At the start of every chat it reads your newest daily note, `About/me.md` and your open tasks. It doesn't announce that it did.
</details>

<details>
<summary><b>What if it gets something wrong?</b></summary>

Tell it: "Don't do that, do this instead." It saves your correction as a new rule, in your words, and follows it from then on.
</details>

<details>
<summary><b>Can I write notes myself?</b></summary>

Yes. They're plain text files. Write in Baalda or any text editor. The Brain Keeper adds a missing info block (the few lines at the top of each note) the next time it passes by.
</details>

<details>
<summary><b>What's an info block?</b></summary>

The few lines between `---` marks at the top of each note, like `status: active` and `tags: [...]`. They help your agent find and sort notes. They stay in English in every language.
</details>

<details>
<summary><b>Where do my tasks go?</b></summary>

Tasks for a project go on that project's front page. Other tasks go in `Daily/tasks.md`, with the date you added them.
</details>

<details>
<summary><b>Can it prepare me for a meeting?</b></summary>

Yes. Say "prep me for Marta" or, with a connected calendar, "prep me for my next meeting". You get eight short lines from your notes: who they are, when you last talked, what's going on, what was agreed, and what to bring up.
</details>

<details>
<summary><b>Can it help me think, not only store notes?</b></summary>

Yes. Say "challenge my idea: ..." for points for and against from your own notes, "what patterns do you see?" for what keeps coming up in the last 30 days, or "find contradictions" for notes that disagree. See [Skills](folders/skills.md#thinking-thinking-tools).
</details>

<details>
<summary><b>Can I undo a change?</b></summary>

Yes. Before a big change, like an import, check-up fixes, a move or a delete, your agent copies the files into a hidden `.backups/` folder. Say "undo the last change" within 10 days. Your cloud drive's version history is a second safety net.
</details>

<details>
<summary><b>Can it write emails and posts for me?</b></summary>

Yes, if you picked "Write for me" in the setup. It writes in the voice saved in `About/brand.md`. For writing other people will read, it shows you the AI-sounding bits it found and lets you choose before changing them. It drafts. You send. The check uses the no-ai-slop skill, which every brain gets in `Skills/no-ai-slop/`.
</details>

## The Brain Keeper and the morning brief

<details>
<summary><b>What does the Brain Keeper do?</b></summary>

Every work day it makes tomorrow's daily note, closes old ones, lists open decisions in today's note, puts tasks open for over 30 days on your list, looks at one folder for problems, fixes up to 5 small things and writes a report. Things only you can decide go in `Skills/brain-keeper/queue.md`. See [Skills](folders/skills.md).
</details>

<details>
<summary><b>Can the Brain Keeper delete my notes?</b></summary>

No. It never deletes, moves or renames your notes. The only thing it deletes is its own reports after 60 days.
</details>

<details>
<summary><b>When does it run?</b></summary>

One hour before your morning brief, or at 8:00 on your work days if you have no brief. You can change it: "Run the Brain Keeper at 7 instead."
</details>

<details>
<summary><b>Why didn't it run?</b></summary>

Scheduled tasks run only while your agent's app is open and your computer is awake. Say "run the brain keeper" to run it now.
</details>

<details>
<summary><b>Can it run while my laptop is closed?</b></summary>

Yes, as a cloud routine (in Claude: routines), if your brain is in a cloud drive that connects to your agent in the cloud, like Google Drive. Say "Run the Brain Keeper in the cloud." Your agent checks the connector can read and write your notes first. See [Running in the cloud](folders/skills.md#running-in-the-cloud).
</details>

<details>
<summary><b>What's the check-up?</b></summary>

The Brain Keeper's other mode. Say "check up my brain" and your agent looks at the whole brain, lists every problem with a suggested fix, and changes nothing until you say yes.
</details>

<details>
<summary><b>Can I pause it?</b></summary>

Yes. Say "pause the brain keeper" and later "resume the brain keeper".
</details>

<details>
<summary><b>What's in the morning brief?</b></summary>

Six short lines at most: your three most important things today, what you're waiting on from others, one decision to make, and today's events if a calendar is connected. It doesn't write any file.
</details>

## Your phone

<details>
<summary><b>Can I use my brain on my phone?</b></summary>

Yes, if your brain is in a cloud drive. Ask things from your agent's phone app with the drive connected. To add things, send a task to your agent on your computer (in Claude, with Dispatch). See [Your brain on your phone](phone.md).
</details>

<details>
<summary><b>Can I add notes from my phone?</b></summary>

Yes, through a task sent to your computer, which files it with all the rules. Some connectors can also edit files straight from the phone, but a phone chat doesn't load the brain's rules by itself, so things may land in the wrong place.
</details>

<details>
<summary><b>Does my computer need to be on?</b></summary>

To read, no: your agent reads straight from the drive. To add or change things through your computer, yes, and your agent's app must be open.
</details>

<details>
<summary><b>Do I need Baalda on my phone?</b></summary>

No. Baalda is for browsing on your computer. On your phone, your drive's app opens notes as plain text.
</details>

## Privacy and safety

<details>
<summary><b>Who can see my notes?</b></summary>

The company that runs your AI sees what your agent reads. Your cloud drive's provider stores your files. Phygital Brain itself sees nothing: it has no server and collects nothing. See [What you share with your AI](../SECURITY.md#what-you-share-with-your-ai).
</details>

<details>
<summary><b>Will my notes be used to train AI?</b></summary>

That depends on your AI company, your plan and your settings. Some may use chats to train their models. Look for a setting about using your data to improve their models, and choose what you're comfortable with.
</details>

<details>
<summary><b>What shouldn't I put in my brain?</b></summary>

Passwords, keys, health records, other people's ID numbers, and anything you've promised to keep secret. Use a password manager for passwords.
</details>

<details>
<summary><b>How are private details handled?</b></summary>

Tax IDs, bank details, card numbers, your full legal name and your birth date live only in the one note that needs them. Your agent never copies them into other notes and never repeats them in a reply. At most it shows the last 4 digits.
</details>

<details>
<summary><b>What's .claudeignore?</b></summary>

A list of files and folders your agent must not open unless you ask for that exact file: password and key files, and `Memory/finances/`. You can add your own private folders. It's a rule your agent follows, so it doesn't lock anything. Keep truly secret things outside the brain folder.
</details>

<details>
<summary><b>Can my team use one brain?</b></summary>

Yes, through Baalda's cloud, which is paid. It syncs everyone's copy in real time, and folder permissions are set in Baalda. Then say "Set up my team" and your agent adds a Team section to the rules, with each person's role and daily notes. See [Teams](teams.md).
</details>

<details>
<summary><b>Can I keep notes about clients?</b></summary>

Yes, but their details are your responsibility. Keep only what you need, and follow the privacy laws where you live and work. Phone numbers, emails and addresses stay only in that person's note.
</details>

<details>
<summary><b>Can I use it for my job?</b></summary>

Check your company's rules first. Many don't allow work information in a personal AI or a personal cloud drive.
</details>

<details>
<summary><b>Can a file I drop in make my agent misbehave?</b></summary>

It can happen with any AI agent: a file, email or web page can hide text that tries to give your agent orders. Only drop in files and links you trust, and watch what your agent does after reading something from outside. If a file ever makes it break the brain's rules, report it as [SECURITY.md](../SECURITY.md) explains.
</details>

## Languages

<details>
<summary><b>Does it work in my language?</b></summary>

Yes. The setup asks which language your brain should speak first. The forms, messages and notes follow it. See [Languages](../languages/README.md).
</details>

<details>
<summary><b>Are the folder names in my language?</b></summary>

Yes. Folders and notes get names in your language, like `Sobre/` instead of `About/`. If your language isn't one of the 21 ready ones, your agent picks the names during the setup. A few things stay in English so every agent reads them the same way: the `CLAUDE.md` and `README.md` file names, and the info block words at the top of each note, like `status: active`.
</details>

<details>
<summary><b>Can I change the language later?</b></summary>

Yes. Tell your agent: "From now on, write in Spanish." It asks first, then updates the Language section of your main rules. Notes already written stay in their language.
</details>

## Changing it

<details>
<summary><b>Can I add my own folders?</b></summary>

Yes. Ask: "I want a place for my students." Your agent suggests where it fits, asks first, and adds it to the rules.
</details>

<details>
<summary><b>Can I add my own rules?</b></summary>

Yes. Say "Add a rule: never book calls on Fridays." Your rules live at the bottom of the main rule file, and upgrades never change them.
</details>

<details>
<summary><b>Can I add other skills, like making videos or editing images?</b></summary>

Yes. Install the skill in your agent, then say "Add it to my brain". Your agent writes a short notes file telling the skill what to read in your brain and where to save its work. For videos, [HyperFrames](https://github.com/heygen-com/hyperframes) and its Keyframes editor work well. For images, [PhotoCraft](https://github.com/storytold/photocraft), an open-source editor similar to Photoshop. Both are in [Add more skills](add-skills.md).
</details>

<details>
<summary><b>Can I change how the Brain Keeper works?</b></summary>

Yes. Ask in chat, for example "Let the Brain Keeper fix 10 things a day" or "Only report, don't fix anything."
</details>

<details>
<summary><b>Can I rename the folders?</b></summary>

You can, but your agent asks first, checks every note that mentions the old name, and updates the rules. Renaming is the change most likely to break things, so do it rarely.
</details>

## Updating and leaving

<details>
<summary><b>How do I update?</b></summary>

Update the plugin (in Claude Code, `/plugin marketplace update phygital-brain`; with another agent, download the new version), then say "Upgrade my second brain." Your agent shows what's new and asks first.
</details>

<details>
<summary><b>Will an update change my notes?</b></summary>

No. Upgrades add new rules and sections. Your notes, your own rules (word for word) and your own folders stay as they are.
</details>

<details>
<summary><b>How do I stop using it?</b></summary>

Uninstall the plugin. Your brain is plain text files in your own cloud drive, and any app that reads Markdown can open it.
</details>

<details>
<summary><b>Can I export my notes?</b></summary>

They're already plain files. Copy the folder anywhere.
</details>

## Cost and licence

<details>
<summary><b>What does it cost?</b></summary>

Phygital Brain is free and open source. What you might pay for:

| Part | Cost |
|---|---|
| Phygital Brain | Free |
| Your AI agent | A paid plan. Claude's paid plans start at about $20 a month; check the current price on their site |
| Your cloud drive | Most have a free tier, which is enough for a brain of text notes. Nextcloud can run on your own server |
| Baalda | Check the current terms on [its repository](https://github.com/naveedharri/baalda) |

The first setup uses more of your AI plan's usage than a normal chat, because it writes many files at once. After that, daily use is like any other chat, plus a little for the Brain Keeper's daily run.
</details>

<details>
<summary><b>Can I use it for my business?</b></summary>

Yes. The Apache License 2.0 lets you use it, change it and use it at work.
</details>

<details>
<summary><b>Can I sell it, or a setup service built on it?</b></summary>

You can use and change the code and text under the licence, and say your work is "built on Phygital Brain". You can't sell it under the Phygital Brain name or logo. See [TRADEMARKS.md](../TRADEMARKS.md).
</details>

<details>
<summary><b>Can I help?</b></summary>

Yes. Bug reports, better questions, clearer docs and translations are all welcome. See [CONTRIBUTING.md](../CONTRIBUTING.md).
</details>

## Problems

<details>
<summary><b>The form window doesn't open.</b></summary>

Your app can't show form windows. Your agent asks the same questions in chat instead.
</details>

<details>
<summary><b>My agent says it can't write to the folder.</b></summary>

Pick your brain folder again when you start the task, and check that your drive's app is running.
</details>

<details>
<summary><b>A link is broken.</b></summary>

Right after a sync, wait a few minutes: the note is usually still on its way. Your agent never fixes a broken link by making a blank note, because that could overwrite the real one.
</details>

<details>
<summary><b>A note shows up twice.</b></summary>

Your drive made a copy, often ending in `(1)` or "conflicted copy", because the note changed in two places at once. Ask your agent: "Merge these two notes."
</details>

<details>
<summary><b>My agent forgot something.</b></summary>

Check that you're in a chat on your brain folder. Your agent only knows your brain there. If the fact should be permanent, tell it, and it saves it in the right note.
</details>

More fixes are in [Getting started](getting-started.md#if-something-goes-wrong) and [Your brain on your phone](phone.md#if-something-goes-wrong).
