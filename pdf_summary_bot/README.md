# 📄 PDF Summary Bot

This module provides Streamlit-based apps that let you interact with PDF documents using voice or text. You can upload PDFs, ask questions based on their content, and even generate AI-powered summaries — all using local LLMs from Ollama.

---

## 📁 Files

| File Name             | Description |
|-----------------------|-------------|
| `app_basic_qa.py`     | Upload a PDF and ask questions. Uses FAISS + local LLM for document Q&A. |
| `app_summary_qa.py`   | Adds document summarization and summary download on top of Q&A. |

---

## 🧠 Features

### ✅ Common Features
- PDF Upload & Text Extraction
- Embedding via HuggingFace MiniLM
- FAISS-powered vector search
- Ollama LLM response generation
- Streamlit user interface

### ✨ Extra in `app_summary_qa.py`
- AI-generated document summary
- Summary download as `.txt`

---

## 🚀 How to Run

```bash
streamlit run app_basic_qa.py
# or
streamlit run app_summary_qa.py
````

> 📌 Make sure your local Ollama server is running and the `phi` or other model is available.

---

## 🔧 Requirements

* `streamlit`
* `faiss-cpu`
* `PyPDF2`
* `langchain`
* `langchain-ollama`
* `langchain-huggingface`
* `sentence-transformers`

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧩 Tips

* You can switch the model in both apps:

  ```python
  llm = OllamaLLM(model="phi")  # Replace with "llama3" or others
  ```
* FAISS indexing is in-memory and resets on every run. Use persistent FAISS if you need longer sessions.

---

## 🏗️ Folder Integration

This module is part of the larger `AI AGENT` project, alongside:

* `voice_assistant/`
* `basic_ai_agent/`
* `web_scraper_agent/`

See the root README for a project overview.
