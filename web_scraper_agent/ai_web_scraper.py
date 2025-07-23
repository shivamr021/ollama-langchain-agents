import requests
from bs4 import BeautifulSoup
import streamlit as st
from langchain_ollama import OllamaLLM

# Load AI Model
llm = OllamaLLM(model="phi")  # Change to "llama3" or another model if needed

# Function to scrape a website
def scrape_website(url):
    try:
        st.write(f"🌍 Scraping website: {url}")
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            return f"⚠️ Failed to fetch {url}"
        
        # Extract text content
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])

        return text[:2000]  # Limit characters to avoid overloading AI
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Function to summarize content using AI
def summarize_content(content):
    st.write("✍️ Summarizing content...")
    return llm.invoke(f"Summarize the following content:\n\n{content[:1000]}")  # Limit to 1000 chars

# Streamlit Web UI
st.title("🤖 AI-Powered Web Scraper")
st.write("Enter a website URL below and get a summarized version!")

# User input
url = st.text_input("🔗 Enter Website URL:")
if url:
    content = scrape_website(url)
    
    if "⚠️ Failed" in content or "❌ Error" in content:
        st.write(content)
    else:
        summary = summarize_content(content)
        st.subheader("📄 Website Summary")
        st.write(summary)