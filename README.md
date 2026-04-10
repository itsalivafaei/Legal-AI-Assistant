# Legal AI Assistant

A multimodal domain-specific QA prototype that accepts text or voice input, gates questions to the legal domain using zero-shot classification, and returns a spoken answer via a Gradio interface.

**Project status:** Personal prototype. Not a production system, not a legal advice tool.

---

## What it does

1. The user types a question or records audio in the Gradio interface.
2. Audio is transcribed to text using OpenAI Whisper.
3. A BART-based zero-shot classifier determines whether the question is legal-domain-relevant (threshold: 0.70 confidence).
4. Relevant questions are sent to the Groq API (Llama 3.1-8b-instant) with a legal-domain system prompt.
5. The text response is converted to speech (gTTS) and returned alongside the text in the UI.
6. Out-of-domain questions receive a polite refusal without any LLM call.

---

## Architecture

```
Text Input ──────────────────────────────────────────────────┐
                                                             ▼
Audio Input ──► Whisper STT ──► BART Domain Gate (≥0.70) ──► Groq LLM ──► gTTS ──► Gradio UI
                                        │
                                        └── (out of domain) ──► Refusal message
```

---

## Components

| Module | File | Technology |
|---|---|---|
| Speech-to-text | `app/speech_to_text.py` | OpenAI Whisper (`tiny`) |
| Domain gating | `app/natural_language_understanding.py` | HuggingFace BART-MNLI zero-shot |
| LLM inference | `app/large_language_model.py` | Groq API, Llama 3.1-8b-instant |
| Text-to-speech | `app/text_to_speech.py` | gTTS |
| UI | `app/gradio_user_interface.py` | Gradio |
| Entrypoint | `app/main.py` | Orchestrates the pipeline |

---

## Design decisions

- **Zero-shot classification over keyword matching.** Keyword lists require manual maintenance and fail on synonyms. BART-MNLI classifies by semantic meaning against a natural-language label (`"legal issues"`), which is more robust to question phrasing.
- **Groq API over a local LLM.** Running a capable local model (e.g., 7B+) requires GPU resources unavailable in a typical dev environment. Groq provides low-latency inference on a capable model with a free-tier API, keeping the prototype runnable on any machine.
- **Modular five-file structure.** Each concern (STT, NLU, LLM, TTS, UI) is a separate module so any component can be swapped independently.

---

## How to run

**Prerequisites:** Python 3.9+, `ffmpeg` installed on your system (`brew install ffmpeg` on macOS), a free [Groq API key](https://console.groq.com).

```bash
# 1. Clone
git clone https://github.com/itsalivafaei/Legal-AI-Assistant.git
cd Legal-AI-Assistant

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your Groq API key
cp .env.example .env
# Edit .env and replace the placeholder with your key

# 5. Run
python app/main.py
```

Gradio will print a local URL (e.g. `http://127.0.0.1:7860`) and an optional public share link. Open either in a browser.

---

## Docker

```bash
docker build -t legal-ai-assistant .
docker run -e GROQ_API_KEY=your_key_here -p 7860:7860 legal-ai-assistant
```

---

## Known limitations

- **No retrieval or grounding.** Answers come entirely from the base LLM's weights. The model can and does hallucinate. Do not use for actual legal advice.
- **No source citations.** Responses do not reference case law, statutes, or other primary sources.
- **Single-turn only.** The assistant has no conversation memory between turns.
- **Small Whisper model.** The `tiny` model is fast but less accurate than `base` or `small`, especially for noisy audio or non-standard accents.
- **TTS writes to disk.** Audio output overwrites `app/static/output.mp3` on every request; concurrent use is not supported.
- **Groq API dependency.** The system requires an active internet connection and a valid API key. There is no offline fallback.
