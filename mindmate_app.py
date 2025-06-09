
import streamlit as st
import time
import re
import cv2
import os
from groq import Groq

# Init Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Safe zone message
def show_safe_zone_message():
    st.markdown("### 🧠 You are in a safe zone.")
    st.markdown("Feel free to share anything you're feeling. I'm here to help.")

# Breathing exercise
def breathing_exercise():
    st.markdown("## 🧘 Breathing Exercise")
    st.markdown("Inhale... Hold... Exhale...")
    for i in range(3):
        st.markdown(f"Inhale... ({i+1}/3)")
        time.sleep(2)
        st.markdown("Hold...")
        time.sleep(1)
        st.markdown("Exhale...")
        time.sleep(2)

# Mental health analysis via webcam (mocked for demo)
def analyze_webcam():
    st.markdown("## 📷 Analyzing mental health via webcam...")
    st.warning("Demo mode: Webcam analysis simulated.")
    st.info("You seem a bit low. I'm here with you. Let's try a breathing exercise.")

# Check for critical words
def check_critical_words(user_input):
    critical_keywords = ["suicide", "depressed", "kill myself", "end life"]
    for word in critical_keywords:
        if word in user_input.lower():
            return True
    return False

# Show helpline and calming message
def show_support_message():
    st.error("If you're feeling suicidal or need help, please contact:")
    st.markdown("""
    - **iCall (TISS)**: 9152987821
    - **AASRA**: +91-9820466726
    - **Snehi**: +91-9582208181
    """)
    st.info("You are not alone. I'm here with you. Let's talk or try a calming activity.")

# Chatbot response using Groq
def get_groq_response(prompt):
    try:
        response = client.chat.completions.create(
            model = "llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a kind and supportive mental health assistant named MindMate."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit interface
def main():
    st.title("🧠 MindMate Mental Health Chatbot (Groq API)")
    show_safe_zone_message()

    st.markdown("### How are you feeling today?")
    user_input = st.text_input("")

    if st.button("Send"):
        if user_input:
            if check_critical_words(user_input):
                show_support_message()
            else:
                reply = get_groq_response(user_input)
                st.markdown(f"**MindMate:** {reply}")

    if st.button("Start Breathing Exercise"):
        breathing_exercise()

    if st.button("Analyze via Webcam"):
        analyze_webcam()

if __name__ == "__main__":
    main()
