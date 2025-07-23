# 🗣️ Voice Assistant with Ollama + LangChain

This project provides two versions of an AI-powered voice assistant built using:
- **LangChain** for conversational context
- **Ollama** for running local LLMs like `phi`, `llama3`, etc.
- **SpeechRecognition + pyttsx3** for voice interaction
- **Streamlit** for web UI (in the web version)

---

## 📁 Folder Structure
```
voice_assistant/
├── ai_voice_assistant_terminal.py   # Terminal CLI version
├── ai_voice_assistant_web.py        # Streamlit Web UI version
└── README.md                        # Project overview and setup
```

---

## 💡 Features
| Feature                  | Terminal Version | Web Version |
|--------------------------|------------------|-------------|
| Voice Input              | ✅               | ✅          |
| AI Voice Response        | ✅               | ✅          |
| Conversational Memory    | ✅               | ✅          |
| LangChain Integration    | ✅               | ✅          |
| Streamlit Interface      | ❌               | ✅          |
| Terminal Console Output  | ✅               | ❌          |

---

## 🔧 Requirements
Make sure you have Python 3.8+ and install dependencies:

```bash
pip install streamlit pyttsx3 speechrecognition langchain langchain-community langchain-core langchain-ollama
```

### Additional setup for **pyttsx3**
- Windows: works out of the box.
- Linux: install `espeak` and `libespeak-dev`.
- Mac: uses `nsss` backend by default.

### Microphone Access
If you're running from terminal or Streamlit:
- Make sure your mic is connected and accessible.
- Grant permission to your terminal/browser if prompted.

---

## 🚀 Run Instructions

### ▶️ Terminal Version
```bash
python ai_voice_assistant_terminal.py
```

### 🧠 Streamlit Web Version
```bash
streamlit run ai_voice_assistant_web.py
```

Then open the provided URL in your browser (usually `http://localhost:8501`)

---

## 🤖 How It Works
- Uses **speech recognition** to capture the user's voice.
- Converts it to text and passes it to **LangChain** with past chat history.
- Gets an intelligent response from the **Ollama model** (like `phi`).
- Uses **TTS (pyttsx3)** to respond back with a voice.

---

## 🧠 Example Models to Use
You can switch the model by editing this line:
```python
llm = OllamaLLM(model="phi")
```
Other options:
- `llama3`
- `mistral`
- `gemma`
(Ensure the model is installed in your Ollama runtime)

---

## 📌 Credits
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [Streamlit](https://streamlit.io/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

---

## 📬 Contact
Built by Shivam Rathod – for feedback or issues, feel free to connect!
