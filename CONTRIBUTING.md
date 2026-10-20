# Contributing

Thanks for helping. Phygital Brain is free and open source under the [Apache-2.0](LICENSE) licence. Bug reports, better questions, clearer docs, translations and fixes are all welcome. Small, focused pull requests are the easiest to review.

## Reporting a problem

Click **New issue** on GitHub and pick a form:

| Form | Use it when |
|---|---|
| **Something doesn't work** | The setup or the Brain Keeper did something wrong, or stopped |
| **Question** | You want to know how to do something |
| **Idea or feature** | You want something new or different |
| **Report a security problem, privately** | Something could leak private notes or make the agent ignore the rules. Only the maintainer sees it. See [SECURITY.md](SECURITY.md). |

Issues are public. **Never paste your notes, names of real people, private details, or anything from `Memory/finances/`.** Make a small made-up example instead.

## Ground rules

Read [AGENTS.md](AGENTS.md) first. The short version:

1. **The templates are the source of truth.** If you change a rule, change the doc page that explains it in the same pull request.
2. **Plain words.** Short sentences, everyday words, no jargon, in every question, message, template and doc.
3. **No em dashes.**
4. **"Your agent"**, never a product name, in anything a person sees.
5. **English stays English** for folder names, file names, links to files and info block words.
6. **The agent asks first** before it creates, moves, renames or deletes someone's notes. Never weaken that.
7. **Keep upgrades safe:** a person's notes and own rules must survive every upgrade.

## Changing something

1. Fork the repository and make a branch.
2. Make your change.
3. Run the checks. No installs needed, only Python 3:

   ```bash
   python3 scripts/check.py
   ```

   They check the links, the files the skills name, em dashes, the form HTML and the version numbers.

4. If you changed a skill, a form or a template, **build a test brain** with your change:
   - Install your copy as a plugin, or point your agent at `skills/brain-setup/SKILL.md` in your copy.
   - Run the setup in an empty folder, once as someone who sells and wants a morning brief, once as someone who doesn't.
   - Read what was built. Check that no `{Name}`-style placeholder is left, and that every note links somewhere.
   - For upgrade changes, also upgrade a copy of an older brain, and check their own rules are unchanged.
5. Add a line to [CHANGELOG.md](CHANGELOG.md).
6. Open a pull request. The checklist in it covers the rest.

## Translations

A checked translation goes in `languages/{code}.md`, for example `languages/pt-BR.md`: the form questions, options and buttons, and the setup messages. Keep every `data-name` and `data-value` in English. See [languages/README.md](languages/README.md).

## Credit

Keep the line "Created by Phygital-Brain" in [NOTICE](NOTICE). By sending a pull request, you agree your change is under the Apache-2.0 licence.
