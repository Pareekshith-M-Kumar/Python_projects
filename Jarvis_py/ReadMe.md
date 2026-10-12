# 🎙️ Jarvis AI - Python Voice Assistant

An AI-powered voice assistant built with Python that listens for a wake word ("Jarvis"), executes voice commands, fetches real-time news, plays music, opens websites, and answers general questions using the Groq LLM API.

This project demonstrates the integration of Speech Recognition, Text-to-Speech, REST APIs, Browser Automation, and Large Language Models (LLMs) to create an intelligent desktop assistant.

---

##  Features

-  Wake Word Detection ("Jarvis")
-  Speech-to-Text using Google Speech Recognition
-  Text-to-Speech using pyttsx3
-  Open Websites
  - Google
  - YouTube
  - LinkedIn
  - Github
-  Play Songs from Custom Music Library
-  Read Latest News Headlines using NewsAPI
-  AI-powered Question Answering using Groq (Llama 3.3 70B)
-  Voice Command to Exit Assistant

---

## 🛠️ Tech Stack

- Python 3.13
- SpeechRecognition
- PyAudio
- pyttsx3
- Requests
- Groq API
- OpenAI Python SDK (Groq Compatible)
- Webbrowser Module

---

## 📁 Project Structure

```
Jarvis-AI/
│
├── main.py              # Main Voice Assistant
├── ai.py                # Groq AI Integration
├── config.py            # API Keys
├── musicLib.py          # Music Dictionary
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/Pareekshith-M-Kumar/Jarvis_py.git

cd Jarvis_py
```

---

### 2. Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

### 3. Install Imports
---

## 🔑 API Keys

### Groq API

Create a free API key from

https://console.groq.com

Add it to `config.py`

```python
GROQ_API_KEY = "YOUR_API_KEY"
```

---

### News API

Create a free key from

https://newsapi.org

Add it to `config.py`

```python
NEWS_API_KEY = "YOUR_API_KEY"
```

---

## ▶️ Run the Project

```bash
python main.py
```

Jarvis initializes and starts listening.

Say

```
Jarvis
```

Then give your command.

---

## 💬 Example Commands

### Open Websites

```
Jarvis
Open Google
```

```
Jarvis
Open YouTube
```

```
Jarvis
Open LinkedIn
```

---

### Play Music

```
Jarvis
Play fairytale
```

---

### News

```
Jarvis
News
```

Jarvis reads the latest headlines.

---

### AI Questions

```
Jarvis
What is Java?
```

```
Jarvis
Explain Machine Learning.
```

```
Jarvis
Who invented Python?
```

These questions are answered using the Groq Llama model.

---

## 📦 Dependencies

```text
SpeechRecognition
PyAudio
pyttsx3
requests
openai
```

Install

```bash
pip install SpeechRecognition
pip install PyAudio
pip install pyttsx3
pip install requests
pip install openai
```

---

## 🚀 Future Improvements

- Conversation Memory
- Weather Updates
- Email Sending
- WhatsApp Automation
- Open Desktop Applications
- File Search
- PDF Summarizer
- Calendar Integration
- Reminder System
- Chat History
- Voice Authentication
- AI Vision (Image Understanding)
- Local LLM Support (Ollama)

---

## 👨‍💻 Author

**Pareekshith M Kumar**

Final Year Engineering Student

Interested in

- Java Backend Development
- Artificial Intelligence
- Automation
- Spring Boot
- Python
- Large Language Models

LinkedIn:
https://www.linkedin.com/in/pareekshith-m-kumar-380181391/

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It motivates me to build more AI and backend projects.
