# Phone only: build your brain with just a phone

You can build and use your whole brain from your phone, with no computer. Your agent builds it straight into your Google Drive, through its Google Drive connector (a small add-on that lets it open and save files in your drive).

If you have a computer, set up your brain there with [Getting started](getting-started.md). It's quicker and easier on a big screen. This page is for when you don't have one.

This page has two parts: four steps for you, then instructions for your agent. You only do the four steps. Your agent reads the rest.

The steps use **Claude and Google Drive**. So far we've tested this only with Claude. Another agent may work too, if its phone app can save files in your drive.

## For you: four steps

**1. Get the app.** Download the Claude app from the App Store or Google Play, and sign in. We recommend a paid plan.

**2. Turn on two settings.** In the app, open Settings, then Capabilities (the name can change a little), and turn on:

- **Code execution and file creation.** Your agent needs it to save files in your drive.
- **Web search.** Your agent needs it to read the setup instructions from this page.

**3. Connect Google Drive.** In Settings, open Connectors, tap Google Drive, then Connect, and sign in with your Google account. Allow what it asks.

If it's not in the app, open claude.ai in your phone's browser, sign in, and do the same there. It's the same account.

**4. Start the setup.** Start a new chat. Tap **+**, then Connectors, and make sure Google Drive is on. Then copy this message and send it:

```
Build my second brain on my phone. Read this page and follow the part "For your agent": https://raw.githubusercontent.com/Phygital-Brain/phygital-brain/main/docs/phone-only.md
```

Your agent asks a few short questions (about 10 minutes, mostly taps), then builds a folder called **My Brain** in your Google Drive. Keep the app open until it says it's done.

**After that:** your agent gives you a short text to paste into Settings, in the personal instructions box. From then on, every chat starts by reading your brain. Then talk normally, for example: "I had a call with Marta, the cover is now due on the 15th." More in [Your brain on your phone](phone.md).

## For your agent

You are setting up Phygital Brain for someone who has only a phone. Everything happens in this chat, and every file goes into their Google Drive through the Google Drive connector. Follow the normal setup, with the changes below.

### 1. Get the setup files

The setup lives in this repository: https://github.com/Phygital-Brain/phygital-brain. Read each file you need from `https://raw.githubusercontent.com/Phygital-Brain/phygital-brain/main/` plus its path. Start with `skills/brain-setup/SKILL.md`. It names every other file it uses, by a path relative to its own folder.

If you can run code with internet access, you can download `https://github.com/Phygital-Brain/phygital-brain/archive/refs/heads/main.zip` once and read the files from it instead.

Read only what you need: `SKILL.md`, the forms or `forms/questions.md`, the templates you'll use, `translating.md` only for a language without a ready set, and `skills/brain-keeper/SKILL.md` with its templates.

### 2. Check before you start

Do these checks before the first question. If one fails, tell the person in one plain line what to turn on (from the steps above), and wait.

1. **Drive connector:** you have Google Drive tools in this chat.
2. **You can write:** create a folder called `My Brain` in the root of their drive (ask them first; if a `My Brain` folder already exists, follow `SKILL.md` Step 0.2 on it). Save a small test file in it, read it back, then move it to the trash. If you can't save files, ask them to turn on code execution and file creation (step 2 above), then try again.
3. **You can read the setup:** you could read `SKILL.md`. If you can't open web pages, ask them to turn on web search.

`My Brain` is the selected folder for the whole setup. Every path in `SKILL.md` (`About/me.md`, `Daily/...`) is inside it.

### 3. What changes from `SKILL.md`

- **Step 0.4:** the cloud drive check passes (the brain is in Google Drive), and so does the connector check. Skip Baalda: it's a computer app.
- **Forms:** on a phone, use the form window only if you have one (in Claude, `show_widget`) and it shows well on a small screen. Otherwise use `forms/questions.md` (or `i18n/{code}/forms/questions.md` for a ready language): click questions where you have them, numbered options in chat where you don't. Keep answers short, because typing on a phone is slow.
- **Form 4 (files):** they can attach photos, screenshots or files from their phone in this chat, or paste links. Read them as `SKILL.md` says.
- **Files:** save every note as plain text Markdown (`.md`), never as a Google Doc or a Word file. Keep the exact file names, including `CLAUDE.md` and `.claudeignore`. Create each folder before the files inside it. Copy `bundled/no-ai-slop/` unchanged.
- **3.8 Brain Keeper:** there's no computer, so no computer schedule. If you can create cloud routines (in Claude: routines), set up the Brain Keeper in the cloud: follow `skills/brain-keeper/SKILL.md` Step 3, "In the cloud", without asking "on this computer or in the cloud". If you can't, skip the schedule, and in the finish message tell them to say "run the brain keeper" once a day and "check up my brain" now and then. Do the same for the morning brief.
- **3.9 Check your work:** list the `My Brain` folder and its subfolders through the connector, and open a few files to check them.

### 4. The finish message

Use `SKILL.md` Step 4, with these changes:

- Leave out Baalda (item 2) and the phone item (item 6): they're already on their phone.
- Item 3: "Start a new chat, check Google Drive is on, and talk normally."
- Item 7: the instructions text gets one more sentence, first, in their language: "My second brain is the My Brain folder in my Google Drive. At the start of every chat, read My Brain/CLAUDE.md through the Google Drive connector and follow it." Tell them where to paste it: in the Claude app, Settings, then the personal instructions box.
- Add one line: "To read your notes yourself, open the Google Drive app, then My Brain."

Then stop.
