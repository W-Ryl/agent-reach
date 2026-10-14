# Instagram Reels → Ideas for Jarvis (Part 3)

## "5 videos to make you an S-tier AI engineer (niche edition)" (@murphmaxxing)
**Reel:** https://www.instagram.com/reel/DecnM25hdVt/ (Oct 13, 2026, about 640 likes)

**What the reel is:** a one-minute list of **5 talks or videos** that teach how to build serious AI agents instead of just "vibe coding." The caption sums them up as covering:
- how LLMs actually run
- locking agent skills to schemas
- cutting 80% of Claude Code's prompt
- context-engineering scratchpads
- error-analysis evals

The links are only sent to people who comment "Video". Below, each video was identified from the thumbnails shown in the reel and then looked up.

This one isn't a tool or a GitHub repo. It's **a study list for whoever builds Jarvis**, and each video maps to a part of Jarvis.

| # | Video | Speaker | Where to watch | Jarvis takeaway |
|---|-------|---------|----------------|-----------------|
| 1 | From Vibe Coding to Agentic Engineering | Andrej Karpathy (with Stephanie Zhan, Sequoia AI Ascent) | https://www.youtube.com/watch?v=96jN2OCOfLs | Build Jarvis with engineering discipline, not vibes |
| 2 | Building Great Agent Skills: The Missing Manual | Matt Pocock (AI Engineer conference) | https://ai.engineer/talks/building-great-agent-skills | How to design Jarvis's skills |
| 3 | Boris Cherny: We Cut 80% of Claude Code's Prompt | Boris Cherny, creator of Claude Code (Y Combinator Startup School) | YC podcast episode "Boris Cherny: Building Claude Code" (search YouTube for "Boris Cherny Y Combinator") | Keep Jarvis's system prompt short; give it tools instead |
| 4 | Context Engineering for Agents | Lance Martin, LangChain (Latent Space podcast) | https://www.latent.space/p/context-engineering-for-agents-lance | How Jarvis decides what goes into the AI's context window |
| 5 | Carrying Out Error Analysis (C3W2L01) | Andrew Ng (DeepLearning.AI) | https://learn.deeplearning.ai/courses/machine-learning-projects/lesson/h9ssf/carrying-out-error-analysis | How to test and improve Jarvis systematically |

---

### 1. Karpathy: From Vibe Coding to Agentic Engineering
- **What it covers:** the difference between "vibe coding" (letting AI write code casually, fine for throwaway projects) and **agentic engineering** (directing AI agents with discipline to build things people rely on). It also covers his "Software 1.0 / 2.0 / 3.0" framing: 3.0 means *prompting is programming*.
- **The reel's point:** he explains how LLMs actually work as a runtime, a mental model for how they process voice, text and images.
- **For Jarvis:** Jarvis will control your computer and your life, so treat it as engineering. That means clear structure, tests, and permissions for risky actions.

### 2. Matt Pocock: Building Great Agent Skills, the Missing Manual
- **What it covers:** a practical framework for writing agent "skills" (reusable instruction playbooks), subtitled "Escaping Skill Hell." It has four parts:
  - **Trigger:** when the skill should activate.
  - **Structure:** how it's laid out.
  - **Steering:** guiding the model's behavior.
  - **Pruning:** removing what isn't needed.
- **Key trade-off:** skills the model picks automatically add context and confusion about which to use. Skills the user picks manually add mental load for the user.
- **The reel's point:** skills locked to schemas (fixed, structured inputs and outputs), described as "AI playbooks."
- **For Jarvis:** each Jarvis ability (inbox triage, morning briefing, opening apps) should be a small, well-triggered skill with a fixed input/output format. This pairs with **SkillOpt** (Part 1, #5) to improve them automatically.

### 3. Boris Cherny: "We cut 80% of Claude Code's prompt"
- **Who:** the creator of Claude Code at Anthropic, interviewed at Y Combinator Startup School 2026.
- **What it covers:** as models got smarter, the Claude Code team **deleted about 80% of the system prompt**, reportedly going from about 15,000 to about 4,500 characters, with no measurable drop in quality. His advice is to **regularly rebuild your AI instructions from scratch as models improve**, instead of piling on more rules.
- **The reel's point:** "Most developers write five-page prompts." Instead, use **a tiny prompt with terminal access**: let the model use tools rather than spelling everything out.
- **For Jarvis:** keep Jarvis's core instructions short. Give it good tools (open app, search, read notes, speak) and let the model figure out how to use them. Revisit the prompt whenever you upgrade the model.
- *Note:* reports disagree on which Claude model this cut was made for. Check the episode itself for exact figures.

### 4. Lance Martin: Context Engineering for Agents
- **What it covers:** "context engineering" means deciding exactly what information goes into the AI's limited context window at each step. Unlike prompt engineering, it covers the whole pipeline. The framework is **write, select, compress, isolate**:
  - **Write:** save notes and "scratchpads" outside the context window for later.
  - **Select:** pull in only the relevant memory or files when needed (retrieval).
  - **Compress:** summarize old conversation so it fits.
  - **Isolate:** split work across sub-agents so each has a clean, focused context.
- **The reel's point:** "Stop dumping your entire repo" into the AI. Use caching and files so "the model only sees the exact tokens it needs."
- **For Jarvis:** this is the core of Jarvis's **memory design**:
  - Keep a notes vault (Part 2, #3).
  - Load only what's relevant to the current request.
  - Summarize long sessions (Mark LV does this, Part 2, #2).
  - Give sub-agents (research, inbox) their own separate context.
- Lance Martin also built **Open Deep Research** (LangChain), an open-source research agent worth looking at.

### 5. Andrew Ng: Carrying Out Error Analysis
- **What it covers:** a short (about 10-minute) classic lesson. Instead of guessing what to improve, **collect about 100 failures, label why each one failed, and count the categories**. Then fix the biggest category first. Example: if only 5% of errors are of one type, fixing them can improve results by at most 5%, so don't start there.
- **The reel's point:** "Amateur builders test their code by eye." Pros build evaluations that test against edge cases.
- **For Jarvis:** log every time Jarvis gets something wrong: a misheard command, the wrong app, a bad answer. Every week, sort the failures into categories and fix the biggest one. Turn the failures into a test set so new changes don't break old things. This is the same idea as SkillOpt's benchmark gate.

---

## How these fit the Jarvis plan (Parts 1–3)

| Jarvis layer | Tools (Parts 1–2) | What to learn (Part 3) |
|---|---|---|
| Overall approach | n/a | Karpathy: agentic engineering, not vibe coding (#1) |
| Skills | SkillOpt, premortem skill | Matt Pocock: trigger, structure, steering, pruning (#2) |
| Core prompt and brain | Claude / GPT | Boris Cherny: short prompt plus good tools (#3) |
| Memory and context | Obsidian vault, Mark LV memory | Lance Martin: write, select, compress, isolate (#4) |
| Testing and improvement | SkillOpt benchmark gate | Andrew Ng: error analysis on real failures (#5) |
| Voice | Voicebox, Hermes voice, Jev | n/a |

---

## Sources
- Karpathy video summary: https://youtubesummary.com/summary/96jN2OCOfLs
- Karpathy, vibe coding vs agentic engineering: https://travis.media/blog/vibe-coding-agentic-engineering-karpathy.md
- Matt Pocock's talk: https://ai.engineer/talks/UNzCG3lw6O0-building-great-agent-skills
- Coverage of Matt Pocock's talk: https://www.startuphub.ai/news/building-better-ai-agent-skills-the-missing-manual
- Boris Cherny episode: https://podscan.fm/podcasts/y-combinator-startup-podcast/episodes/boris-cherny-building-claude-code
- Boris Cherny write-up: https://youmind.com/landing/x-viral-articles/claude-code-loop-engineering-guide
- Boris Cherny summary: https://zeli.app/zh/story/49077040
- Lance Martin episode: https://www.latent.space/p/context-engineering-for-agents-lance
- Open Deep Research case study: https://www.zenml.io/llmops-database/context-engineering-and-agent-development-at-scale-building-open-deep-research
- Andrew Ng's lesson: https://learn.deeplearning.ai/courses/machine-learning-projects/lesson/h9ssf/carrying-out-error-analysis
- Error analysis explained: https://www.kdnuggets.com/2018/01/error-analysis-your-rescue.html
