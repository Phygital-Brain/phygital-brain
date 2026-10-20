# Add more skills

A skill is a set of instructions your agent follows for one kind of job. Your brain comes with the Brain Keeper, meeting prep, thinking tools, import and the Writing Check. You can add others, like one that makes videos, and point them at what your brain already knows.

```mermaid
flowchart LR
    I[Install the skill<br>in your agent] --> T[Tell your agent:<br>add it to my brain]
    T --> N[Skills/name/notes.md:<br>how to use your brain with it]
    N --> U[Use it: it reads your<br>voice, projects and people]
    U --> S[Results saved in the<br>right project]
```

## How a skill fits in your brain

- **The skill itself** is installed in your agent (as a plugin, or with the skill's own install line). It isn't copied into your brain, and it's never edited.
- **Your notes for it** live in your brain, in `Skills/{skill-name}/notes.md`: what to read first, where to save results, and how you like things done. This is how one skill works your way.
- **The list of skills** is in `Skills/CLAUDE.md`. Each new skill gets a line there, so every chat knows it exists.

## Add any skill

1. Install it in your agent, the way the skill's own page says.
2. In a chat on your brain folder, say: **"Add the {skill name} skill to my brain."**
3. Your agent asks first, then:
   - makes `Skills/{skill-name}/notes.md` with what the skill should read in your brain (for example `About/brand.md` for your voice and colours) and where it saves its work (usually a project folder),
   - adds a line for it in `Skills/CLAUDE.md`.
4. Use it like any other: "Use {skill} to..." Your agent reads your notes for it first.

To change how it works for you, say "From now on, {skill} should...". Your agent updates `notes.md`, never the skill.

## Make videos with HyperFrames and Keyframes

[HyperFrames](https://github.com/heygen-com/hyperframes) is an open-source tool by HeyGen (Apache 2.0) that turns HTML and animations into MP4 videos. Its **Keyframes** part handles animation: your agent writes the motion, checks it, and you can fine-tune keyframes by hand on a timeline in HyperFrames Studio or the HyperFrames app. HyperFrames isn't part of Phygital Brain; this is how to use the two together.

### What you need

- An agent that can run commands on your computer, like Claude Code (the Claude desktop app's Code tab, or the terminal).
- **Node.js 22 or newer** and **FFmpeg** installed. Your agent can help install them.
- Disk space: rendered videos are large files.

### Install it

In Claude Code:

```
claude plugin marketplace add heygen-com/hyperframes
```

```
claude plugin install hyperframes@hyperframes
```

With another agent, follow the [HyperFrames quickstart](https://hyperframes.heygen.com/quickstart). Then, in a chat on your brain folder, say **"Add HyperFrames to my brain."**

### Connect it to your brain

Your agent writes `Skills/hyperframes/notes.md`. A good one looks like this:

```
Before a video, read:
- About/brand.md: voice, words to use and avoid, colours and fonts if listed
- the project's README.md and its drafts/ folder for the script

Save:
- the HyperFrames project in Projects/{project}/video/
- the finished MP4 in Projects/{project}/assets/, or outside the brain folder
  if it's over 100 MB, with a line in the project's README saying where it is

Style:
- calm motion, no flashy transitions
- captions on by default
```

Add your brand colours and fonts to `About/brand.md` if they aren't there yet, so every video uses them.

### Make a video

In a chat on your brain folder:

- "Make a 30-second video for the picture book from the script in drafts, in my brand."
- "Turn this week's daily notes into a 1-minute update video for my clients."
- "Make a short motion graphic of my cover price going up, for Instagram."

Your agent reads your brand and the script, builds the video, renders a preview, and saves it in the project. It logs one line in today's daily note.

### Edit the keyframes yourself

1. Open the video's project in **HyperFrames Studio** or the **HyperFrames app**.
2. Move, add or ease keyframes on the timeline.
3. Back in the chat: "I changed the keyframes in the picture book video. Check it and render it again." Your agent runs HyperFrames' keyframe check, fixes anything that breaks, and renders.

### Good to know

- Big video files make your cloud drive slow to sync. Keep renders outside the brain folder when they're large, and link to them.
- Music, voice and images the video uses need the right licences. HyperFrames' own media skill can help find them.
- Problems with HyperFrames itself go to [its repository](https://github.com/heygen-com/hyperframes), not to Phygital Brain.
