## 📚 README for Student Study Assistant Chatbot

Here is a **complete, ready-to-use README** for your student chatbot project.

---

### 📄 `README.md` (Copy & Paste)

```markdown
# 🍊 Student Study Assistant – AI-Powered Learning Companion

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A smart, conversational AI study assistant built with **Streamlit** and powered by **Google Gemini AI** (primary) and **Groq API** (fallback). It helps students understand concepts, solve problems, and get study tips – all through an interactive chat interface.

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Configuration](#-configuration)
- [Usage Guide](#-usage-guide)
- [Deployment](#-deployment)
- [Color Scheme & UI](#-color-scheme--ui)
- [Screenshots](#-screenshots)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**Student Study Assistant** is a conversational AI designed to help learners of all ages. It provides instant, personalised support across a wide range of subjects – from mathematics and science to programming, essay writing, and exam preparation.

**Why this project?**  
Many students struggle to find quick, accurate help when studying. This chatbot offers a 24/7 study companion that explains concepts in simple terms, guides problem‑solving, and encourages independent learning.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **AI-Powered Responses** | Uses Google Gemini AI (primary) and Groq (fallback) for intelligent, context‑aware replies. |
| 🎓 **Subject‑agnostic** | Supports Math, Science, Programming, English, History, and more. |
| 💬 **Real‑time Chat** | Seamless, message‑based interaction with a clean, intuitive interface. |
| 🔐 **Secure API Key Management** | Keys can be stored in a `.env` file or entered directly via the sidebar. |
| 🎨 **Modern UI** | Dark theme with warm orange & green accents – easy on the eyes during late‑night study sessions. |
| 📱 **Mobile‑friendly** | Fully responsive; sidebar accessible via hamburger menu on phones. |
| 🧪 **Mock Mode** | Test offline with predefined responses (great for demos). |
| 🗑️ **Clear Chat** | One‑click to reset the conversation history. |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend / Backend | **Streamlit** (Python) |
| Primary AI API | **Google Gemini** (`gemini-2.0-flash-exp`) |
| Fallback AI API | **Groq** (`llama-3.3-70b-versatile`) |
| Environment Management | `python-dotenv` |
| Deployment | **Streamlit Community Cloud** |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```
student_chatbot/
│
├── app.py                 # Main entry point – starts the chat interface
├── ai_utils.py            # AI logic – Gemini primary, Groq fallback, Mock mode
├── requirements.txt       # Python dependencies
├── .env                   # API keys (not in version control)
├── .gitignore             # Excludes secrets, temp files, etc.
├── README.md              # This file
│
└── pages/
    └── chat.py            # Chat interface + sidebar (API keys, controls)
```

---

## 🔧 Installation & Setup

### Prerequisites

- **Python 3.12** or higher installed.
- **API Keys** from:
  - [Google AI Studio](https://aistudio.google.com/apikey) (Gemini)
  - [Groq Console](https://console.groq.com/keys) (Groq)

### Step 1: Clone the Repository

```bash
git clone https://github.com/NayabMalik1/student_chatbot.git
cd student_chatbot
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create `.env` File (Optional)

Copy this into a file named `.env` in the root folder:

```env
GEMINI_API_KEY=your_gemini_key_here
GROQ_API_KEY=your_groq_key_here
```

> **Note:** If you skip this step, you can enter keys manually in the app’s sidebar.

### Step 5: Run the Application

```bash
streamlit run app.py
```

Your assistant will be available at `http://localhost:8501`.

---

## ⚙️ Configuration

### API Key Priority

1. Keys entered in the sidebar override `.env` keys.
2. If no keys are entered, the app tries to load from `.env`.

### Mock Mode (Offline Testing)

In `ai_utils.py`, set:

```python
USE_MOCK = True   # Predefined responses – no API needed
USE_MOCK = False  # Use real APIs (default)
```

---

## 📖 Usage Guide

1. **Launch** the app → you see the chat interface.
2. **Open the sidebar** (☰ on mobile) and enter your Gemini and/or Groq API keys.
3. **Click "Save Keys"** – keys are stored for the session.
4. **Type your question** in the chat input and press Enter.
5. The AI responds with helpful, step‑by‑step explanations.

### Example Questions

| Question | What the Assistant Does |
|----------|-------------------------|
| *"Explain photosynthesis in simple terms."* | Breaks down the concept with analogies and key points. |
| *"Solve 2x + 5 = 15, step by step."* | Guides you through the solution while teaching the method. |
| *"Write a Python function to reverse a string."* | Provides code with explanation. |
| *"How do I write a good thesis statement?"* | Gives tips and examples. |
| *"I’m struggling with physics – any study tips?"* | Offers strategies and resources. |

---

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub (ensure `.env` is in `.gitignore`).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **"Create app"** → select your repository and branch.
4. Set **Main file path** to `app.py`.
5. Under **Advanced settings** → **Secrets**, add your API keys:

```toml
GEMINI_API_KEY = "your_gemini_key"
GROQ_API_KEY = "your_groq_key"
```

6. Click **Deploy** – your app will be live in a few minutes!

**Your App URL:**  
`https://student-chatbot-nayabmalik1.streamlit.app`

---

## 🎨 Color Scheme & UI

The interface features a **dark theme** with a warm **orange & green** accent palette:

- **Header:** Orange gradient (`#d35400` → `#e67e22`) – energetic and friendly.
- **Bot messages:** Dark orange background with orange accents.
- **User messages:** Dark green background with green accents.
- **Input box:** Orange border for focus and consistency.

**Icons** are SVG-based (book, person, robot) for crisp rendering on all devices.

---

## 📸 Screenshots

*[Insert screenshots of the chat interface here – showing a conversation, sidebar, and mobile view.]*

---

## 🔧 Troubleshooting

| Error | Solution |
|-------|----------|
| `API key not valid` | Check for typos or regenerate the key. |
| `Quota exhausted` | Switch to Mock Mode (`USE_MOCK = True`) or wait for quota reset. |
| `ModuleNotFoundError` | Ensure all packages in `requirements.txt` are installed: `pip install -r requirements.txt`. |
| `Sidebar not showing on mobile` | The hamburger menu (☰) appears; tap it to open the sidebar. We no longer hide the top bar. |

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo, make improvements, and submit a pull request.

---

## 📝 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Google Gemini AI** – for the powerful language model.
- **Groq** – for the fast fallback inference.
- **Streamlit** – for the amazing framework that makes building AI apps so easy.

---

## 👨‍💻 Author

**Nayab Malik**  
[GitHub](https://github.com/NayabMalik1)  

---

## ⭐ Show Your Support

If this project helps you, please give it a ⭐ on GitHub!

---

Happy Learning! 🍊📚
```

---

## ✅ How to Save & Use

1. Create a file named `README.md` in your project root.
2. Copy the above content and paste it.
3. Replace placeholder links and usernames if needed.
4. Add actual screenshots if you want (optional).

---

This README is now tailored for your **Student Study Assistant** – clear, comprehensive, and perfect for your university submission. 😊🍊
