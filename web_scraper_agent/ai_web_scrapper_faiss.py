import requests
from bs4 import BeautifulSoup
import streamlit as st
import faiss
import numpy as np
from langchain_ollama import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings  # Updated Import
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document

# Load AI Model
llm = OllamaLLM(model="phi")  # Change to "llama3" or another Ollama model

# Load Hugging Face Embeddings (Updated)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize FAISS Vector Database
index = faiss.IndexFlatL2(384)  # Vector dimension for MiniLM
vector_store = {}

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

        return text[:5000]  # Limit characters to avoid overloading AI
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Function to store data in FAISS
def store_in_faiss(text, url):
    global index, vector_store
    st.write("📥 Storing data in FAISS...")
    
    # Split text into chunks
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = splitter.split_text(text)

    # Convert text into embeddings
    vectors = embeddings.embed_documents(texts)
    vectors = np.array(vectors, dtype=np.float32)

    # Store in FAISS
    index.add(vectors)
    vector_store[len(vector_store)] = (url, texts)

    return "✅ Data stored successfully!"

# Function to retrieve relevant chunks and answer questions
def retrieve_and_answer(query):
    global index, vector_store

    # Convert query into embedding
    query_vector = np.array(embeddings.embed_query(query), dtype=np.float32).reshape(1, -1)

    # Search FAISS
    D, I = index.search(query_vector, k=2)  # Retrieve top 2 similar chunks

    context = ""
    for idx in I[0]:
        if idx in vector_store:
            context += " ".join(vector_store[idx][1]) + "\n\n"

    if not context:
        return "🤖 No relevant data found."

    # Ask AI to generate an answer
    return llm.invoke(f"Based on the following context, answer the question:\n\n{context}\n\nQuestion: {query}\nAnswer:")

# Streamlit Web UI
st.title("🤖 AI-Powered Web Scraper with FAISS Storage")
st.write("🔗 Enter a website URL below and store its knowledge for AI-based Q&A!")

# User input for website
url = st.text_input("🔗 Enter Website URL:")
if url:
    content = scrape_website(url)
    
    if "⚠️ Failed" in content or "❌ Error" in content:
        st.write(content)
    else:
        store_message = store_in_faiss(content, url)
        st.write(store_message)

# User input for Q&A
query = st.text_input("❓ Ask a question based on stored content:")
if query:
    answer = retrieve_and_answer(query)
    st.subheader("🤖 AI Answer:")
    st.write(answer)