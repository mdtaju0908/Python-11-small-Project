import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Configure API
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 AI Chatbot")

# Chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Input
user_input = st.text_input("Ask something...")

if st.button("Send"):
    if user_input:
        response = model.generate_content(user_input)

        # Save chat
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", response.text))

# Display chat
for sender, msg in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")