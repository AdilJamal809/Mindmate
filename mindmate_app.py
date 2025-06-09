
import streamlit as st
import os
import time
from openai import OpenAI

# Load API Key
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("GROQ_API_KEY is missing. Please set it in Render environment variables.")
    st.stop()

client = OpenAI(api_key=groq_api_key)

# Trigger words and helpline message
TRIGGER_WORDS = ['suicide', 'depression', 'kill myself', 'end my life', 'worthless', 'hopeless']
HELPLINE_MSG = """
🚨 You're not alone.

🇮🇳 Indian Helplines:
- iCall: +91 9152987821
- AASRA: +91 9820466726
- Snehi: +91-9582208181

Please breathe. You're safe here. 💙
"""

SAFE_ZONE_MSG = "🫂 You’re in a safe zone. Share freely — I’m here to help you."

# UI
st.set_page_config(page_title="MindMate Mental Health Bot", page_icon="🧠")
st.title("🧠 MindMate Mental Health Bot")

# Safe zone message
st.markdown(f"### {SAFE_ZONE_MSG}")

# Webcam analysis (simulation)
use_webcam = st.checkbox("📷 Analyze Mental Health via Webcam")
if use_webcam:
    st.markdown("Analyzing facial emotion... (simulated)")
    st.info("You seem a bit low. Let's work together to help you feel better.")

# Breathing exercise
if st.button("🧘 Start Breathing Exercise"):
    st.write("Follow this pattern:")
    for _ in range(2):
        st.markdown("### 🫁 Inhale...")
        time.sleep(4)
        st.markdown("### ✋ Hold...")
        time.sleep(4)
        st.markdown("### 😮‍💨 Exhale...")
        time.sleep(4)

# Chat input
user_input = st.text_input("How are you feeling today?")
if user_input:
    if any(word in user_input.lower() for word in TRIGGER_WORDS):
        st.warning(HELPLINE_MSG)

    with st.spinner("MindMate is thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a compassionate mental health support assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        st.markdown("### 🤖 MindMate:")
        st.write(response.choices[0].message.content)
