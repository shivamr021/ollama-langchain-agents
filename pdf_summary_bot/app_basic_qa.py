# app_basic_qa.py

import streamlit as st
import faiss
import numpy as np
import PyPDF2
from langchain_ollama import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter

# Load AI Model
llm = OllamaLLM(model="phi")  # Can also use "llama3" etc.

# Load Hugging Face Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize FAISS Vector Database
index = faiss.IndexFlatL2(384)  # Vector dimension for MiniLM
vector_store = {}

# Function to extract text from PDFs
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# Function to store text in FAISS
def store_in_faiss(text, filename):
    global index, vector_store
    st.write(f"📥 Storing document '{filename}' in FAISS...")

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(text)
    vectors = np.array(embeddings.embed_documents(chunks), dtype=np.float32)

    index.add(vectors)
    vector_store[len(vector_store)] = (filename, chunks)

    return "✅ Document stored successfully!"

# Function to retrieve relevant chunks and answer questions
def retrieve_and_answer(query):
    query_vector = np.array(embeddings.embed_query(query), dtype=np.float32).reshape(1, -1)
    D, I = index.search(query_vector, k=2)

    context = ""
    for idx in I[0]:
        if idx in vector_store:
            context += " ".join(vector_store[idx][1]) + "\n\n"

    if not context.strip():
        return "🤖 No relevant data found in stored documents."

    return llm.invoke(f"Based on the following document context, answer the question:\n\n{context}\n\nQuestion: {query}\nAnswer:")

# Streamlit UI
st.title("📄 AI PDF Q&A App (Basic)")
st.write("Upload a PDF and ask questions based on its content.")

uploaded_file = st.file_uploader("📂 Upload a PDF Document", type=["pdf"])
if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    store_message = store_in_faiss(text, uploaded_file.name)
    st.write(store_message)

query = st.text_input("❓ Ask a question based on the uploaded document:")
if query:
    answer = retrieve_and_answer(query)
    st.subheader("🤖 AI Answer:")
    st.write(answer)