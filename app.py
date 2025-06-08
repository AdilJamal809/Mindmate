import streamlit as st
from openai import OpenAI
import time

st.set_page_config(page_title="MindMate", layout="wide")

# Initialize Groq Client (compatible with OpenAI Python >=1.0.0)
client = OpenAI(
    api_key=st.secrets["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

# Suicide keyword trigger
SUICIDE_KEYWORDS = ["suicide", "kill myself", "end my life", "die", "depressed"]

# Welcome message
if "first_visit" not in st.session_state:
    st.session_state.first_visit = True
    st.info("🛡️ You are in a **safe zone**. Feel free to share your feelings. I'm here for you. 💙")

# Sidebar feature selector
feature = st.sidebar.selectbox("Choose a Feature", ["Chat with MindMate", "Breathing Exercises"])

def detect_crisis(text):
    return any(word in text.lower() for word in SUICIDE_KEYWORDS)

def get_crisis_response():
    return (
        "⚠️ It sounds like you're going through a tough time."

"
        "**Please know you're not alone.** Here are some helpline numbers in India:
"
        "- ☎️ iCall: 9152987821"
"
        "- ☎️ AASRA: 91-22-27546669 / 91-22-27546667
"
        "- ☎️ Vandrevala Foundation: 1860 266 2345 or 1800 233 3330

"
        "_You're valuable and help is available. ❤️_"
    )

def ai_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error generating response: {e}"

def breathing_exercise():
    st.title("🧘 Breathing Exercise")
    st.write("Follow the guided breathing cycle below:")

    cycles = st.slider("Number of Cycles", 1, 5, 3)
    inhale_time = st.slider("Inhale (seconds)", 2, 6, 4)
    hold_time = st.slider("Hold (seconds)", 2, 6, 4)
    exhale_time = st.slider("Exhale (seconds)", 2, 6, 4)

    if st.button("Start Breathing"):
        for i in range(cycles):
            st.subheader(f"Cycle {i+1}")
            st.write("🌬️ Inhale...")
            time.sleep(inhale_time)
            st.write("⏸️ Hold...")
            time.sleep(hold_time)
            st.write("😮‍💨 Exhale...")
            time.sleep(exhale_time)
        st.success("✅ Breathing session complete. Feel the calm?")

if feature == "Chat with MindMate":
    st.title("🧠 MindMate Chatbot")
    user_input = st.text_input("What's on your mind?")
    if user_input:
        if detect_crisis(user_input):
            st.warning(get_crisis_response())
        else:
            reply = ai_response(user_input)
            st.markdown("**MindMate:** " + reply)

elif feature == "Breathing Exercises":
    breathing_exercise()
