# Limits

What Phygital Brain does badly, or not yet. Read this before you depend on it.

## It's a brain, not a database

Your brain is for knowledge in words: what you decided and why, who someone is, what a project needs, how you work. It's a poor place for thousands of rows of the same kind of data, like every customer order or an inventory. Keep those in a spreadsheet or a database, and let your brain hold what they mean.

## The rules work because your agent follows them

Nothing in the folder is locked. `.claudeignore` and "ask before you delete" are instructions your agent follows. A different tool, or a person with the folder, can still open and change anything. Keep secret things outside the brain folder.

## Scheduled tasks need a computer, unless they run in the cloud

On your computer, the Brain Keeper and the morning brief run only while your agent's app is open and the computer is awake. A missed run waits or is skipped; say "run the brain keeper" to run it by hand. They can run as cloud routines instead, if your agent has them and your cloud drive connects in the cloud. See [Running in the cloud](folders/skills.md#running-in-the-cloud).

## The first setup uses more of your plan

Building a brain writes many files in one go, so the setup uses more of your AI plan's usage than a normal chat. After that, daily use is similar to any other chat. The Brain Keeper's daily run uses a little every work day.

## Search is by words, not by meaning

Your agent finds notes by names, words, links and folders. It doesn't search by meaning ("notes like this one"). For a brain of a few thousand notes this works well, because the folders and links do most of the finding.

## Files that aren't text

Your agent reads PDFs, images and Word files when you drop them into a chat, and writes what matters into notes. Inside the brain, those files are kept as they are, and some apps show them only as a link.

## Connected apps are read only, and limited

Your brain can read email and calendar through connectors (see [Connect your apps](connect-your-apps.md)), but only to note who you talked to and what's coming up. It never sends or changes anything in an app, it doesn't read chat apps like Slack yet, and it can't read meeting recordings.

## Teams need Baalda's paid cloud

A team can share one brain through Baalda's cloud, which is paid (see [Teams](teams.md)). Permissions are set in Baalda, per folder, not inside a note. Large teams writing at once haven't been tested.

## Phone use depends on your agent and drive

Reading your brain on your phone needs a phone app that can connect to your cloud drive. Adding things from the phone works best through Dispatch, which only Claude has.

## It's new

This is version 0.1.7. The setup has been tested by its makers, not yet by many people. If something goes wrong, open an issue.
