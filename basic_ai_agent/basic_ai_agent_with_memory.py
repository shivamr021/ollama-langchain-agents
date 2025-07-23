from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Load AI Model
llm = OllamaLLM(model="phi")

# Initialize chat message history
chat_history = ChatMessageHistory()

# Define a prompt template
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template = "Previous conversation: {chat_history}\n\nUser's question: {question}\n\nAI's response:"
)

# Function to run AI chat with memory
def run_chain(question):
    # Retrieve chat history manually
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content})" for msg in chat_history.messages])

    # Run the AI response generation
    response = llm.invoke(prompt.format(chat_history=chat_history_text, question=question))

    # Store new user input and AI response in chat history
    chat_history.add_user_message(question)
    chat_history.add_ai_message(response)

    return response

# Interactive CLI Chatbot
print("AI Chatbot with Memory")
print("Type 'exit' to stop the chatbot.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Exiting the chatbot. Goodbye!")
        break

    ai_response = run_chain(user_input)
    print(f"AI: {ai_response}")