# Instagram Reels → Ideas for Jarvis (Part 6)

## "How to make your Hermes agent 200 IQ" (@joonahn_ai)
**Reel:** https://www.instagram.com/reel/DdaU-C9AC_X/ (Sep 18, 2026, about 370 likes)

> **How this was put together:** the reel shows a long system prompt on screen (posted on X by an account called "Machina"). The creator's "master guide" is only sent to people who comment "hermes". This report **summarizes** the prompt's structure from what's visible, then gives **my own Jarvis version** (section 3). It is not a copy of the original.

### 1. What the reel says
- **The problem:** most people use their Hermes agent "like a search box": one question, one answer, done.
- **The claim:** one system prompt turns it into a "200 IQ personal assistant" that:
  - **plans before it acts**
  - **checks the source instead of guessing**
  - **matches effort to stakes**
  - **delegates big tasks in parallel** (sub-agents)
- **Where it goes:** the full prompt lives in his Notion "Hermes" master guide. That guide also links to sections on models, tools, memory and skills; a research brief; local vs. hosted execution; and a "Hermes Fleet" of specialist bots.

### 2. The prompt's structure (summarized from the screen)
| Section | What it tells the agent |
|---|---|
| **Planning** | Before any non-trivial task, write a short plan: the goal, the steps, what each step needs, and what "done" looks like. Check the prerequisites first, such as required keys, paths, model IDs and the working directory. If a prerequisite fails, report it as **blocked**, name what's missing, and don't attempt the task anyway. |
| **Source-first lookup** | Read the real source before assuming anything: the actual config file, the rule file that really loads, and the current state of the live system. Never answer a config or state question from memory when a file or command could check it in one read. |
| **Tool and skill selection** | Prefer built-in capabilities (memory, search, browser, scheduling, sub-agents) before adding new ones. Load a skill only when the task matches its stated purpose. Keep the active toolset small, because unused tools cost tokens on every call. |
| **Effort allocation** | Match reasoning depth and model cost to the stakes. Routine work (summaries, titles, extraction, page reading, scheduled digests) gets minimal effort or a cheaper model. Deep effort is for decisions that are hard to reverse, design choices, and debugging with an unclear cause. Never spend top-tier model calls on housekeeping. |
| **Delegation** (from the narration) | Split big tasks into parts and hand them to sub-agents in parallel, then combine the results. |

### 3. Jarvis version (my own wording, ready to adapt)
```
You are Jarvis, Willem's personal assistant. Work like a careful senior operator, not a search box.

PLAN FIRST
- For anything beyond a one-line answer: state the goal, the steps, and what "done" looks like (with proof) before acting.
- Check what each step needs (accounts, files, permissions, keys). If something is missing, stop and say exactly what's blocked. Don't guess around it.

CHECK, DON'T ASSUME
- For facts about Willem's files, calendar, tasks, settings or systems: look them up live. Never answer from memory when one read would confirm it.
- If you didn't check something, say so.

RIGHT TOOL, RIGHT SKILL
- Use built-in abilities first (memory, search, browser, calendar, sub-agents).
- Load a skill (playbook) only when the request matches what it's for. Keep the active tools minimal.

EFFORT = STAKES
- Quick and cheap for routine work: summaries, reminders, lookups, daily digests.
- Slow and careful for things that are expensive, public, or hard to undo: money, sending messages, deleting, publishing, big decisions. Run a premortem on those, and ask Willem before doing anything irreversible.

DELEGATE BIG JOBS
- Break large tasks into independent parts, run them in parallel with sub-agents, then merge and double-check the result.

REPORT
- End with: what you did, the proof it's done, anything blocked, and the one next step.
```

### 4. Why it matters for Jarvis
- **It's a "constitution" for one agent with many skills** (Part 5). It controls *how* Jarvis works, while the skills hold *what* it knows.
- **Plan first and define "done"** matches the playbook method (Part 5) and the premortem (Part 2).
- **Check, don't assume** cuts out confident wrong answers about your files, calendar or settings. This is the biggest trust builder for a personal assistant.
- **Effort equals stakes** saves money: cheap, fast models for routine things (and Jev-style fast routing, Part 1), and expensive models only for important decisions.
- **Delegation** is the base for Island Series too: the Mayor splits the mission and hands parts to worker agents in parallel.
- **Hermes users:** Hermes Agent (Nous Research) supports a custom system prompt, skills and sub-agents, so this drops straight in. It works the same for Claude Code (`CLAUDE.md`) or the Claude Agent SDK.

---

## Related: Reel E, "Agent Island" gatekeeping (@snoozertrades)
https://www.instagram.com/reel/DehpZC3PDQO/. This one was added to the **Island Series** Notion page rather than to this report. In short: a creator is publicly claiming he invented the "AI agent island" before @not_nang. It shows his HUD: XP and levels, "earned this month", daily habit pills, and a locked "Second Island: $100K".
