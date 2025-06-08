import os
import streamlit as st
from groq import Groq

# Set Streamlit page config
st.set_page_config(page_title="MindMate", layout="centered")

# Retrieve the GROQ API key from environment variables
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ Missing GROQ_API_KEY in environment variables.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

# UI Elements
st.title("🧠 MindMate")
st.subheader("AI Mental Health Companion")
st.markdown("Chat privately with an AI about your thoughts or feelings.")

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user prompt
if prompt := st.chat_input("How are you feeling today?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Send to Groq
    try:
        chat_completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
        )

        reply = chat_completion.choices[0].message.content
        st.chat_message("assistant").markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"❌ Failed to get response: {e}")
