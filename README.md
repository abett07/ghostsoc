# 👻 GhostSOC

> 🔐 AI-Powered Cyber Deception and Adaptive Incident Response System  
> Powered by LLaMA + FastAPI + Streamlit

---

## 🎯 Overview

**GhostSOC** is an advanced, self-adaptive deception and response system that simulates realistic Linux environments using local LLaMA models (via Ollama) to interact with attackers in real time.

It helps defenders **trap attackers**, **log behavior**, and **simulate fake vulnerabilities** to **waste attacker time** and study tactics.

---

## 🧠 Core Features

- 🎭 **LLM-Powered Fake Terminal** – Dynamic deception via locally hosted LLaMA (Ollama)
- ⚡ **FastAPI Backend** – Secure `/simulate` endpoint for attacker inputs
- 📊 **Streamlit Dashboard** – Real-time terminal interface + attacker history
- 🕵️ **Session Logger** – Stores all attacker commands + LLM responses in JSON
- 🔒 Self-hosted – No external API required (offline-ready)

---

## ⚙️ Tech Stack

| Layer      | Tools                                 |
|------------|----------------------------------------|
| Deception  | LLaMA 3 via [Ollama](https://ollama.com) |
| Backend    | FastAPI, Python                        |
| Frontend   | Streamlit                              |
| Logging    | JSON-based session logger              |
| Versioning | Git & GitHub                           |

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/Abett07/ghostsoc.git
cd ghostsoc
