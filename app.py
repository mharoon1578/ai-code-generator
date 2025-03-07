import os
import streamlit as st
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "mixtral-8x7b-32768"

# Initialize chat memory in session state
if "chat_memory" not in st.session_state:
    st.session_state.chat_memory = [
        {"role": "system", "content": "You are an AI coding assistant. Respond only with programming-related answers."}
    ]

# Function to extract code and explanation
def extract_code_and_explanation(text):
    if "```" in text:
        parts = text.split("```")
        explanation = parts[0].strip()
        lang = parts[1].split("\n")[0].strip()
        code = "\n".join(parts[1].split("\n")[1:]).strip()
        return explanation, lang, code
    return text.strip(), "plaintext", ""

# Function to generate a response using Groq API
def generate_code(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    messages = st.session_state.chat_memory + [{"role": "user", "content": prompt}]

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.6,
        "max_tokens": 2000
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        st.session_state.chat_memory.append({"role": "assistant", "content": reply})
        return reply
    else:
        return f"Error: {response.status_code}, {response.json()}"

# Streamlit UI setup
st.set_page_config(page_title="AI Code Assistant", page_icon="🤖")

# Custom CSS for better UI
st.markdown("""
    <style>
        .stChatMessage {
            background-color: #1E1E1E;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .stTextInput, .stTextArea {
            border-radius: 10px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("💬 AI Code Assistant")
st.write("Chat with AI to generate, optimize, and debug code.")

# Display chat history
for chat in st.session_state.chat_memory[1:]:
    with st.chat_message("user" if chat["role"] == "user" else "assistant"):
        explanation, lang, code = extract_code_and_explanation(chat["content"])
        st.write(explanation)
        if code:
            st.code(code, language=lang)

# User input box
prompt = st.chat_input("Type your request here...")

# Process user input
if prompt:
    st.session_state.chat_memory.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.write(prompt)

    ai_response = generate_code(prompt)

    with st.chat_message("assistant"):
        explanation, lang, code = extract_code_and_explanation(ai_response)
        st.write(explanation)
        if code:
            st.code(code, language=lang)