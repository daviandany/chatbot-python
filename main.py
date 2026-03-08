import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")

st.title("AI Chatbot")

if "message_list" not in st.session_state:
    st.session_state["message_list"] = []

for message in st.session_state["message_list"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_text = st.chat_input("Write your message")

if user_text:

    with st.chat_message("user"):
        st.write(user_text)

    st.session_state["message_list"].append(
        {"role": "user", "content": user_text}
    )

    response = model.generate_content(user_text)
    ai_text = response.text

    with st.chat_message("assistant"):
        st.write(ai_text)

    st.session_state["message_list"].append(
        {"role": "assistant", "content": ai_text}
    )