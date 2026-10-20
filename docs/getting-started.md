# Getting started

About 20 minutes the first time: 10 to get the apps ready, 10 for the setup forms.

## What you need

- A computer (Mac or Windows). The setup runs in the Claude desktop app.
- A paid Claude plan.
- A Google account, for Google Drive.
- A little free space on your computer. A brain is small: plain text files, plus any pictures you add.

You don't need to know any code.

## 1. Claude

1. Download the Claude desktop app from claude.ai/download.
2. Sign in and pick a paid plan.

**Why:** the setup uses the form window, reads and writes files in a folder, and sets up scheduled tasks. These need the desktop app.

## 2. Google Drive

Your brain lives in Google Drive, so it's backed up and you can reach it from anywhere.

1. Install **Google Drive for desktop** and sign in.
2. Open your Google Drive folder on your computer and make a new folder for your brain, for example `My Brain`.
3. Make sure that folder is kept **on your computer**, not only in the cloud. In Google Drive's settings, either choose to mirror your files, or right-click the `My Brain` folder and make it available offline.

**Why step 3 matters:** if the files only live in the cloud, your agent may not be able to open them quickly, or at all, while you're offline.

**Why the folder goes in Drive first:** then you never have to move it later. Moving a brain after it's built can break things.

**Folder name tips:** short and simple. Letters, numbers, spaces and hyphens are fine.

## 3. Attach the folder to Claude

In the Claude app, start a new task and choose the `My Brain` folder. Your agent can now read and write in it.

**Check it worked:** ask "What folder are you in?" Your agent should name `My Brain`.

You'll pick this same folder every time you want to work with your brain.

## 4. Connect Google Drive to Claude

In Claude's settings, under connectors, connect **Google Drive**.

**Why:** then you can read your brain from the Claude website and the phone app too, away from your computer.

The cloud part is done.

## 5. Baalda

Download [Baalda](https://github.com/naveedharri/baalda) and open the same `My Brain` folder. This is where you read and browse your notes: click a `[[link]]` to jump to that note.

You don't have to use Baalda to use your brain. Your agent does the writing. Baalda is for looking around.

## 6. Install Phygital Brain

In Claude Code:

```
/plugin marketplace add Phygital-Brain/phygital-brain
/plugin install phygital-brain@phygital-brain
```

In the Claude desktop app, add `Phygital-Brain/phygital-brain` as a plugin from GitHub in the plugin settings.

**Check it worked:** in a chat, ask "Do you have the Phygital Brain setup?" Your agent should say yes.

## 7. Build your brain

In a chat on your `My Brain` folder, say:

> Set up my second brain.

Here's what happens:

1. **Language.** Your agent asks which language your brain should speak. Everything after this is in that language.
2. **Form 1: About you.** Your name, what you do, your strengths, how you like to work, and more.
3. **Form 2: Your work.** It starts with 3 questions your agent writes just for your kind of work. Then your customers or interests, your goal, your projects and what's worrying you.
4. **Form 3: Your days and people.** Work days, morning brief time, the people who matter, your social media, your tools.
5. **Form 4: Files.** Drop your CV, a bio, a price list or old notes. Or skip it.
6. **Build.** Your agent makes the folders, the rule files, your first notes and the Brain Keeper. This takes a few minutes. You don't need to do anything.
7. **Finish.** One short message: what was built, how to open it, how to use it every day, and a short text for your settings (step 8).

**Tips for the forms:**

- Mostly clicks. Short answers are fine.
- Every choice has an "Other" box to write your own answer.
- You can skip any question. You can add things later just by telling your agent.
- Press Continue and the next form opens. The last one says "Build my brain".
- If the form window doesn't open (some apps can't show it), your agent asks the same questions in chat instead.

## 8. Instructions for every chat

Your brain's rules work inside your brain folder. To make your agent talk the same way in **every** chat, paste a short text into its settings:

- **Claude:** Settings, the personal instructions box. On the desktop app you can also save instructions on this computer.
- **Other agents:** their custom instructions.

At the end of the setup, your agent writes this text for you from your answers. It looks like this:

```
Use simple, plain words and no jargon. Keep replies short, no walls of text. Use short lists and examples. Work step by step and check each step before moving on. Do only what I asked.
```

Keep it short, and don't put private details in it. Your brain's rules still win inside your brain folder.

## Your first week

- **Talk to it every day,** even small things: "Had a call with Marta", "Sent the invoice". The more it knows, the more it helps.
- **Drop things in:** an email you got, a brief, a photo of notes. Ask "Where should this go?"
- **Correct it** when it gets something wrong: "Don't do that, do this." It saves your correction as a rule.
- **Look in Baalda** once or twice, to see how your notes link up.
- **Read the Brain Keeper's line** in your daily note when it says something needs you.

## Keeping it up to date

When there's a new version of Phygital Brain:

1. Update the plugin. In Claude Code: `/plugin marketplace update phygital-brain`.
2. In a chat on your brain folder, say **"Upgrade my second brain."**

Your agent shows what's new, asks first, and keeps your notes and your own rules as they are.

To change your setup answers later, say **"Update my answers."** The forms open again, and your About pages are refreshed.

## If something goes wrong

| What you see | What to do |
|---|---|
| The form window doesn't open | Nothing. Your agent asks the same questions in chat. |
| "I can't write to this folder" | Pick the `My Brain` folder again when you start the task, and check that Google Drive is running. |
| A link looks broken right after a sync | Wait a few minutes. The note is usually still on its way from Google Drive. Your agent never "fixes" it with a blank note. |
| Two copies of a note, one ending in `(1)` | Google Drive made a copy because the note changed in two places at once. Ask your agent: "Merge these two notes." |
| The Brain Keeper didn't run | Scheduled tasks only run while the Claude app is open and your computer is awake. Say "run the brain keeper" to run it now. |
| No morning brief | Same as above. Or say "morning brief" anytime. |
| Your agent forgot something | Check it's working in your `My Brain` folder. It only knows your brain there. |

## Leaving

Your brain is plain text files in your own Google Drive. If you ever stop using Phygital Brain, the notes stay yours, and any notes app that reads Markdown can open them.
