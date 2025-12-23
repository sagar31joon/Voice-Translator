# Hindi-to-English Real-Time Voice Translator

## Overview

This project implements a **real-time Hindi-to-English voice translation pipeline**.
It captures live audio from the microphone, transcribes Hindi speech using an offline ASR model, and translates the transcribed text into English — **without saving any audio files**.

The system is designed as a **streaming pipeline**, focusing on clean architecture, modularity, and low latency.

---

## Key Features

* 🎤 **Real-time microphone streaming**
* 🗣️ **Offline Hindi speech recognition** using Vosk
* 🌐 **Hindi → English text translation** using MarianMT
* 🚫 **No intermediate WAV files**
* 🧩 Clean separation of concerns (I/O, ASR, Translation, Pipeline)
* ⚡ Event-based translation on sentence boundaries

---

## Architecture

```
Microphone
   ↓
Raw PCM Audio Stream
   ↓
Vosk Streaming ASR (Hindi)
   ↓
Sentence Finalization
   ↓
Text Translation (Hindi → English)
   ↓
English Text Output
```

---

## Project Structure

```
HTE_translator/
├── main.py                 # Entry point
├── core/
│   ├── pipeline.py         # Orchestrates streaming pipeline
│   ├── stt.py              # Vosk streaming speech-to-text
│   └── translator.py       # Hindi → English translation
├── io_layer/
│   └── mic_stream.py       # Real-time microphone input
├── models/
│   └── vosk/vosk-small-hi/ # Hindi ASR model
└── venv/
```

---

## Tech Stack

* **Python 3.10+**
* **Vosk** — Offline streaming speech recognition
* **HuggingFace Transformers** — MarianMT translation model
* **SoundDevice** — Real-time audio capture

---

## Setup Instructions

### 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
```

### 2. Install dependencies

```bash
install the requirements.txt file
```

### 3. Download Hindi Vosk model

Download from:

```
https://alphacephei.com/vosk/models
```

Extract and place it here:

```
models/vosk/vosk-small-hi/
```

Ensure the directory contains:

```
am/ conf/ graph/ ivector/
```

---

## Running the Project

```bash
python main.py
```

* Speak Hindi into the microphone
* Pause briefly after each sentence
* The English translation will be printed in real time
* Press **Ctrl+C** to stop

---

## Example Output

```
Hindi: क्या कर रहे हो
English: What are you doing?
```

---

## Design Notes

* Speech recognition is **fully offline**
* Translation is performed only after sentence finalization to avoid partial outputs
* The system is modular and easily extensible to other languages or models

---

## Known Limitations

* Sentence-level translation only (no conversational context)
* Proper nouns and ambiguous Hindi constructions may translate incorrectly
* Translation quality depends on the pretrained MT model

These are known trade-offs of lightweight, offline-first pipelines.

---

## Possible Improvements

* Named Entity Recognition (NER) to preserve proper nouns
* Context-aware translation using LLMs
* Confidence scoring for ASR output
* WebSocket / REST API interface

---

## Author

Sagar Joon
# Voice-Translator
