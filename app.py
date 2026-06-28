import streamlit as st

st.set_page_config(
    page_title="Smart City Complaint System",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    from pages.dashboard import show_dashboard

show_dashboard()

st.markdown(
    """
    <div class="main-title">
        🏙️ Smart City Complaint System
    </div>

    <div class="subtitle">
        AI Powered Complaint Management Platform
    </div>
    """,
    unsafe_allow_html=True,
)

st.info("🚀 Project setup completed successfully!")

st.write("")
st.write("### Welcome")

st.write(
    """
This is the beginning of our AI-powered Smart City Complaint System.

In the next step, we'll build the premium dashboard that matches the UI design.
"""
)
