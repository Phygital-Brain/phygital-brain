# The setup questions, as plain text

Use this file only when you can't show the form window (Step 0.5 in `SKILL.md`). It has the same questions as the four forms, with the same answer names.

- Click questions (AskUserQuestion, up to 4 per call, 2 to 4 options each; "Other" is added for you) where the tool exists. Otherwise numbered options in chat, answered with a number.
- Free-text questions go together in one chat message per form. Tell them short answers are fine and they can skip any.
- Same switches and same order as the forms. `(multi)` means they can pick several.

## Form 1: About you

Chat message:

1. Your name, and what you do in one line. (`name`)
2. What are you good at? Skills, strengths, what people come to you for. (`strengths`)
3. What do you stand for, and what work do you say no to? (`values`)
4. What drains you? (`energy`)
5. Where are you based? Optional, it sets your time zone. (`city`)
6. A link that describes you, optional. Your agent reads it so you type less. (`link`)

Click questions:

- What describes you best? (`you`): Freelancer or creator · Small business owner · Employee or professional · Personal projects
- Do you sell anything or have clients? (`selling`): Yes, services or clients · Yes, products · Not yet, planning to · No
- What should your second brain help with? (`help`, multi): Organise projects · Remember people · Write for me · Goals and decisions
- How should your agent talk to you? (`style`): Short and plain · Detailed · Friendly and casual · Formal and professional
- How do you take things in best? (`learning`, multi): Short lists · Examples · Step by step · Pictures and diagrams
- When do you focus best? (`focus_time`): Early morning · Late morning · Afternoon · Night

## Form 2: Your work

Click questions: the 3 job questions you write (see `SKILL.md`, Form 2), as click questions where they are choices.

If BUSINESS = on:

- Who are your customers? (`customers`, multi): Businesses and brands · Agencies · Individuals · Other creators
- How do most customers find you? (`leads`, multi): Referrals and word of mouth · Social media · I reach out to them · Platforms or marketplaces
- What slows you down most? (`pain`, multi): Finding clients · Admin, quotes and invoices · Posting content regularly · Too many tools and scattered notes
- Main goal for the next 12 months? (`goal`): Earn more · More free time · Launch something new · Get organised

If BUSINESS = off:

- Which areas matter most right now? (`areas`, multi): Career or job · Learning or studies · Creative projects · Side project
- What slows you down most? (`pain`, multi): Too many ideas, no follow-through · Scattered notes · Forgetting details about people · No clear goals
- Main goal for the next 12 months? (`goal`): Grow in my career · Finish a big project · Learn a new skill · Get organised

Chat message:

1. The job question that needs typing (`job_clients`).
2. What are you working on now? Up to 3, one line each. (`projects`)
3. What's worrying you most right now? (`worries`)

## Form 3: Your days and people

Click questions:

- When should your morning brief be ready? (`brief_time`, only if BRIEF = on): 7:00 · 8:00 · 9:00 · No brief
- Who do you work with? (`people`, multi): Clients (only if BUSINESS = on) · Collaborators · Team or freelancers · Partners, press or venues. "Just me" comes through "Other".
- Where do you talk to people? (`comms`, multi): Gmail or Google Workspace · Outlook or Microsoft 365 · WhatsApp · Slack or Teams
- Where do your notes and work live today? (`notes_now`, multi): Google Drive or Docs · Notion · Apple Notes · Paper notebooks
- How do you want to sound in writing? (`voice`, multi, only if BUSINESS = on and WRITE = on): Warm and personal · Direct and confident · Humble and honest · Playful

Chat message:

1. Which days do you work? (`work_days`, for example "Mon to Fri")
2. Who matters most in your work right now? Up to 3 names, one line each. (`key_people`)
3. Your social media, for work or personal projects. (`social`)

## Form 4: Files

One chat line: "Anything your agent should read before building? You can drop files (CV, About page, price list, old notes) or paste links. Or just say 'build'."
