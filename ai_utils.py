# ==========================================
# MOCK MODE - Set to False for real APIs
# Set to True for offline testing (no API keys needed)
# ==========================================

USE_MOCK = False   # ← Keep False for real AI

import random
import os
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()

# --- Real API Imports ---
try:
    from google import genai
except ImportError:
    genai = None
    print("Please install google-genai: pip install google-genai")

try:
    from groq import Groq
except ImportError:
    Groq = None
    print("Please install groq: pip install groq")

# ============================================================
# STUDENT-FRIENDLY SYSTEM PROMPT
# ============================================================
SYSTEM_PROMPT = """You are a friendly, patient, and knowledgeable study assistant for students. Your goal is to help students learn, understand concepts, and solve academic problems.

You help with:
- Explaining difficult concepts in simple, easy-to-understand language
- Solving math, science, programming, or language problems step by step
- Providing study tips and effective learning techniques
- Helping students write and edit essays or assignments (guiding, not doing it for them)
- Clarifying doubts in any subject (Math, Science, English, History, Computer Science, etc.)
- Suggesting resources for further learning (books, websites, videos)

Always:
- Be patient, encouraging, and clear
- Break down complex ideas into simple steps
- Ask questions to guide students to the answer themselves (when appropriate)
- If you don't know something, admit it honestly and suggest where the student might find the answer
- NEVER give false information
- Keep your tone friendly, supportive, and motivating

Remember: You are here to HELP students learn, not to just give answers!"""

# ============================================================
# MAIN AI FUNCTION
# ============================================================
def get_ai_response(user_message, gemini_key, groq_key):
    # --- MOCK MODE (for testing without API keys) ---
    if USE_MOCK:
        user_lower = user_message.lower()
        if any(word in user_lower for word in ["math", "calculate", "solve", "equation"]):
            return "📐 Let's solve this together! I'll help you understand the steps. Can you show me what you've tried so far? I'm here to guide you, not just give the answer!"
        elif any(word in user_lower for word in ["essay", "write", "paragraph", "thesis"]):
            return "✍️ Great! Let's work on your essay. What's the topic? I'll help you outline your ideas and find the right structure for a strong essay."
        elif any(word in user_lower for word in ["science", "biology", "chemistry", "physics"]):
            return "🔬 Science is fascinating! I'll help you understand the concepts step by step. What specific topic or question do you have?"
        elif any(word in user_lower for word in ["program", "code", "python", "java", "function"]):
            return "💻 Nice! I'd love to help with coding. Can you share your code or explain what you're trying to build? I'll guide you to the solution."
        elif any(word in user_lower for word in ["hello", "hi", "hey"]):
            return random.choice([
                "👋 Hello there! I'm your Study Buddy. What would you like to learn today?",
                "Hi! Ready to explore something new? Ask me anything about your studies!",
                "Hey! Great to see you studying. What can I help you with today?"
            ])
        elif any(word in user_lower for word in ["thank", "thanks"]):
            return "😊 You're welcome! I'm always here to help. Keep up the great work!"
        else:
            return f"📚 Great question! Let me help you with that. \n\nI'm here to guide you through learning. Could you tell me more about what you're studying and what you're struggling with?"

    # ============================================================
    # REAL API CODE (runs when USE_MOCK = False)
    # ============================================================
    
    # Combine keys: user-provided first, then .env as fallback
    final_gemini = gemini_key if gemini_key else os.getenv("GEMINI_API_KEY", "")
    final_groq = groq_key if groq_key else os.getenv("GROQ_API_KEY", "")

    error_log = []

    # --- Try Gemini (Primary) ---
    if final_gemini and final_gemini.strip() and genai:
        try:
            client = genai.Client(api_key=final_gemini.strip())
            response = client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=f"{SYSTEM_PROMPT}\n\nStudent: {user_message}"
            )
            return response.text
        except Exception as e:
            error_log.append(f"Gemini: {str(e)[:60]}")
            print(f"Gemini failed: {e}")

    # --- Try Groq (Fallback) ---
    if final_groq and final_groq.strip() and Groq:
        try:
            client = Groq(api_key=final_groq.strip())
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_message}
                ],
                model="llama-3.3-70b-versatile",
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            error_log.append(f"Groq: {str(e)[:60]}")
            print(f"Groq failed: {e}")

    # --- If both fail ---
    if error_log:
        return f"⚠️ I'm having trouble connecting right now. Errors: {', '.join(error_log)}\n\n💡 Tips:\n1. Check your API keys in the sidebar\n2. Make sure you have internet connection\n3. Try again in a moment"
    
    return "⚠️ No API keys found. Please enter your Gemini or Groq API keys in the sidebar."