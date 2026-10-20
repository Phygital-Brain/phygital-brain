# The folders in your brain

Your brain is one folder with seven folders inside. Each one holds one kind of thing. Your agent knows where everything goes, so you never have to.

| Folder | What goes in it | Page |
|---|---|---|
| `About/` | Facts about you: who you are, your goals, your work, your voice | [About](about.md) |
| `Daily/` | One note for each day, and your list of open tasks | [Daily](daily.md) |
| `Projects/` | One folder for each thing you're working on | [Projects](projects.md) |
| `Relationships/` | One note for each person or company you work with | [Relationships](relationships.md) |
| `Memory/` | Decisions and why you made them, research, money, applications, old things | [Memory](memory.md) |
| `Library/` | Things you use again and again: prompts, templates, checklists | [Library](library.md) |
| `Skills/` | The helpers: the Brain Keeper and the morning brief | [Skills](skills.md) |

There are also two files at the very top:

- `CLAUDE.md`: the main rules your agent follows everywhere. See [Main rules](main-rules.md).
- `.claudeignore`: a list of things your agent must not read unless you ask. See [Main rules](main-rules.md#things-your-agent-never-reads).

## Things every folder has in common

- **A rule file.** Every folder has its own `CLAUDE.md`. It tells your agent what goes there and how each note starts. You can read it, but you don't have to.
- **An info block.** Every note starts with a few lines between `---` marks, like `status: active` and `tags: [...]`. It helps your agent find and sort notes. These words always stay in English, even if your brain speaks another language.
- **Links.** Notes point to each other with double brackets, like `[[Marta]]` or `[[goals]]`. Click one in Baalda to jump to that note.
- **No empty folders.** A folder inside a folder only appears when something needs to go in it.
- **Your agent asks first** before it makes a new note, moves something, renames something or deletes something. Small updates to a note that already exists, it just does, and tells you in one line.
