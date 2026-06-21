import streamlit as st
import os
from dotenv import load_dotenv
from ai_utils import get_ai_response

load_dotenv()
HAS_ENV_KEYS = bool(os.getenv("GEMINI_API_KEY") or os.getenv("GROQ_API_KEY"))

def show_chat():
    st.markdown("""
        <style>
        .stApp {
            background-color: #0a0a0a !important;
        }
        
        /* ---------- Header: Orange Gradient ---------- */
        .chat-header {
            background: linear-gradient(135deg, #d35400, #e67e22) !important;
            padding: 18px 20px;
            border-radius: 12px;
            color: white;
            margin-bottom: 25px;
            border-bottom: 2px solid #f39c12;
            box-shadow: 0 4px 20px rgba(211, 84, 0, 0.4);
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .chat-header h3 {
            margin: 0;
            font-size: 24px;
            font-weight: 700;
            color: #fff;
        }
        .chat-header .sub-header {
            font-size: 14px;
            color: #fdebd0;
            margin: 0;
        }
        
        /* ---------- Message Bubbles ---------- */
        .message-bubble {
            padding: 12px 16px;
            border-radius: 14px;
            display: inline-block;
            max-width: 80%;
            text-align: left;
            line-height: 1.6;
            margin-bottom: 2px;
        }
        .message-wrapper {
            display: flex;
            align-items: flex-start;
            gap: 10px;
            margin: 10px 0;
        }
        .message-wrapper.user {
            justify-content: flex-end;
        }
        .message-wrapper.bot {
            justify-content: flex-start;
        }
        
        /* ---------- Icons ---------- */
        .message-icon {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            flex-shrink: 0;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            overflow: hidden;
        }
        .message-icon.bot-icon {
            background: rgba(211, 84, 0, 0.2);
            border-color: rgba(211, 84, 0, 0.4);
        }
        .message-icon.user-icon {
            background: rgba(39, 174, 96, 0.2);
            border-color: rgba(39, 174, 96, 0.4);
        }
        .message-icon svg {
            width: 24px;
            height: 24px;
        }
        
        /* ---------- Bot Message (Orange accent) ---------- */
        .bot-message {
            background-color: #2c1a0e;
            color: #fdf2e9;
            border: 1px solid #d35400;
        }
        .bot-message .sender-name {
            color: #f39c12;
            font-weight: 600;
            font-size: 13px;
            display: block;
            margin-bottom: 4px;
        }
        
        /* ---------- User Message (Green accent) ---------- */
        .user-message {
            background-color: #0e2a1a;
            color: #eafaf1;
            border: 1px solid #27ae60;
        }
        .user-message .sender-name {
            color: #2ecc71;
            font-weight: 600;
            font-size: 13px;
            display: block;
            margin-bottom: 4px;
            text-align: right;
        }
        
        /* ---------- Chat Input ---------- */
        .stChatInput {
            background-color: #1a1a1a !important;
            border: 1px solid #d35400 !important;
            border-radius: 10px !important;
        }
        .stChatInput > div > input {
            background-color: #1a1a1a !important;
            color: white !important;
            padding: 12px 16px !important;
            font-size: 15px !important;
        }
        .stChatInput > div > input::placeholder {
            color: #888 !important;
        }
        .stChatInput > div > input:focus {
            border-color: #f39c12 !important;
            box-shadow: 0 0 0 2px rgba(211, 84, 0, 0.3) !important;
        }
        
        /* ------------------------------------------------------------ */
        /* ✅ FIXED: Only hide the footer (not the header/menu)         */
        /* This keeps the hamburger menu visible on mobile.            */
        /* ------------------------------------------------------------ */
        footer { visibility: hidden; }
        /* #MainMenu and header are NOT hidden – they stay visible */
        </style>
    """, unsafe_allow_html=True)

    # ============================================================
    # SIDEBAR - API Keys
    # ============================================================
    with st.sidebar:
        st.markdown("##  Study Assistant")
        st.markdown("---")
        st.markdown("### 🔑 API Keys")
        
        if HAS_ENV_KEYS:
            st.success("✅ API Keys loaded from .env")
        
        has_session_keys = bool(st.session_state.get("gemini_key") or st.session_state.get("groq_key"))
        if has_session_keys:
            st.info("✅ Keys are saved in this session.")
        
        with st.form("api_keys_form"):
            gemini = st.text_input(
                "Gemini API Key",
                type="password",
                placeholder="Enter your Gemini key...",
                value=st.session_state.get("gemini_key", "")
            )
            groq = st.text_input(
                "Groq API Key",
                type="password",
                placeholder="Enter your Groq key...",
                value=st.session_state.get("groq_key", "")
            )
            submitted = st.form_submit_button("💾 Save Keys")
        
        if submitted:
            if gemini or groq:
                st.session_state.gemini_key = gemini
                st.session_state.groq_key = groq
                st.success("✅ Keys saved successfully!")
                st.rerun()
            else:
                st.error("Please enter at least one API key.")
        
        st.markdown("---")
        st.markdown("### 💡 How to use")
        st.markdown("""
        1. Enter your API keys above
        2. Type your question
        3. Press Enter
        
        **Ask about:**
        - 📖 Any subject
        - 🧮 Math & Science
        - 💻 Programming
        - ✍️ Essay help
        - 📝 Study tips
        """)
        
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

    # ============================================================
    # HEADER – with SVG Book Icon
    # ============================================================
    st.markdown("""
        <div class="chat-header">
            <div style="display: flex; align-items: center; gap: 10px;">
                <!-- SVG Book Icon -->
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
                    <line x1="8" y1="7" x2="16" y2="7"/>
                    <line x1="8" y1="11" x2="14" y2="11"/>
                </svg>
                <div>
                    <h3>Student Study Assistant</h3>
                    <p class="sub-header">🎯 Learn, understand, and grow 24/7</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ============================================================
    # DISPLAY CHAT MESSAGES
    # ============================================================
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"""
                <div class="message-wrapper user">
                    <div style="text-align: right; max-width: 85%;">
                        <div class="message-bubble user-message">
                            <span class="sender-name"> You</span>
                            {msg["content"]}
                        </div>
                    </div>
                    <div class="message-icon user-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2ecc71" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                            <circle cx="12" cy="7" r="4"/>
                        </svg>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="message-wrapper bot">
                    <div class="message-icon bot-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#f39c12" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 2a2 2 0 0 1 2 2c0 .74-.4 1.39-1 1.73V7h1a7 7 0 0 1 7 7h1a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v1a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-1H2a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1h1a7 7 0 0 1 7-7h1V5.73c-.6-.34-1-.99-1-1.73a2 2 0 0 1 2-2z"/>
                            <circle cx="7.5" cy="15.5" r="1.5" fill="#f39c12"/>
                            <circle cx="16.5" cy="15.5" r="1.5" fill="#f39c12"/>
                        </svg>
                    </div>
                    <div style="max-width: 85%;">
                        <div class="message-bubble bot-message">
                            <span class="sender-name"> Study Buddy</span>
                            {msg["content"]}
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # ============================================================
    # INPUT (uses st.chat_input)
    # ============================================================
    user_input = st.chat_input(
        placeholder="💬 Ask me anything about your studies...",
        key="chat_input"
    )

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        gemini_key = st.session_state.get("gemini_key", "")
        groq_key = st.session_state.get("groq_key", "")

        if not gemini_key and not groq_key and HAS_ENV_KEYS:
            gemini_key = os.getenv("GEMINI_API_KEY", "")
            groq_key = os.getenv("GROQ_API_KEY", "")

        with st.spinner(" Study Buddy is thinking..."):
            bot_reply = get_ai_response(user_input, gemini_key, groq_key)

        st.session_state.messages.append({"role": "bot", "content": bot_reply})
        st.rerun()