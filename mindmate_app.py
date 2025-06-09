
import streamlit as st
import time
import re
import cv2
import numpy as np
from openai import OpenAI

# Load API Key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Safe zone message
st.title("🧠 MindMate - Mental Health Support Chatbot")
st.markdown("### 🫂 You are in a **safe space**. Feel free to share your feelings with me.")

# Chat function with OpenAI
def chat_with_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Detect critical keywords
def check_critical(input_text):
    critical_keywords = ["suicide", "end my life", "kill myself", "hopeless"]
    if any(word in input_text.lower() for word in critical_keywords):
        st.warning("🛑 It sounds like you're going through a tough time. You're not alone.")
        st.markdown("**Here are some Indian helpline numbers you can contact:**\n"
                    "- AASRA: 91-9820466726\n"
                    "- iCall: +91-9152987821\n"
                    "- Snehi: +91-9582208181")
        st.info("Take a deep breath. I'm here for you. ❤️")
        return True
    return False

# Breathing activity
def breathing_exercise():
    st.markdown("## 🧘 Breathing Exercise")
    phases = [("Inhale", 4), ("Hold", 4), ("Exhale", 4)]
    for phase, duration in phases:
        st.markdown(f"### {phase}")
        with st.empty():
            for i in range(duration, 0, -1):
                st.write(i)
                time.sleep(1)
    st.success("Done! Hope you feel better.")

# Webcam-based mood check (demo using brightness)
def analyze_mood():
    st.markdown("## 🎥 Analyzing Mood via Webcam...")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        brightness = np.mean(gray)
        mood = "neutral" if brightness > 100 else "sad"
        st.markdown(f"Detected mood: **{mood}**")
        if mood == "sad":
            st.info("It looks like you're feeling down. Want to try a breathing exercise?")
    else:
        st.error("Unable to access webcam.")

# UI interaction
user_input = st.text_input("How are you feeling today?")

if user_input:
    if not check_critical(user_input):
        reply = chat_with_openai(user_input)
        st.markdown(f"**MindMate:** {reply}")

# Breathing Exercise Button
if st.button("Start Breathing Exercise"):
    breathing_exercise()

# Webcam Mood Detection Button
if st.button("Check Mood with Webcam"):
    analyze_mood()
