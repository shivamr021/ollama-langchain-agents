# 🤖 Basic AI Agent

This folder contains basic examples of LangChain-powered AI agents using Ollama LLMs.

## Files

- `basic_ai_agent.py` — Stateless prompt-response agent.
- `basic_ai_agent_with_memory.py` — Adds conversational memory.
- `streamlit_app.py` — Web UI for basic agent interaction.

## Features

- Simple LLM-based response generation
- Chat memory support
- Optional Streamlit interface

## How to Run

### CLI
```bash
python basic_ai_agent.py
```

## With Memory
```bash
python basic_ai_agent_with_memory.py
```

## Streamlit Web App
```bash
streamlit run streamlit_app.py
```

## Model Used
```python
llm = OllamaLLM(model="phi")
```

You can replace "phi" with "llama3", "mistral", etc., depending on what you've installed in Ollama.