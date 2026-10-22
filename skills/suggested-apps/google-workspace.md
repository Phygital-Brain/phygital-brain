# Connect Google Workspace (Gmail, Calendar, Drive)

Connect your Google account so your brain can read your email and calendar, read only. Each work day, the Brain Keeper notes who wrote to you (only people and companies that already have a note, and clear new leads) and puts tomorrow's meetings in your daily note. Meeting prep reads your calendar when you ask. Google Drive lets your agent reach your brain folder from a phone or a cloud routine. What each app does in your brain, and the rules: [Connect your apps](../../docs/connect-your-apps.md).

## What you need

- A Google account (Gmail, or Google Workspace for work).
- An agent that takes connectors, like the Claude app (web, desktop or phone) or Claude Code.

## Check first

Check which of Gmail, Google Calendar and Google Drive already show up as connectors in this chat. Connect only the ones that don't (steps 1 and 2), then do step 3. If all three are there, go straight to step 3.

## Connect it

With Claude:

1. In Claude's settings, open **Connectors**.
2. Connect **Gmail**, **Google Calendar** and **Google Drive**, and sign in with your Google account.
3. In a chat on your brain folder, say: **"Connect my Gmail and calendar to my brain."**
4. Your agent checks the connectors work, asks which ones your brain should read from, and adds them to `Skills/connected-apps/connected-apps.md`.

With another agent, use its own connector or integration settings, then do step 3.

There's no `notes.md` for this one: what your brain reads from each app goes in `Skills/connected-apps/connected-apps.md`.

## Good to know

- **Read only.** Your agent never sends, replies, deletes, archives, labels, moves or accepts anything. It writes a draft only when you ask in a chat, and you send it.
- To stop, say **"Stop reading my email."** To cut access completely, also disconnect it in your agent's settings.
- Connecting an app lets your AI company see what your agent reads from it. Connect only what you're comfortable with.
