import streamlit as st
import time
from groq import Groq

# Initialize Groq client using Streamlit secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Safe zone message
st.markdown("## 🧠 Welcome to MindMate")
st.success("You are in a safe zone. Feel free to share your thoughts and feelings with me.")

# User input
user_input = st.text_input("How are you feeling today?")

# Critical word detection
critical_words = ["suicide", "depressed", "ending my life", "kill myself", "hopeless", "self-harm"]
helpline_msg = """
#### 🚨 You're not alone. Please consider reaching out:
- **iCall**: 9152987821
- **AASRA**: 91-9820466726
- **Vandrevala Foundation**: 1860 266 2345
"""

# Respond if critical terms are detected
if any(word in user_input.lower() for word in critical_words):
    st.error("⚠️ It sounds like you're going through a really tough time.")
    st.markdown(helpline_msg)
    st.info("Try to take a few deep breaths. I'm here for you. 💙")

# Breathing Exercise
if st.button("🧘‍♂️ Start Breathing Exercise"):
    for _ in range(3):
        st.write("👉 Inhale...") 
        time.sleep(4)
        st.write("✋ Hold...")
        time.sleep(4)
        st.write("🌬️ Exhale...")
        time.sleep(6)
    st.success("Feeling a bit better? You’re doing great!")

# AI Response via Groq API
if user_input and not any(word in user_input.lower() for word in critical_words):
    with st.spinner("MindMate is thinking..."):
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {"role": "system", "content": "You are a kind and supportive mental health assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        st.markdown(f"**MindMate:** {response.choices[0].message.content}")