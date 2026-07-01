import streamlit as st

from utils.database import initialize_database
from utils.sidebar import show_sidebar

from pages.login import show_login
from pages.dashboard import show_dashboard
from pages.raise_complaint import show_raise_complaint
from pages.track_complaint import show_track_complaint
from pages.my_complaints import show_my_complaints
from pages.admin_dashboard import show_admin_dashboard
from pages.ai_assistant import show_ai_assistant

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Smart City Complaint System",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load Custom CSS
# -----------------------------
with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Initialize Database
# -----------------------------
initialize_database()

# -----------------------------
# Session State
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# Login Page
# -----------------------------
if not st.session_state.logged_in:
    show_login()
    st.stop()

# -----------------------------
# Sidebar Navigation
# -----------------------------
selected = show_sidebar()

# -----------------------------
# Page Routing
# -----------------------------
if selected == "Dashboard":
    show_dashboard()

elif selected == "Raise Complaint":
    show_raise_complaint()

elif selected == "Track Complaint":
    show_track_complaint()

elif selected == "My Complaints":
    show_my_complaints()

elif selected == "Admin Dashboard":
    show_admin_dashboard()

elif selected == "AI Assistant":
    show_ai_assistant()

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
elif
