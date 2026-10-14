# Instagram Reels → Ideas for Jarvis

A research report on 11 Instagram links, describing what each one shows, what the tool or feature really is, and how it could be used in **Jarvis**, a personal AI assistant.

**How this was gathered:** captions and on-screen text pulled from each post, then checked against the projects' own pages and news coverage. Audio was not transcribed, so a few details from the spoken parts of the videos may be missing. 3 of the 11 links could not be read (see the end).

---

## Quick summary

| # | Reel | Topic | Relevance to Jarvis |
|---|------|-------|---------------------|
| 1 | @builtbynus | A working "Jarvis" built on **Jev** + Nūs | ⭐⭐⭐ Closest reference design |
| 2 | @aiupdates.hub | **Jev** (TypeSafe AI) voice Mac assistant demo | ⭐⭐⭐ Speed / acting while the user talks |
| 3 | @julian.goldie_ | **Hermes Speech**: voice plugin for Hermes Agent | ⭐⭐⭐ Text-to-speech and speech-to-text |
| 4 | @colton.ai.dean | **Grok Bot**: always-on agents on a cloud computer | ⭐⭐⭐ 24/7 background work |
| 5 | @marc.kaz | **Microsoft SkillOpt**: skills that improve themselves | ⭐⭐ Self-improving Jarvis |
| 6 | @cracked.artificial | Heretic, God's Eye View, Brain2Qwerty | ⭐ Mostly background / caution |
| 7 | @thejimmyreilly | Claude finds Etsy product ideas and builds a digital product | ⭐ Example "money-making" workflow |
| 8 | @syntaix.ai | "7 GitHub repos that make AI feel different" (image carousel) | ⚠️ Repo names only in the images, not readable |
| 9–11 | 3 posts | Could not be accessed | — |

---

## 1. "I built a working Jarvis with Jev" (@builtbynus)
**Link:** https://www.instagram.com/reel/DdjhmVyS1Ej/

**What the reel shows:** A one-take demo of a voice assistant. The creator just talks, and the assistant opens apps, types and searches **while they are still mid-sentence**. It then summarizes what is on their plate from their real notes and calendar. The milliseconds on screen show how long Jev took to decide each action.

**The architecture they describe (the key takeaway):**
- **Jev = the reflexes:** a tiny, very fast model that picks the next action.
- **A bigger model = the brain:** handles reasoning and longer answers.
- **The user's own notes = the memory:** no separate memory database. It reads folders of the user's own notes when asked, and only saves new routines when the user says yes.
- The app it lives in, **Nūs**, is free. The voice "reflexes" layer is the creator's own code.

**Research:** The Nūs project page describes Jev picking each action in roughly **200–350 ms** and using a TypeSafe API key for voice commands.

**Use for Jarvis:** This is almost exactly the Jarvis concept, so treat it as a reference architecture. Split Jarvis into a **fast router** (decides *what* to do in under half a second) and a **slow thinker** (an LLM such as Claude or GPT for actual reasoning). Use the user's own files and notes as memory, and ask before saving anything new.

---

## 2. Jev voice-controlled Mac assistant (@aiupdates.hub)
**Link:** https://www.instagram.com/reel/DdkX_7KxKUl/

**What the reel shows:** Developer **Andy Gao** says "open the notes app and create…" and Notes opens **before he finishes the sentence**. The demo was posted on X on Sept 18, 2026.

**What Jev actually is:**
- Made by **TypeSafe AI**, released Sept 15, 2026. They call it a **"System One model"**: the fast, instinctive kind of thinking, as opposed to slow deliberate reasoning.
- It **doesn't write text like a chatbot.** It returns **typed decisions with confidence scores** (for example "open app: Notes, 0.97") that your code can branch on.
- It makes decisions in a fraction of a second, so it can start acting while you are still talking.
- **It doesn't see the screen or press keys itself.** Gao's own code does the clicking and typing. His experiment is on GitHub as `musubipapi/computah`.
- Access: hosted API, **early access via a waitlist** (typesafe.ai).

**Use for Jarvis:**
- **Intent routing:** map a spoken command to "which app / which tool / which action" almost instantly.
- **Starting early:** begin opening the app while the sentence is still being spoken, so Jarvis *feels* instant.
- **Confidence scores** let Jarvis act automatically when sure and ask "did you mean…?" when not.
- **Next step:** join the Jev waitlist, and look at `computah` and the community list `MrJev/awesome-jev` on GitHub.

---

## 3. Hermes Speech: voice plugin for Hermes Agent (@julian.goldie_)
**Link:** https://www.instagram.com/reel/DeLqbiRiJA7/

**What the reel shows:** A free plugin that lets a **Hermes agent talk out loud and understand voice messages**. Its main claims:
- **80+ speech models behind one API key**, so there's no juggling of separate voice subscriptions.
- Setup by just telling the agent "set up speech for me."
- Pick a voice by description ("warmer", "British narrator") and **preview samples** before choosing.

**Research:**
- **Hermes Agent** is an open-source AI agent from **Nous Research**.
- `hermes-speech` is a **third-party plugin** (via the AllModels API), *not* an official Nous product. It's listed as MIT-licensed, for Hermes Agent 0.20+.
- Hermes Agent already has **built-in voice**: about 10 text-to-speech providers (Edge TTS by default, plus ElevenLabs, OpenAI and local engines like Piper). It now **streams speech** from most API-based voices, so replies start playing sooner.

**Use for Jarvis:**
- Jarvis needs a **voice layer**: speech-to-text in, text-to-speech out. A single-API-key setup like this avoids managing many providers.
- **Pick-a-voice-by-description with previews** is a nice touch for setting Jarvis's personality.
- **Streaming speech** matters: Jarvis should start talking after the first sentence is ready, not after the whole answer.
- If Jarvis is built on Hermes Agent, this plugin drops in directly. Otherwise, copy the pattern: one gateway to many voice models.

---

## 4. Grok Bot update (@colton.ai.dean)
**Link:** https://www.instagram.com/reel/Dec2yStPEmX/

**What the reel shows** (from its on-screen captions): xAI's **Grok Bot** can now use your **own Claude subscription**. You log in to Claude Code inside the bot and switch on "Claude subscription – access for this bot." The reel's other points:
- Each bot does **computer use** on its own cloud machine.
- It's pitched as "twice as efficient."
- You **don't need a Mac mini running at home**: agents keep working with your laptop lid closed and **run overnight**.
- Setup is simple: pick an individual bot (for example "Research", "My bot", "Inbox"), then check what it has access to.

**Research:**
- Grok Bot is xAI's agent product. **Each bot runs on a persistent cloud computer with its own browser, files, terminal and logins**, so work continues after you close your device.
- You can install Claude Code (or Codex) in the bot's terminal and sign in with your own subscription.
- Pricing is reported inconsistently: it comes through SuperGrok, X Premium+ or a Cursor plan, with figures around $20/month. Check current pricing before relying on it.

**Use for Jarvis:**
- **Always-on background workers:** Jarvis could hand long tasks (research, inbox triage, monitoring) to a cloud agent that runs overnight and reports back in the morning.
- **Multiple named bots with their own permissions** ("Research", "Inbox") is a good pattern: separate agents, each with limited access.
- **Bring your own subscription** keeps costs down by reusing an existing Claude plan.

---

## 5. Microsoft SkillOpt: self-improving agent skills (@marc.kaz)
**Link:** https://www.instagram.com/reel/DbEK3bustQ7/

**What the reel shows:** Microsoft open-sourced **SkillOpt**, which lets an agent's "skills" (instruction files) **improve themselves**. A model runs the task, and an optimizer rewrites the instructions based on the results. The reel lists four features:
- It separates what worked from what failed.
- It automatically rejects edits that don't beat the benchmark.
- It beats hand-written prompts and TextGrad.
- It isn't locked to one model.

**Research:**
- From Microsoft Research, MIT license, repo **github.com/microsoft/SkillOpt**, paper arXiv:2605.23904.
- It treats a **Markdown skill file as the only thing that gets "trained"**. The AI model itself is never changed.
- **How it works:** run tasks → score the results → reflect and edit the skill file → keep the edit only if it scores better on held-out tests. The output is a `best_skill.md` (about 300–2,000 tokens) that you put in front of the model.
- **Results:** tested on 6 benchmarks, 7 models and 3 setups (including Claude Code), and best or tied in all 52 combinations.
- **SkillOpt-Sleep** (v0.2.0, July 2026) adds a **nightly offline self-improvement** mode for local coding agents.

**Use for Jarvis:**
- Write Jarvis's abilities as **skill files** ("how to triage my inbox", "how to plan my day"). Let SkillOpt rewrite them over time based on what went well.
- **A nightly improvement loop** (the "Sleep" idea): Jarvis reviews the day's tasks overnight and improves its own playbooks.
- The **benchmark gate** is important: only keep changes that measurably help, so Jarvis doesn't get worse.

---

## 6. Three open-source projects about privacy (@cracked.artificial)
**Link:** https://www.instagram.com/reel/Dd_vtriAntp/

**What the reel shows:** Three free, public projects with the message: "the same code that protects you is the code that exposes you."

**a) Heretic** (github.com/p-e-w/heretic)
- **What it is:** automatically removes "refusal" behavior from open-weight AI models (a technique called "abliteration").
- **How it works:** finds the single internal direction tied to refusing and removes it, while keeping the model close to the original.
- **Details:** about 45 minutes per model on an RTX 3090. AGPL-3.0 license.
- **Jarvis relevance: low and risky.** It's only relevant if you run a local model that over-refuses harmless requests. Uncensored models can produce harmful output, so add your own safety checks if you go that way.

**b) God's Eye View** (github.com/bilawalsidhu/gods-eye-view)
- **What it is:** a 3D globe in the browser (built on CesiumJS) that layers **live public data** in one place: flights (including military), ships, satellites, earthquakes, traffic and public CCTV feeds.
- **Caveats:** the project warns the data may be delayed or wrong. Some bundled data is **non-commercial only** (CC BY-NC-SA).
- **Jarvis relevance: medium, as an add-on.** Possible as a "world awareness" dashboard or data source, such as "what's that plane overhead?" or travel and weather awareness.

**c) Brain2Qwerty (Meta)** (github.com/facebookresearch/brain2qwerty)
- **What it is:** Meta research that **reconstructs typed sentences from brain recordings** (MEG), with no implant.
- **Results:** the newer version reportedly averages about 61% word accuracy (78% for the best participant).
- **Limits:** needs a room-sized scanner in a magnetically shielded room, and any head movement breaks it.
- **Jarvis relevance: none for now.** Research only, but a glimpse of future brain-to-computer input.

---

## 7. Claude mines Etsy for product ideas (@thejimmyreilly)
**Link:** https://www.instagram.com/reel/DbszHEghro6/

**What the reel shows:** The creator used **Claude to research Etsy for product ideas**, then had it **build a digital product** that he says made hundreds of sales. The prompts are only sent to people who comment "prompt", so the exact workflow isn't public.

**Research:** No independent coverage of this creator was found, so the sales claim is unverified. The general workflow is common:
1. Have the AI research what's selling in a niche (top listings, reviews, gaps).
2. Pick an underserved idea.
3. Have the AI generate the product (planner, template, printable, guide).
4. Have it write the listing (title, tags, description).

There are also community Claude Code skills for Etsy digital products.

**Use for Jarvis:** an example of a **multi-step "business" workflow** Jarvis could run on command ("research a product idea in niche X and draft it"). It's useful as a skill template, and pairs well with SkillOpt (#5) to improve it over time.

---

## 8. "7 GitHub repos that make AI feel VERY different" (@syntaix.ai)
**Link:** https://www.instagram.com/p/DdlzMA8iXG7/

**What the post shows:** An image carousel. The caption only gives themes: AI working with **Wi-Fi signals, Android apps, voice, simulations, research, codebases and autonomous agents**. The actual repo names are **only in the slide images**, which Instagram wouldn't serve without a login, and the full links are only sent to people who comment "REPOS."

**Status:** ⚠️ The 7 repos couldn't be identified. Guessing would be unreliable, so they're left out.
**To finish this one:** open the post, screenshot the slides (or comment "REPOS" to get the list), and send the names. They can then be researched and added here.

---

## Could not be accessed

| Link | Reason |
|------|--------|
| https://www.instagram.com/reel/Dd6izTYiln1/ | Age-restricted (needs a logged-in account). Posted by Tunde Alao (@itstundeanthony). The visible caption only says "Comment 'agent' for the setup guide", so the topic is some kind of AI agent setup. |
| https://www.instagram.com/reel/DeKuJ7dpO5R/ | The account limits viewers to 21+, so it needs a login. |
| (carousel slides of #8) | Images need a login. See above. |

**To finish these:** send screenshots or the captions, or watch them and describe them in one line each.

---

## Suggested Jarvis architecture from these reels

1. **Voice in/out:** speech-to-text and streaming text-to-speech through a single gateway with many voices (#3).
2. **Reflexes:** a fast decision model such as Jev routes each command to an action in about 200–350 ms, starting while the user is still talking (#1, #2).
3. **Brain:** a larger model (Claude or GPT) for reasoning, planning and long answers (#1).
4. **Memory:** the user's own notes and files, read on demand. Ask before saving anything new (#1).
5. **Hands:** code that actually opens apps, types and clicks on the local machine (#2). Cloud agents with their own browser and terminal handle long or overnight jobs (#4).
6. **Skills:** each capability is a Markdown skill file, improved automatically each night and kept only if it scores better (#5).
7. **Example workflows:** product research → build → listing (#7). Optional "world awareness" data layers (#6b).

---

## Sources

- TypeSafe AI, Jev launch: https://typesafe.ai/blog/introducing-system-one-models-and-jev
- TechCrunch on Jev: https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/
- MarkTechPost on Jev: https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/
- The Register on Jev: https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711
- Andy Gao's demo on X: https://x.com/instantricecook/status/2100814590300889426
- Nūs: https://potlakai.github.io/nus/
- awesome-jev: https://github.com/MrJev/awesome-jev
- hermes-speech listing: https://hermesatlas.com/projects/allmodels-io/hermes-speech
- Hermes Agent voice docs: https://hermes-agent.nousresearch.com/docs/ko/user-guide/features/tts
- Hermes streaming speech: https://runtimewire.com/article/nous-research-streaming-speech-hermes-agent-voice-chats
- Grok Bot breakdown: https://www.vellum.ai/blog/official-grok-bot-breakdown
- Claude Code in Grok Bot: https://www.mindstudio.ai/blog/run-claude-code-codex-inside-grok-bot
- Grok Bot explained: https://www.ayautomate.com/blog/grok-bot-xai-ai-agents-explained
- SkillOpt (Microsoft Research blog): https://www.microsoft.com/en-us/research/blog/skillopt/
- SkillOpt paper page: https://www.microsoft.com/en-us/research/publication/skillopt-executive-strategy-for-self-evolving-agent-skills/
- Heretic overview: https://pyshine.com/Heretic-Directional-Ablation-Censorship-Removal-Language-Models/
- God's Eye View README: https://raw.githubusercontent.com/bilawalsidhu/gods-eye-view/main/README.md
- God's Eye View coverage: https://www.implicator.ai/gods-eye-view-planes-ships-palantir/
- Brain2Qwerty v2: https://thenextweb.com/news/meta-brain2qwerty-v2-non-invasive-brain-to-text
- Etsy digital products Claude skill: https://claudskills.com/skills/etsy-digital-products/
