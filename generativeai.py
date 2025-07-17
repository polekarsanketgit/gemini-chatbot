#===============================================
#   To run this code run below line in terminal 
#   python -m streamlit run generativeai.py 
#===============================================

import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load Gemini API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Use the Gemini 1.5 Flash model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Streamlit app settings
st.set_page_config(page_title="💬 Chat with Gemini 1.5 Flash", layout="centered")
st.title("💡 Chat with Gemini 1.5 Flash")

# Sidebar for Clear Chat
with st.sidebar:
    st.subheader("⚙️ Options")
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show chat history
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# Input box for new message
prompt = st.chat_input("Ask something...")

if prompt:
    # Show user message
    st.chat_message("user").markdown(prompt)
    st.session_state.chat_history.append(("user", prompt))

    # Build prompt parts from history
    history_parts = [
        {"role": "user", "parts": [msg]} if role == "user" else {"role": "model", "parts": [msg]}
        for role, msg in st.session_state.chat_history
    ]

    # Get Gemini response
    with st.chat_message("assistant"):
        with st.spinner("Gemini is thinking..."):
            try:
                response = model.generate_content(history_parts)
                reply = response.text
                st.markdown(reply)
                st.session_state.chat_history.append(("assistant", reply))
            except Exception as e:
                st.error(f"❌ Gemini error: {e}")
