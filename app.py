import streamlit as st
import time

# Display welcome/safe zone message
st.title("MindMate 🤝")
st.markdown("You're in a safe space. Whatever you're feeling, it's okay. I'm here to support you.")

# Load Groq API key
api_key = st.secrets["GROQ_API_KEY"]

# Breathing exercise
if st.button("Start Breathing Exercise"):
    st.write("Inhale...")
    time.sleep(4)
    st.write("Hold...")
    time.sleep(7)
    st.write("Exhale...")
    time.sleep(8)
    st.success("Great job!")

# Critical word detection (basic example)
user_input = st.text_area("How are you feeling today?")

if any(word in user_input.lower() for word in ["suicide", "kill myself", "end it all"]):
    st.error("It sounds like you're in a very tough place. You're not alone.")
    st.markdown("📞 **India Helpline:** 9152987821")
    st.markdown("💬 Try talking to someone you trust.")

# Placeholder for webcam-based sentiment analysis
st.info("🧠 Webcam mood analysis feature coming soon...")
