# ===============================
# Terminal Version: ai_voice_assistant_terminal.py
# ===============================

import speech_recognition as sr
import pyttsx3
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Load Model
llm = OllamaLLM(model="phi")  # Change to "llama3" or other supported model

# Initialize memory
chat_history = ChatMessageHistory()

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty("rate", 160)

# Initialize recognizer
recognizer = sr.Recognizer()

# AI prompt template
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="Previous conversation:\n{chat_history}\nUser: {question}\nAI:"
)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        print("😕 Could not understand audio.")
    except sr.RequestError:
        print("⚠️ Speech Recognition service unavailable.")
    return ""

def run_chain(question):
    history_text = "\n".join([
        f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages
    ])
    response = llm.invoke(prompt.format(chat_history=history_text, question=question))
    chat_history.add_user_message(question)
    chat_history.add_ai_message(response)
    return response

if __name__ == "__main__":
    print("🤖 AI Voice Assistant (Terminal Mode)")
    print("Speak to ask a question. Say 'exit' to quit.")

    while True:
        user_query = listen()
        if not user_query:
            continue
        if "exit" in user_query:
            print("👋 Goodbye!")
            break

        print(f"🧍‍♂️ You: {user_query}")
        ai_response = run_chain(user_query)
        print(f"🤖 AI: {ai_response}\n")
        speak(ai_response)
        print("🎤 Ask another question or say 'exit' to quit.")
# ===============================