from openai import OpenAI
from config import GROQ_API_KEY

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def ask(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
    {
        "role": "system",
        "content": """
You are Jarvis, an intelligent voice assistant.

Rules:
1. Keep every answer under 100 words.
2. Speak naturally and clearly.
3. Give direct answers.
4. If the user asks for code, provide only the necessary code.
5. Avoid long paragraphs.
"""
    },
    {
        "role": "user",
        "content": prompt
    }
]
        )

        return response.choices[0].message.content

    except Exception as e:
        print(e)
        return "Sorry, I couldn't connect to Groq."