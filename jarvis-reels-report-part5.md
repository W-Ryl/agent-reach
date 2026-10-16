# Instagram Reels → Ideas for Jarvis (Part 5)

## "Stop building AI agents. One agent, one playbook." (@cooper.simson)
**Reel:** https://www.instagram.com/reel/Dec_uC2tRTg/ (Oct 13, 2026, about 1.35K likes)

> **How this was put together:** the reel's on-screen text and diagrams were read frame by frame. The creator's "four prompts and folder setup" guide is only sent to people who comment "PLAYBOOK", so it wasn't accessed. The method below is rebuilt from the reel itself and from the Anthropic talk it's based on. The four prompts in section 4 are **my own versions** written to match the method; they are not the creator's text.

### 1. What the reel says
- **Hook:** "Stop ~~building~~ AI agents." The reel attributes this idea to Anthropic.
- **The problem:** you catch the AI bug, start building, and end up with **15 half-finished agents** (inbox bot, lead scorer, CRM sync, content bot, support bot and so on) that are all "stuck" and break every couple of weeks. Then you try to **wire them all together**, which makes it worse.
- **The fix, "the complete opposite":** **one agent plus a playbook for each job.**
- **How to build a playbook:**
  1. **Let the AI interview you about your job.** For example, "What starts the job?" ("A new lead fills the form.") and "What does done look like?" ("Reply sent within an hour.")
  2. Turn the answers into a **playbook** with three parts:
     - **Starts:** a new lead
     - **Steps:** read, draft, reply
     - **Done:** reply sent
  3. Give it a **toolbox**: **files, scripts, templates, docs**. These are **linked back** to the playbook, so the agent uses them instead of rebuilding them. "Never build it twice."
  4. Add **"Done means"**: proof the job is finished, such as **numbers, links, a screenshot, tests**.
  5. **It checks its own work** against the "Done means" list before reporting back.
  6. **When it gets it wrong, you fix the playbook**, not the agent. Each fix makes it permanently better.
  7. **Save it, send it:** the playbook is a file you can reuse and share.

### 2. The real source: Anthropic's "Don't Build Agents, Build Skills Instead"
The reel is a simplified version of a talk by **Barry Zhang and Mahesh Murag (Anthropic)** at the AI Engineer conference (about 16 minutes).
- **Watch:** https://www.ai.engineer/talks/CEvIs9y1uog-agent-skills
- **Core argument:** don't build a new agent for every domain. **One general agent plus "skills"** supplies the domain know-how.
- **What a skill is:** a **folder** with a main `SKILL.md` (instructions and navigation) plus **scripts, reference docs and assets**. This matches the reel's "playbook plus toolbox."
- **Progressive disclosure:** only a short description of each skill is loaded at first. The full instructions and files load **only when the task needs them**, so you can have hundreds of skills without filling the context window.
- **MCP vs. skills:** MCP connects the agent to tools and data. Skills hold the **how-to** for workflows.
- **What's still unsolved:** as skills multiply they need testing, versioning and dependency management, like normal software.
- **Further reading:** Anthropic's engineering post "Equipping agents for the real world with Agent Skills."

**Reel term → Claude Skills term:**

| Reel | Claude Skills |
|---|---|
| One agent | Claude Code / Claude Agent SDK (one general agent) |
| Playbook | `SKILL.md` (name, description, instructions) |
| Starts | the skill's *description*: when to use it |
| Steps | instructions in `SKILL.md` |
| Toolbox (files, scripts, templates, docs) | `scripts/`, `references/`, `assets/` folders inside the skill |
| Done means / checks its own work | a verification checklist plus scripts or tests in the skill |
| Fix the playbook when wrong | edit `SKILL.md`; version it in git |

### 3. Example playbook (skill folder)
```
skills/
  lead-reply/
    SKILL.md            ← playbook
    templates/
      reply-email.md    ← toolbox: template
    scripts/
      check_reply.py    ← toolbox: verifies "done"
    references/
      pricing.md        ← toolbox: "price: the usual"
      tone-guide.md
```
```markdown
---
name: lead-reply
description: Use when a new lead fills the website form. Reads the lead, drafts and sends a reply within 1 hour.
---
## Starts
A new form submission arrives.
## Steps
1. Read the lead's message and company.
2. Draft a reply using templates/reply-email.md, prices from references/pricing.md, tone from references/tone-guide.md.
3. Send the reply.
## Done means
- [ ] Reply sent (link to sent email)
- [ ] Sent within 1 hour of the form time (numbers)
- [ ] Price matches references/pricing.md
- [ ] scripts/check_reply.py passes
Report back with the proof. If any check fails, fix it and re-check before reporting.
```

### 4. Four "interview me" prompts (my versions, written to fit the method)
1. **Interview:** "Interview me about one recurring task in my work. Ask one question at a time: what triggers it, the exact steps, what tools and files I use, common mistakes, and what 'done' looks like with proof. Keep going until you could do it without me."
2. **Write the playbook:** "Turn my answers into a skill folder: a SKILL.md with a one-line description of *when* to use it, Starts, Steps and a 'Done means' checklist with verifiable proof. List any templates, scripts or reference docs it needs."
3. **Build the toolbox:** "Create the templates, scripts and reference files that SKILL.md links to, so the agent never has to rebuild them. Add a script or test that checks 'Done means' automatically where possible."
4. **Fix from failure:** "Here's a case where the skill got it wrong: [paste]. Find which step or check was missing or unclear and update SKILL.md (and the toolbox) so it can't happen again. Show me the diff."

### 5. How this applies to Jarvis (and Island Series)
- **Architecture decision:** **Jarvis should be one agent with many skills, not 15 separate agents.** This confirms the direction from the earlier parts: Matt Pocock's skills talk (Part 3), SkillOpt (Part 1), and the ADHD skill list (Part 4).
- **Turn each Jarvis ability into a playbook:** morning briefing, inbox triage, focus mode, task-splitter, premortem, evening shutdown, and so on. Each one gets Starts / Steps / Done means / toolbox.
- **"Done means" plus self-checks** cut errors a lot. Jarvis reports **with proof** (links, numbers, screenshots).
- **The fix-the-playbook loop** is the same as error analysis (Part 3) and SkillOpt (Part 1). Every failure becomes a permanent improvement.
- **Progressive disclosure** keeps Jarvis fast. Only the relevant skill loads per request, which pairs with context engineering (Part 3).
- **For Island Series:** you can still have many *characters* on the island, but under the hood each character can be **the same agent running a different playbook** (Designer skill, Banker skill, Storyteller skill). It's easier to build and maintain, with fewer things that break.
- **Jarvis feature idea:** a voice command, "**Jarvis, learn a new job**", that runs the interview (prompt 1), writes the skill (prompts 2–3), and saves it to the skills folder.

---

## Sources
- Talk page: https://www.ai.engineer/talks/CEvIs9y1uog-agent-skills
- Talk listing: https://ai.engineer/talks/agent-skills
- Talk highlights: https://videohighlight.com/v/CEvIs9y1uog
- Talk transcript: https://sozai.app/transcript/build-skills-instead-agents-anthropic/
- Coverage of the talk: https://devby.io/en/news/anthropic-industriya-oshiblas-s-ii-agentami-proryv-dast-drugoi-podhod-1765362742.amp
- Summary of the talk: https://hyper.ai/en/stories/1bb6d77a6488d174ebc2dd4f20a1642a
- Video notes: https://www.beri.net/learning/anthropic-dont-build-agents-build-skills-video
- Korean-language write-up: https://wikidocs.net/blog/@jaehong/8112/
