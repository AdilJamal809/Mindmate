
import streamlit as st
import time
import cv2
import numpy as np
from groq import Groq
import os

st.set_page_config(page_title="MindMate Mental Health Chatbot", layout="centered")

# Set your Groq API key from environment variable
groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)

# Safe zone welcome message
st.markdown("""
# 🧠 MindMate Mental Health Chatbot (Groq API)

## 🧠 You are in a safe zone.
Feel free to share anything you're feeling. I'm here to help.
""")

# Text input
st.subheader("How are you feeling today?")
user_input = st.text_input("", placeholder="Type here and press Enter…")

# Check for crisis keywords
def contains_crisis_words(text):
    text = text.lower()
    crisis_words = ["suicide", "kill myself", "self-harm", "depressed", "want to die", "hurting myself"]
    return any(word in text for word in crisis_words)

if user_input:
    if contains_crisis_words(user_input):
        st.markdown("""
### 🆘 It looks like you're going through something very difficult.
You're not alone. Please consider reaching out to a mental health professional or calling these Indian helpline numbers:

📞 **iCall** – 9152987821  
📞 **AASRA** – 91-9820466726  
📞 **Vandrevala Foundation Helpline** – 1860 266 2345 / 1800 233 3330  

💙 You are valued. You are important. You deserve support.
        """)
    else:
        try:
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "user", "content": user_input}],
                temperature=0.7
            )
            st.markdown("**MindMate:** " + response.choices[0].message.content)
        except Exception as error:
            st.error(f"MindMate: Error: {error}")

# Breathing Exercise
if st.button("Start Breathing Exercise"):
    st.markdown("## 🌬️ Breathing Exercise")
    for _ in range(3):
        st.markdown("### Inhale")
        time.sleep(4)
        st.markdown("### Hold")
        time.sleep(4)
        st.markdown("### Exhale")
        time.sleep(4)
    st.success("Hope that helped you feel a little better 💙")

# Webcam-based mood analysis (mock)
def analyze_face_emotion():
    st.markdown("## 📷 Analyzing Emotion via Webcam")
    st.info("(Simulated Webcam Analysis: This part needs a real emotion recognition model.)")
    st.success("You seem calm. Keep taking care of yourself 💙")

if st.button("Analyze via Webcam"):
    analyze_face_emotion()
