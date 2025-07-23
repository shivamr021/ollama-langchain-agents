# 🕸️ AI-Powered Web Scraper Agent

This project is an advanced AI-powered web scraping assistant that extracts information from a website and either:

* Summarizes it using a local language model (like `phi` or `llama3` via Ollama), **or**
* Stores it in a FAISS vector database with embeddings (MiniLM) for **context-aware Q\&A**.

> 🚀 Built using Streamlit, BeautifulSoup, FAISS, and LangChain integrations with Ollama & HuggingFace.

---

## 🧠 Features

### 🔹 Basic Version

* Scrapes the content (mainly `<p>` tags) from a given URL.
* Summarizes the content using an LLM via `OllamaLLM` (e.g. `phi`, `llama3`).
* Runs in a clean and interactive Streamlit web UI.

### 🔹 Advanced Version (Vector DB Q\&A)

* Scrapes the content and splits it into chunks using LangChain `CharacterTextSplitter`.
* Embeds the chunks using HuggingFace (`MiniLM-L6-v2`).
* Stores vectors in a FAISS vector store.
* Accepts user questions and retrieves the top-k relevant context.
* Uses local LLM to generate answers based on the context.

---

## 📂 Folder Structure

```
web_scrapper_agent/
├── web_scraper_basic.py          # Summarizes scraped content
├── web_scraper_faiss_agent.py   # Stores data in FAISS and enables Q&A
├── README.md
├── requirements.txt
```

---

## 💻 How to Run

### 1. Activate Your Virtual Environment (if applicable):

```bash
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Basic Web Scraper

```bash
streamlit run web_scraper_basic.py
```

### 4. Run FAISS + Q\&A Web Agent

```bash
streamlit run web_scraper_faiss_agent.py
```

---

## 🧪 Example

### Input URL:

```
https://en.wikipedia.org/wiki/Natural_language_processing
```

### Ask a Question (Advanced Version):

```
What are the main applications of NLP?
```

---

## 🧰 Tech Stack

| Tool                   | Purpose                        |
| ---------------------- | ------------------------------ |
| Streamlit              | Web UI                         |
| BeautifulSoup          | HTML parsing                   |
| Requests               | Website HTTP fetch             |
| FAISS                  | Vector similarity search       |
| HuggingFace Embeddings | Vector creation                |
| Ollama                 | Local LLM backend (e.g. `phi`) |
| LangChain              | Modular LLM orchestration      |


---

## 📌 Notes

* You can switch the LLM from `phi` to `llama3` or others if installed via Ollama.
* FAISS stores are ephemeral in memory by default in this script; add persistence if needed.
* Make sure to limit the content size sent to LLM to prevent overloading.

---

## 🧠 Future Improvements

* Add persistent FAISS storage to disk.
* Add metadata and better chunk tracking.
* Enhance web page cleaning with readability libraries.

---

## 🏁 Credits

* Developed as part of the **AI Agents Bootcamp (Local Ollama Edition)**.
* Vector store and LLM workflow inspired by LangChain architecture.

---
