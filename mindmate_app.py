import streamlit as st
import os
from groq import Groq
import time

# Set up Groq API client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Set page config
st.set_page_config(page_title="MindMate Mental Health Chatbot", page_icon="🧠", layout="centered")

# Custom CSS for UI styling
st.markdown("""
    <style>
        html, body {
            background-color: #f2f6fa;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #2b4c7e;
        }
        .safe-zone {
            font-size: 1.2rem;
            background-color: #eaf6ff;
            border-radius: 10px;
            padding: 1rem;
            color: #22577a;
            margin-top: 10px;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #4d7cfe;
            color: white;
            font-weight: bold;
            padding: 0.5rem 1.5rem;
            border-radius: 10px;
        }
        input, textarea {
            font-size: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title and safety message
st.markdown('<div class="title">🧠 MindMate Mental Health Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="safe-zone">💬 You are in a safe zone. <br>Feel free to share anything you’re feeling. I’m here to help.</div>', unsafe_allow_html=True)

# Chat input
st.markdown("### How are you feeling today?")
user_input = st.text_input("")

# Show bot response
if st.button("Send"):
    try:
        with st.spinner("MindMate is thinking..."):
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {"role": "system", "content": "You are a compassionate AI trained to help users with mental wellness. Be supportive and thoughtful."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.success("MindMate:")
            st.write(response.choices[0].message.content)
    except Exception as e:
        st.error(f"MindMate: Error: {str(e)}")

# Breathing exercise
if st.button("🧘 Start Breathing Exercise"):
    st.markdown("### Let's begin a calming breathing exercise")
    phases = [("Inhale", 4), ("Hold", 4), ("Exhale", 4), ("Hold", 4)]
    for i in range(3):  # 3 cycles
        for action, duration in phases:
            st.markdown(f"#### {action} for {duration} seconds")
            time.sleep(duration)
            st.experimental_rerun()

# Webcam placeholder
if st.button("📷 Analyze via Webcam"):
    st.warning("Webcam mental health analysis not available in this deployment. Try local app for full features.")

