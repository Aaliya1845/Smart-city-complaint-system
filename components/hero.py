import streamlit as st

def hero_section():

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#FFDDEB,#DFF4FF);
    padding:35px;
    border-radius:25px;
    box-shadow:0px 10px 25px rgba(0,0,0,.08);
    margin-bottom:20px;
    ">

    <h1 style="color:#E75480;">
    🏙 Smart City Complaint System
    </h1>

    <h3 style="color:#4F9DD9;">
    Welcome 👋
    </h3>

    <p style="font-size:18px;">
    AI Powered Complaint Management Platform
    </p>

    </div>
    """, unsafe_allow_html=True)
