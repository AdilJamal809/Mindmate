import streamlit as st
import time
import re
import cv2
import tempfile
import base64
import requests
from PIL import Image

# Safe space message
st.markdown("""
    <h1 style='text-align: center;'>MindMate 🤝</h1>
    <p style='text-align: center; font-size: 20px;'>You're in a safe space. Whatever you're feeling, it's okay. I'm here to support you.</p>
""", unsafe_allow_html=True)

# Load Groq API Key
try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    st.error("Missing GROQ_API_KEY in Streamlit secrets.")
    st.stop()

# Suicide keyword detection and helpline response
def check_for_emergency(text):
    crisis_keywords = ["suicide", "kill myself", "end my life", "depressed"]
    if any(re.search(rf"\\b{k}\\b", text, re.IGNORECASE) for k in crisis_keywords):
        st.error("⚠️ It sounds like you're going through something really tough. You're not alone.")
        st.info("📞 India Helpline: 9152987821 (iCall), 022-27546669 (AASRA), or 91-9820466726")
        st.success("Take a deep breath. You matter and you're cared for. ❤️")
        return True
    return False

# Breathing exercise
with st.expander("🧘 Breathing Exercise"):
    inhale_time = st.slider("Inhale time (seconds)", 2, 10, 4)
    hold_time = st.slider("Hold time (seconds)", 2, 10, 4)
    exhale_time = st.slider("Exhale time (seconds)", 2, 10, 4)
    if st.button("Start Breathing Exercise"):
        for i in range(3):
            st.write("**Inhale**")
            time.sleep(inhale_time)
            st.write("**Hold**")
            time.sleep(hold_time)
            st.write("**Exhale**")
            time.sleep(exhale_time)
        st.success("Done! Hope you're feeling calmer now.")

# Webcam analysis (placeholder)
with st.expander("📷 Analyze Mental Health via Webcam"):
    st.info("Note: This is a placeholder. Camera mood analysis requires ML models.")
    run_webcam = st.checkbox("Run Webcam")
    if run_webcam:
        cap = cv2.VideoCapture(0)
        stframe = st.empty()
        while run_webcam:
            ret, frame = cap.read()
            if not ret:
                break
            stframe.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            if st.button("Stop Webcam"):
                break
        cap.release()

# Main chatbot interaction
st.markdown("---")
user_input = st.text_area("🗣️ Talk to MindMate")

if user_input:
    if not check_for_emergency(user_input):
        # Send to Groq API
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {
            "model": "llama3-70b-8192",
            "messages": [{"role": "user", "content": user_input}]
        }
        try:
            response = requests.post("https://api.groq.com/openai/v1/chat/completions",
                                     headers=headers, json=payload)
            ai_reply = response.json()["choices"][0]["message"]["content"]
            st.write(f"**MindMate:** {ai_reply}")
        except Exception as e:
            st.error(f"Error from Groq API: {e}")
