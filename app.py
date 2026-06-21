import streamlit as st

# --- Must be the first Streamlit command ---
st.set_page_config(page_title="Student AI Chatbot", page_icon="📚", layout="centered")

# --- Initialize session state ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "gemini_key" not in st.session_state:
    st.session_state.gemini_key = ""
if "groq_key" not in st.session_state:
    st.session_state.groq_key = ""

# --- Import and show chat page ---
from pages.chat import show_chat
show_chat()