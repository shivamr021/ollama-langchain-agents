from langchain_ollama import OllamaLLM

# Load AI model from Ollama
llm = OllamaLLM(model="phi")

print("Welcome to your AI Agent! Ask me anything.")

while True:
    question = input("Your question (or type 'exit' to stop): ")
    if question.lower() == 'exit':
        print("Exiting the AI Agent. Goodbye!")
        break
    response = llm.invoke(question)
    print(f"AI Response: {response}")