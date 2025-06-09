
import streamlit as st
from groq import Groq
import os

st.set_page_config(page_title="MindMate Mental Health Bot", layout="centered")

st.title("🧠 MindMate Mental Health Bot")
st.markdown("Welcome to your safe space. How are you feeling today?")

# Initialize Groq client using environment variable
client = Groq(api_key=os.environ["GROQ_API_KEY"])

user_input = st.text_input("Type your thoughts here:")

if user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {"role": "system", "content": "You are a supportive mental health companion."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write(response.choices[0].message.content)
