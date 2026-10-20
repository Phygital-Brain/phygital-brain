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

**3. Connect Google Drive.** In Settings, open Connectors, tap Google Drive, then Connect, and sign in with your Google account. Allow what it asks. Using Dropbox, OneDrive or Nextcloud instead? Connect it the same way. No drive yet, or stuck? Skip this step: your agent helps you during the setup.

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

1. **You can read the setup:** you could read `SKILL.md`. If you can't open web pages, ask them to turn on web search, and wait.

Then follow `SKILL.md` from Step 0: the language, the welcome, then the cloud drive in Step 1.6, "On a phone". It helps them connect Google Drive or another drive if it isn't connected yet. When the drive is connected, do the folder check:

2. **The folder:** create a folder called `My Brain` in the root of their drive (ask them first; if a `My Brain` folder already exists, follow `SKILL.md` Step 0.2 on it). Save a small test file in it, read it back, then delete it. If you can't save files, ask them to turn on code execution and file creation (step 2 above), then try again.

`My Brain` is the selected folder for the whole setup. Every path in `SKILL.md` (`About/me.md`, `Daily/...`) is inside it.

### 3. What changes from `SKILL.md`

- **Step 1.6:** use its "On a phone" part: no "later", because the brain needs the drive.
- **Forms and windows:** on a phone, never use form windows, even if you have the tool (in Claude, `show_widget`): they don't work well there. Ask the language question, the welcome and the forms as click questions, and use `forms/questions.md` for the four forms. For a ready language, take the same questions and options from that language's forms in `i18n/{code}/forms/`, so they're already translated. Ask them as click questions where you have them, numbered options in chat where you don't. Keep answers short, because typing on a phone is slow.
- **Form 4 (files):** they can attach photos, screenshots or files from their phone in this chat, or paste links. Read them as `SKILL.md` says.
- **Files:** save every note as plain text Markdown (`.md`), never as a Google Doc or a Word file. Keep the exact file names, including `CLAUDE.md` and `.claudeignore`. Create each folder before the files inside it. Copy `bundled/no-ai-slop/` unchanged.
- **3.8 Brain Keeper:** there's no computer, so no computer schedule. If you can create cloud routines (in Claude: routines), set up the Brain Keeper in the cloud: follow `skills/brain-keeper/SKILL.md` Step 3, "In the cloud", without asking "on this computer or in the cloud". If you can't, skip the schedule, and in the finish message tell them to say "run the brain keeper" once a day and "check up my brain" now and then. Do the same for the morning brief.
- **3.9 Check your work:** list the `My Brain` folder and its subfolders through the connector, and open a few files to check them.

### 4. The finish message

Use `SKILL.md` Step 4, with these changes:

- Item 4: "Start a new chat, check your drive's connector is on, and talk to me the way you'd talk to a friend."
- Item 5: the brain is in their drive, so say `finish_cloud_on`.
- Skip Step 4.1 (Baalda): it's a computer app.
- Add the instructions text (`SKILL.md`, "The instructions text"), with one more sentence first, in their language: "My second brain is the My Brain folder in my {drive}. At the start of every chat, read My Brain/CLAUDE.md through the {drive} connector and follow it." (with their drive's name) Tell them where to paste it: in the Claude app, Settings, then the personal instructions box. Without it, a new chat won't know the brain is there.
- Add one line: "To read your notes yourself, open the {drive} app, then My Brain."

Then stop.
