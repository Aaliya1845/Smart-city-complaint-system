import streamlit as st

from utils.sidebar import show_sidebar
from pages.dashboard import show_dashboard
from pages.raise_complaint import show_raise_complaint

st.set_page_config(
    page_title="Smart City Complaint System",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar Navigation
selected = show_sidebar()

# Page Routing
if selected == "Dashboard":
    show_dashboard()

elif selected == "Raise Complaint":
    show_raise_complaint()

elif selected == "Track Complaint":
    st.title("📍 Track Complaint")
    st.info("🚧 Coming Soon...")

elif selected == "My Complaints":
    st.title("📂 My Complaints")
    st.info("🚧 Coming Soon...")

elif selected == "AI Assistant":
    st.title("🤖 AI Assistant")
    st.info("🚧 Coming Soon...")

elif selected == "Reports":
    st.title("📊 Reports")
    st.info("🚧 Coming Soon...")

elif selected == "Notifications":
    st.title("🔔 Notifications")
    st.info("🚧 Coming Soon...")

elif selected == "Profile":
    st.title("👤 Profile")
    st.info("🚧 Coming Soon...")

elif selected == "Settings":
    st.title("⚙️ Settings")
    st.info("🚧 Coming Soon...")
