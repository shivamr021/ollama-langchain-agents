# ===============================
# Streamlit Version: ai_voice_assistant_web.py
# ===============================

import streamlit as st
import speech_recognition as sr
import pyttsx3
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Load Ollama Model
llm = OllamaLLM(model="phi")  # You can switch to "llama3" or others

# Initialize LangChain memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatMessageHistory()

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty("rate", 160)

# Initialize Speech Recognizer
recognizer = sr.Recognizer()

# AI prompt template
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="Previous conversation:\n{chat_history}\nUser: {question}\nAI:"
)

# Function to speak
def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        st.error(f"TTS Error: {e}")

# Function to listen
def listen():
    with sr.Microphone() as source:
        st.write("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        st.write(f"👂 You Said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        st.warning("😕 Sorry, I couldn't understand. Try again!")
    except sr.RequestError:
        st.error("⚠️ Speech Recognition Service Unavailable")
    return ""

# Function to process AI response
def run_chain(question):
    chat_history_text = "\n".join([
        f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.messages
    ])
    response = llm.invoke(prompt.format(chat_history=chat_history_text, question=question))
    st.session_state.chat_history.add_user_message(question)
    st.session_state.chat_history.add_ai_message(response)
    return response

# ===================== Streamlit UI ===================== #

st.title("🧠🎙️ AI Voice Assistant (Web UI)")
st.write("🗣️ Click the button below to speak to your AI assistant!")

if st.button("🎤 Start Listening"):
    user_query = listen()
    if user_query:
        ai_response = run_chain(user_query)
        st.write(f"🧍‍♂️ **You:** {user_query}")
        st.write(f"🤖 **AI:** {ai_response}")
        speak(ai_response)

# Show Chat History
st.subheader("📜 Chat History")
for msg in st.session_state.chat_history.messages:
    st.write(f"**{msg.type.capitalize()}**: {msg.content}")
# ===============================