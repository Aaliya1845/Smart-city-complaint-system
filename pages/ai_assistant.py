import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def show_ai_assistant():

    st.title("🤖 Smart City AI Assistant")

    st.write(
        "Ask anything related to Smart City services or complaints."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Type your question...")

    if prompt:

        st.session_state.messages.append(
            {
                "role":"user",
                "content":prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = model.generate_content(
                    f"""
You are an AI Smart City Assistant.

Help citizens regarding:

Roads

Garbage

Water Supply

Electricity

Street Lights

Traffic

Drainage

Government Services

Always answer politely.

Question:

{prompt}
"""
                )

                answer = response.text

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":answer
            }
        )
