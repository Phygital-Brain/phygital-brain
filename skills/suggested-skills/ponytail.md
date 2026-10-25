# Keep your code small with Ponytail

[Ponytail](https://github.com/DietrichGebert/ponytail) is an open-source coding skill by Dietrich Gebert (MIT). It makes your agent act like a lazy senior developer: before it writes code, it checks whether the job needs code at all, whether your project or the browser already does it, and only then writes the smallest thing that works. Its replies are short and plain. It also reviews a change or a whole project and tells you, in plain words, what to fix first. Ponytail isn't part of Phygital Brain; this is how to use the two together.

## What you need

- An agent that can work on code on your computer, like Claude Code (the Claude desktop app's Code tab, or the terminal), Codex, Cursor or Gemini CLI.
- A project with code, in its own folder.

## Install it

In Claude Code:

```
claude plugin marketplace add DietrichGebert/ponytail
```

```
claude plugin install ponytail@ponytail
```

With another agent, follow the [Ponytail install guide](https://github.com/DietrichGebert/ponytail/blob/main/INSTALL.md). Then, in a chat on your brain folder, say **"Add Ponytail to my brain."**

## Connect it to your brain

Ponytail works on the code, not on your notes. Your brain keeps why the code exists and the shortcuts you chose to leave for later.

Your agent writes `Skills/ponytail/notes.md`. A good one looks like this:

```
Before coding, read:
- the project's README.md: what the code must do, and for whom

Where:
- the code lives in its own folder, not in the brain
  (write its path in the project's README.md)

Save:
- a short summary of each review or audit in the project's notes/ folder

Style:
- level: full
```

## Use it

In a chat on your project's folder:

- "Add a contact form to my site. Ponytail."
- "Review my last change." (`/ponytail-review`)
- "Audit the whole project and tell me what to fix first." (`/ponytail-audit`)
- "List the shortcuts we left for later." (`/ponytail-debt`)

Your agent writes the smallest change that solves the task, or runs the review and saves its summary in the project. It logs one line in today's daily note.

## Change it yourself

1. Pick how strict it is: `/ponytail lite`, `/ponytail full` or `/ponytail ultra`. `/ponytail off` turns it off.
2. Back in the chat: "From now on, use Ponytail lite for this project."

## Good to know

- In Claude Code it shows a small band above the chat with what the task cost and whether the tests passed. `/ponytail band` hides it. Its numbers stay on your computer.
- Only install it from `DietrichGebert/ponytail` on GitHub. Copies under other names aren't the real one.
- Problems with Ponytail itself go to [its repository](https://github.com/DietrichGebert/ponytail), not to Phygital Brain.
