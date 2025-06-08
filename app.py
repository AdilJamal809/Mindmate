import streamlit as st
import time
import os

groq_api_key = os.getenv("GROQ_API_KEY")


def safe_zone():
    st.markdown("### 🫂 You’re in a **Safe Zone**\nFeel free to share your thoughts. I’m here to listen without judgment.")

def check_crisis(text):
    crisis_words = ["suicide", "kill myself", "depressed", "end my life"]
    if any(word in text.lower() for word in crisis_words):
        st.warning("🚨 It sounds like you're going through a really hard time.")
        st.info("Here are some **Indian mental health helplines**:\n\n📞 iCall: 9152987821\n📞 Snehi: 91-9582208181\n📞 Vandrevala: 9999 666 555")
        st.success("You're not alone. Help is available. You matter. ❤️")

def breathing_technique():
    st.markdown("## 🧘 Breathing Exercise")
    st.write("Follow the inhale → hold → exhale routine.")
    phase = [("Inhale", 4), ("Hold", 4), ("Exhale", 4)]
    for name, duration in phase:
        st.markdown(f"### {name}")
        time.sleep(duration)
        st.write(f"{name} done")

def ai_response(prompt):
    import openai
    openai.api_key = GROQ_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def mood_from_webcam():
    st.markdown("## 🎥 Webcam Mood Analysis (Simulated)")
    st.write("This feature would analyze your expression via webcam.")
    st.write("Feature under development!")

def main():
    st.set_page_config(page_title="MindMate 💬", layout="centered")
    st.title("🧠 MindMate - Your Mental Wellness Companion")

    safe_zone()

    choice = st.sidebar.selectbox("Choose a Feature", ["Chat with MindMate", "Breathing Exercise", "Webcam Mood Analysis"])

    if choice == "Breathing Exercise":
        breathing_technique()

    elif choice == "Webcam Mood Analysis":
        mood_from_webcam()

    elif choice == "Chat with MindMate":
        user_input = st.text_input("What's on your mind?", key="user_input")
        if user_input:
            check_crisis(user_input)
            with st.spinner("MindMate is thinking..."):
                reply = ai_response(user_input)
                st.success(reply)

if __name__ == "__main__":
    main()
