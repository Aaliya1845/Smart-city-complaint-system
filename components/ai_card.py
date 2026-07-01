import streamlit as st

def ai_card():

    st.markdown("""
    <div style="
    background:white;
    border-radius:25px;
    padding:25px;
    box-shadow:0px 10px 20px rgba(0,0,0,.08);
    ">

    <h2>🤖 AI Assistant</h2>

    <p>Hello Citizen 👋</p>

    <p>I can help with:</p>

    <ul>
        <li>Complaint Analysis</li>
        <li>Priority Prediction</li>
        <li>Department Recommendation</li>
        <li>Complaint Tracking</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)
