import streamlit as st
import openai
import cv2
import time

# Groq API key
openai.api_key = st.secrets["GROQ_API_KEY"]

TRIGGER_WORDS = ['suicide', 'depression', 'kill myself', 'end my life', 'worthless', 'hopeless']

HELPLINE_MSG = """
🚨 *You're not alone.*

🇮🇳 Indian Helplines:
- iCall: +91 9152987821
- AASRA: +91 9820466726
- Snehi: +91-9582208181

Please breathe. You're safe here. 💙
"""

SAFE_ZONE_MSG = "🫂 You’re in a safe zone. Share freely — I’m here to help you."

def critical_keywords_present(text):
    return any(word in text.lower() for word in TRIGGER_WORDS)

def breathing_exercise():
    steps = [("Inhale", 4), ("Hold", 4), ("Exhale", 4)]
    for step, seconds in steps:
        st.write(f"**{step}** for {seconds} seconds...")
        time.sleep(seconds)
    st.success("🧘 Breathing cycle complete.")

def webcam_analysis():
    st.info("🧠 Analyzing via webcam...")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if ret:
        st.image(frame, caption="Captured Image")
        return "I sense some tension. Let's try breathing together. 🌿"
    return "Could not access webcam."

def get_groq_response(user_input):
    res = openai.ChatCompletion.create(
        model="mixtral-8x7b-32768",
        messages=[
            {"role": "system", "content": "You are MindMate, a supportive AI mental health companion."},
            {"role": "user", "content": user_input}
        ]
    )
    return res['choices'][0]['message']['content']

# Streamlit UI
st.set_page_config(page_title="MindMate", page_icon="🧠")
st.title("🧠 MindMate: Your Mental Health Companion")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.success(SAFE_ZONE_MSG)

with st.form("user_input_form"):
    user_input = st.text_area("Share your thoughts", placeholder="How are you feeling today?")
    analyze_cam = st.checkbox("Analyze my mental state via webcam")
    breathe = st.checkbox("Guide me through breathing")
    submit = st.form_submit_button("Send")

if submit and user_input.strip():
    response_parts = []

    if analyze_cam:
        analysis = webcam_analysis()
        response_parts.append(analysis)

    if breathe:
        breathing_exercise()

    if critical_keywords_present(user_input):
        response_parts.append(HELPLINE_MSG)

    ai_response = get_groq_response(user_input)
    response_parts.append(ai_response)

    final_response = "\n\n".join(response_parts)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("MindMate", final_response))

for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
