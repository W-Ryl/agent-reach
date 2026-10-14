# Instagram Reels → Ideas for Jarvis (Part 2)

A second batch of 4 links. Each section covers what the reel shows, what the tool actually is (checked against its GitHub README or other sources), the links, and how to use it in **Jarvis**.

**How this was gathered:** captions, on-screen text read from video frames, the projects' own READMEs, and web research. Audio was not transcribed.

---

## Quick summary

| # | Reel | What it is | GitHub / link | Priority for Jarvis |
|---|------|-----------|---------------|---------------------|
| 1 | @brodyautomates | **Voicebox**: free, local voice studio (clone voices, text-to-speech, dictation, MCP for agents) | https://github.com/jamiepine/voicebox | ⭐⭐⭐ **Top pick: Jarvis's voice** |
| 2 | @fatihmakes | **Mark LV "JARVIS"**: full open-source desktop Jarvis (voice, screen, computer control) | https://github.com/FatihMakes/Mark-LV | ⭐⭐⭐ Reference build to borrow from |
| 3 | @aiprofitlabdaily | **Hermes Apollo**: voice agent inside Julian Goldie's Hermes "Agent OS", with Obsidian memory | No official repo (based on Hermes Agent) | ⭐⭐ Ideas: shared memory, daily briefings |
| 4 | @quentin_aimarketing | **Claude "premortem" prompt**: stress-test a plan before acting | Prompt technique (no repo) | ⭐ A "decision check" skill for Jarvis |

---

## 1. Voicebox: the voice one ⭐ (most important)
**Reel:** https://www.instagram.com/reel/DaGI7PJNNWP/ (@brodyautomates, about 7.5K likes)

**What the reel says:** "Someone just built a GitHub repo" that runs **entirely on your own machine**. It has over **33,000 GitHub stars** and was **#1 Repository of the Day** on GitHub Trending. It lets you:
- **clone a voice from a few seconds of audio**
- generate speech in **23 languages**
- **dictate into any text field** with a system-wide hotkey
- all **without a server**

"Normally this kind of thing costs you an ElevenLabs key… but Voicebox does all of it locally." "Free open source genuinely replaces two subscriptions." Setup is shown as pasting the GitHub repo link.

### Links
- **GitHub:** https://github.com/jamiepine/voicebox (MIT license, so free for commercial use)
- **Website / demo:** https://voicebox.sh
- **Docs:** https://docs.voicebox.sh
- **Downloads:** macOS (Apple Silicon and Intel), Windows, and Docker (`docker compose up`). There are no ready-made Linux downloads yet; Linux users build from source (https://voicebox.sh/linux-install).

### What it is
A **local-first AI voice studio**, pitched as a free open-source replacement for **ElevenLabs** (voice output) and **WisprFlow** (voice dictation) in one app. Models, voice data and recordings **never leave your computer**.

### Key features (from the README)
- **8 text-to-speech engines**, switchable per generation:

  | Engine | Languages | Strength |
  |---|---|---|
  | Qwen3-TTS (0.6B / 1.7B) | 10 | High-quality multilingual voice cloning; follows delivery instructions like "speak slowly" or "whisper" |
  | Qwen CustomVoice | 10 | 9 preset voices, controlled with plain-language directions |
  | Qwen VoiceDesign | 10 | **Creates a voice from a written description**, with no sample audio needed |
  | LuxTTS | English | Lightweight (about 1 GB of graphics memory), runs 150× faster than real time on CPU |
  | Chatterbox Multilingual | 23 | Widest language coverage |
  | Chatterbox Turbo | English | Fast; supports emotion tags like `[laugh]`, `[sigh]`, `[whispering]`, `[sarcastic]` |
  | HumeAI TADA (1B / 3B) | 10 | Very long, coherent audio (700+ seconds) |
  | Kokoro | 8 | 50 preset voices, tiny model (82M), fast on CPU |

- **Voice cloning** from a few seconds of audio. You can use multiple samples for better quality, and import or export voice profiles.
- **Dictation (voice in):** hold a global hotkey, speak and release, and the text is pasted into whatever app is focused. Push-to-talk and toggle modes are available. Auto-paste currently works on macOS; Windows and Linux are on the roadmap.
- **Speech-to-text:** OpenAI Whisper (Base to Large, plus Turbo, which is about 8× faster than Large). Every recording is saved with its transcript in a "Captures" tab.
- **Voice personalities:** attach a persona to a voice, and a bundled local AI model rewrites text in that character before speaking it.
- **Audio effects:** pitch shift, reverb, echo, chorus, compression and filters. Built-in presets include Robotic, Radio and Deep Voice.
- **Unlimited length:** long text is split at sentence boundaries automatically and blended back together (up to 50,000 characters).
- **Stories editor:** a multi-track timeline for conversations and podcasts.
- **Fast native app:** built with Tauri (Rust) instead of Electron. It runs on Apple GPUs, NVIDIA, AMD, Intel Arc and plain CPU.

### How Jarvis would use it: the API and MCP server
Voicebox runs a local server at **`http://127.0.0.1:17493`**:

```bash
# Make Jarvis speak in a cloned voice
curl -X POST http://127.0.0.1:17493/speak      # (body: text + profile/voice name)

# Generate an audio file
curl -X POST http://127.0.0.1:17493/generate

# Transcribe audio (speech-to-text)
curl -X POST http://127.0.0.1:17493/transcribe -F "model=whisper-turbo"

# List voices
curl http://127.0.0.1:17493/profiles
```
Full API documentation is at `http://127.0.0.1:17493/docs` while the app is running.

**Built-in MCP server**, so any MCP-capable AI agent can use it directly. Four tools: `voicebox_speak`, `voicebox_transcribe`, `voicebox_list_captures` and `voicebox_list_profiles`.

Hook it into Claude Code with one line:
```bash
claude mcp add voicebox --transport http --url http://127.0.0.1:17493/mcp --header "X-Voicebox-Client-Id: claude-code"
```
For other MCP apps (Cursor, Windsurf, VS Code), use the URL `http://127.0.0.1:17493/mcp`. There is also a bundled `voicebox-mcp` binary for apps that only support the stdio connection type.

- **A different voice per agent:** in Settings → MCP you can give each agent its own voice, so you can tell which agent is talking.
- **Personality mode:** passing `personality: true` to `voicebox_speak` makes the text go through the persona AI first, then into speech.

### Why it's the top pick for Jarvis
- **It covers both directions of voice:** Jarvis can hear you (dictation and Whisper) and talk back (8 voice engines), all locally.
- **Free:** no ElevenLabs bill, and no limits on characters or minutes.
- **Private:** voice data stays on your machine.
- **A custom Jarvis voice:** clone a voice you have the rights to (your own, or a voice actor's with permission), or design one from a description ("calm British AI butler").
- **Easy to plug in:** Jarvis just calls `POST /speak` or the MCP tool. No audio code is needed.
- **Combines well with Part 1:** use Jev (Part 1, #2) to decide actions quickly and Voicebox for the voice.

> ⚠️ Only clone voices you have permission to use. Cloning a real person (for example, a celebrity or a film's Jarvis voice actor) without consent can break laws and platform rules.

**Hardware note:** it runs best with a GPU or Apple Silicon. Smaller engines (Kokoro, LuxTTS) work fine on CPU.

---

## 2. Mark LV: open-source desktop "JARVIS" by FatihMakes
**Reel:** https://www.instagram.com/reel/DdEyVJ6qJre/ (@fatihmakes, about 2K likes)

**What the reel shows:** an Iron Man–style **J.A.R.V.I.S. interface** (red HUD with a voice orb) **playing Clash Royale on its own** in an Android emulator. Jarvis talks back ("I'm defending, sir"), then the creator takes over. He says this was a **prototype only and won't be released**, because using AI to play games breaks the games' rules. He points to the real product instead: the **Jarvis "Mark" models**. The caption mentions Mark 56, Mark 52 (with a YouTube tutorial) and a **Telegram Remote Control** plugin.

### Links
- **GitHub (latest public, "Mark LV" = 55):** https://github.com/FatihMakes/Mark-LV
- **All versions:** https://github.com/FatihMakes (Mark-XLIX, Mark-X.1, and others)
- **YouTube setup videos:** https://www.youtube.com/@FatihMakes
- **Community and free plugins (Telegram Remote Control, VPS):** https://whop.com/fatihmakes/
- **License:** custom ("Copyright (c) 2026 FatihMakes"), **not a standard open-source license**. Read the LICENSE before copying code into a product.

### What it is
A **real-time voice AI for Windows, macOS and Linux** that can **hear, see, speak and control your computer**. It's written in Python, built on **Google's Gemini Live API** for streaming voice, and adds a plugin per feature.

### Features worth copying for Jarvis
**Voice and conversation**
- Real-time voice in any language (Gemini 3.1 Flash Live, about 2× faster to start speaking than the previous model).
- Local **"Hey Jarvis" wake word**: it sleeps until called and sends no audio while asleep. It goes back to sleep after 2 minutes of silence.
- **Push-to-talk** (Ctrl+Space).
- **Instant acknowledgment:** it says something short right away when a long task starts, so there's no awkward silence.
- **Echo guard:** never responds to its own voice.
- 5 voices you can switch live. Sessions can last hours (older conversation is compressed).

**Computer control**
- Opens apps, files and browser tabs.
- Controls volume, brightness, WiFi, windows and power.
- Sends WhatsApp and Telegram messages.
- **Sees the screen and webcam.**
- An **agent mode** for multi-step tasks.

**Memory**
- Unlimited, searchable memory.
- A **memory panel** where you can see and delete every fact it stored about you.
- Session summaries it brings up naturally the next morning.

**Proactive behavior**
- A **morning briefing** (time, yesterday's recap, news).
- Time-aware check-ins, daily headline watching on topics you choose, and hardware temperature alerts.
- Weather, reminders (using the operating system's scheduler), and clipboard actions (translate, summarize, explain or fix whatever you copy).

**Safety and reliability**
- **Undo** for things it did (moved, renamed or created files, changed settings).
- **Real confirmation:** shutdown, restart and WiFi changes wait for **a button you press**. The AI can't approve its own risky actions.
- **Model ladder:** 9 Gemini models ranked by speed. If one fails or runs out of quota, it moves to the next instead of breaking.

**UI and extras**
- Holographic avatar with real lip-sync and facial expressions, plus live theming.
- Plays videos in the interface.
- **Phone remote dashboard** (pair with a QR code).
- Starts automatically on boot.
- **Plugins:** drop one `.py` file into `plugins/` and it learns a new skill.

### Use for Jarvis
This is basically a working Jarvis you can study. Ideas to borrow:
- **One file per plugin** that it discovers automatically.
- **A wake word plus push-to-talk.**
- **Quick acknowledgment** before long tasks.
- **Undo, and a human confirmation button for risky actions.** These are important safety patterns.
- **A model fallback ladder** so it never just breaks.
- **A "what Jarvis knows about me" memory panel.**
- **Morning briefing** and proactive check-ins.
- **A phone remote and Telegram control.**

You could also **pair Mark LV's structure with Voicebox (#1)** if you want a custom or cloned voice instead of Gemini's built-in voices.

---

## 3. Hermes Apollo: voice agent with Obsidian memory
**Reel:** https://www.instagram.com/reel/DedXkvojId8/ (@aiprofitlabdaily)

**What the reel shows:** "**Hermes Agent Apollo**," a voice AI agent inside a "**Mission Control**" dashboard ("Good morning, Julian"). The reel shows it:
- responding to spoken commands live, for example "open Google" and "find SEO keywords"
- **seeing your screen**
- **saving every chat** to an **Obsidian memory vault** ("so it remembers")
- **sharing memory with other agents** ("agents get that… team stays in sync")
- letting you **change its voice**
- giving **daily briefings**

It claims to run through the **ChatGPT voice command-line tool, using a subscription you already have instead of a paid API**.

### Links and what it really is
- **No official "Apollo" repo.** "Apollo" is **Julian Goldie's name** for the voice part of his paid/community "**Hermes Agent OS**" bundle. Fact-checkers note that Nous Research's official docs never use the name "Apollo".
- **The real underlying feature:** Hermes Agent's **Voice Mode** (added in Hermes Agent v0.20.0, August 2026).
- **Hermes Agent (official, open source):** https://github.com/NousResearch/hermes-agent, with docs at https://hermes-agent.nousresearch.com
- **Hermes voice/text-to-speech docs:** https://hermes-agent.nousresearch.com/docs/user-guide/features/tts
- **About Apollo:** https://aitoolsreview.co.uk/insights/hermes-agent-apollo-voice-mode and https://aiprofitboardroom.com/blog/hermes-apollo-voice/
- **Agent OS / Mission Control (Julian Goldie):** https://juliangoldieaiautomation.com/blog/hermes-agent-os/
- **Related open-source alternative:** https://github.com/symunona/obsidian-hermes. This is a real-time voice interface for an Obsidian vault (Gemini live audio) that can read, edit and search notes and saves conversations as Markdown notes.

### Use for Jarvis
- **Shared memory vault:** store every conversation as plain Markdown notes (for example in Obsidian) so **all of Jarvis's sub-agents read and write the same memory**. It's simple, readable and editable by you.
- **A "Mission Control" dashboard:** one screen showing all agents, status and a greeting or briefing.
- **Reuse existing subscriptions** (ChatGPT or Claude) instead of paying per API call. This matches the Grok Bot idea from Part 1, #4.
- Treat the "Apollo" branding as marketing. Build on **Hermes Agent Voice Mode** or **Voicebox (#1)** directly.

---

## 4. Claude "premortem" prompt
**Post:** https://www.instagram.com/p/DeW5v-aiN19/ (@quentin_aimarketing, image carousel)

**What the post says:** "A premortem makes Claude assume your plan has **already failed**, then explain exactly why, **before you commit a penny to it**." The full prompt is in the slide images, which needed a login, so the wording below is a reconstruction of the standard technique, not the creator's exact text.

### What a premortem is
A decision-making technique from psychologist Gary Klein. Instead of asking "what could go wrong?", you state that **it already failed** and ask **why**. Research cited for it ("prospective hindsight") says it surfaces about **30% more reasons** for failure. With AI it also counters the model's habit of agreeing with your plan.

### Example prompt for Jarvis (standard pattern)
```
It is [date 12 months from now]. My plan below was carried out and it FAILED badly.
Act as a skeptical, experienced reviewer. Explain exactly why it failed:
1. List the 5–10 most likely specific causes (no generic risks), grounded in the plan's details.
2. For each: early warning signs I could have spotted, and how likely it is (high/med/low).
3. Then give a revised plan that prevents the top 3 causes.

Plan: [paste plan]
```

### Ready-made premortem skills (Claude Code / agent skills)
- https://www.skills.sh/vishalsachdev/claude-code-skills/premortem
- https://www.skills.sh/julianobarbosa/claude-code-skills/premortem
- https://skills.sh/guia-matthieu/clawfu-skills/pre-mortem

### Use for Jarvis
Add a **"stress-test this" skill**. Before Jarvis spends money, launches something or takes a big action, it runs a premortem automatically and reads the top risks back to you. It pairs with the Etsy workflow (Part 1, #7) and SkillOpt (Part 1, #5).

---

## Recommended next steps for Jarvis (both parts combined)

1. **Voice layer = Voicebox** (local, free). Connect it over MCP or `POST /speak` and `/transcribe`, and design or clone the Jarvis voice.
2. **Fast action routing = Jev** (Part 1). Join the waitlist.
3. **Brain = Claude or GPT** for reasoning. Reuse existing subscriptions where possible (Part 1, #4; Part 2, #3).
4. **Memory = Markdown notes vault** (Obsidian), shared by all agents, with a "what I know about you" panel (Mark LV).
5. **Reference build = Mark LV.** Borrow the wake word, instant acknowledgment, undo, confirmation buttons, model fallback ladder, plugin folder and morning briefing.
6. **Skills** as Markdown files that improve automatically (SkillOpt), including a **premortem** skill before big decisions.
7. **Always-on cloud workers** for overnight tasks (Grok Bot), plus **phone/Telegram remote control** (Mark LV).

---

## Sources
- Voicebox README: https://github.com/jamiepine/voicebox
- Voicebox docs: https://docs.voicebox.sh/
- Voicebox site: https://voicebox.sh
- Third-party Voicebox review: https://wavect.io/blog/voicebox-local-voice-cloning-mcp.md
- Mark LV README: https://github.com/FatihMakes/Mark-LV
- FatihMakes on GitHub: https://github.com/FatihMakes
- FatihMakes community: https://whop.com/fatihmakes/
- Mark-LV issue about phone remote control: https://github.com/FatihMakes/Mark-LV/issues/83
- Hermes Apollo fact-check: https://aitoolsreview.co.uk/insights/hermes-agent-apollo-voice-mode
- Hermes Apollo voice guide: https://aiprofitboardroom.com/blog/hermes-apollo-voice/
- Hermes Agent OS: https://juliangoldieaiautomation.com/blog/hermes-agent-os/
- Hermes Agent OS article on X: https://x.com/i/article/2109696038890250426
- obsidian-hermes: https://github.com/symunona/obsidian-hermes
- Hermes Agent and Obsidian second brain: https://zorost.com/hermes-agent-obsidian-second-brain
- Premortem in practice: https://routine.co/blog/posts/premortem-planning-failure
- Premortem research ("prospective hindsight"): https://blog.idonethis.com/?p=233
- Premortem skill: https://www.skills.sh/vishalsachdev/claude-code-skills/premortem
