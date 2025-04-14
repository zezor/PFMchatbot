# Updated Features
# ✅ 1. Voice Input & Text-to-Speech

import streamlit as st
from chatbot_backend import generate_response
import pyttsx3
import speech_recognition as sr
import tempfile
from gtts import gTTS
import os
from playsound import playsound

def speak(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        tts.save(fp.name)
        playsound(fp.name)
        os.remove(fp.name)

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn’t understand that."

# Streamlit UI
st.set_page_config(page_title="Finance Buddy", layout="centered")
st.title("🎙️💬 Finance Buddy Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("🎤 Speak"):
    user_input = listen()
    st.text(f"You said: {user_input}")
else:
    user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    response = generate_response(user_input)
    speak(response)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for sender, message in st.session_state.chat_history[::-1]:
    st.markdown(f"**{sender}:** {message}")
