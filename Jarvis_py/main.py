import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib
import requests
from ai import ask
import os
from config import NEWSAPI

recognizer = sr.Recognizer()
engine = pyttsx3.init() 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process(c):
    text=c.lower()
    if "open google" in text:
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open youtube" in text:
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in text:
        speak("opening linkedin")
        webbrowser.open("https://linkedin.com")
    
    elif "open github" in text:
        speak("opening github")
        webbrowser.open("https://github.com/Pareekshith-M-Kumar")

    elif text.startswith("play"):
        song = text.split(" ")[1]
        link = musicLib.music[song]
        webbrowser.open(link)

    elif "news" in text:
        r = requests.get(f"Paste_API_Key_from_NEWSAPI")
        if r.status_code == 200:
            data = r.json()
            
            # get articles
            articles = data.get('articles', [])
            
            # headlines
            for article in articles:
                speak(article['title'])
    elif "exit" in text:
        speak("goodbye") 
        exit()

    else:
        answer = ask(text)
        print(answer)
        speak(answer)


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis is Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    process(command)


        except Exception as e:
            print("Error; {0}".format(e))