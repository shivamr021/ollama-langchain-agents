# 🧠 AI Agent Projects with Ollama + LangChain

This repository showcases my hands-on projects while learning about **AI Agents** using [LangChain](https://www.langchain.com/), [Ollama](https://ollama.com), and Python. It includes both minimal setups and advanced interactive applications that demonstrate real-world agent use cases like memory handling, voice interaction, and local LLM inference.

---

## 📁 Folder Structure

```bash
.
├── basic_ai_agent/        # Basic text agent with and without memory
│   ├── basic_ai_agent.py
│   ├── basic_ai_agent_with_memory.py
│   ├── streamlit_app.py
│   ├── requirements.txt
│   └── README.md
│
├── pdf_summary_bot/       # QA-based PDF summarizer agent
│   ├── app_basic_qa.py
│   ├── app_summary_qa.py
│   ├── requirements.txt
│   └── README.md
│
├── voice_assistant/       # Voice assistant with terminal + Streamlit UI
│   ├── ai_voice_assistant_and_streamlit_app.py
│   ├── streamlit_app.py
│   ├── requirements.txt
│   └── README.md
│
├── web_scraper_agent/     # Agent that scrapes data using tools + memory
│   ├── ai_web_scraper.py
│   ├── ai_web_scrapper_faiss.py
│   ├── requirements.txt
│   └── README.md
│
├── .gitignore
├── README.md               # ← You are here
└── requirements.txt        # Master requirements for full repo
```

---

## 🔧 Tech Stack

| Feature             | Library/Tool                   |
| ------------------- | ------------------------------ |
| LLM Inference       | [Ollama](https://ollama.com)   |
| Language Agent APIs | LangChain, LangChain Community |
| Web UI              | Streamlit                      |
| Voice I/O           | SpeechRecognition, pyttsx3     |
| Parsing & Memory    | FAISS, LangChain Memory        |

---

## 🎓 Projects Overview

### 1. `basic_ai_agent/` – Basic LLM Agent

Minimal examples to:

* Load local LLMs (like `phi`, `mistral`, etc.) via Ollama
* Run single-turn and memory-supported agents
* Try a web UI version with Streamlit

### 2. `pdf_summary_bot/` – PDF QA Agent

Ask questions or summarize based on uploaded PDF content:

* `app_basic_qa.py`: Basic question answering
* `app_summary_qa.py`: Summary-focused version

### 3. `voice_assistant/` – Voice-Based LLM Chat

Talk to your LLM with:

* A terminal-based CLI voice chat
* A full Streamlit-based voice chat UI

### 4. `web_scraper_agent/` – Web Scraping AI Agent

Give queries like "Find top Python tutorials" and get results scraped live:

* `ai_web_scraper.py`: Basic tool-based agent
* `ai_web_scrapper_faiss.py`: Uses memory and FAISS for smarter recall

---

## ⚡ Getting Started

1. **Clone this repo**

   ```bash
   git clone https://github.com/your-username/ai-agent-projects.git
   cd ai-agent-projects
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Make sure Ollama is running**

   ```bash
   ollama run phi
   ```

4. **Run a project**

   ```bash
   cd voice_assistant
   python ai_voice_assistant_and_streamlit_app.py
   # OR
   streamlit run streamlit_app.py
   ```

---

## 📜 Requirements

Each folder includes its own `requirements.txt`, but a master file is available at root if you want to install everything together.

* Python 3.9+
* Ollama running locally with a model like `phi`, `mistral`, or `llama2`
* Microphone + speaker (for voice apps)

---

## ✨ Credits

* [LangChain](https://www.langchain.com/) for the powerful agent ecosystem
* [Ollama](https://ollama.com) for local, private LLM serving
* [Streamlit](https://streamlit.io) for interactive UIs

---

## 📚 License

This repo is for educational purposes. MIT License. Feel free to fork, use, and modify with attribution.

---

## 🚀 What's Next?

* Add file upload / PDF reading support
* Build a full research assistant
* Experiment with tools, memory, and agents

Pull requests and suggestions are welcome!
