import streamlit as st
import pandas as pd
from utils.cards import stat_card


def show_dashboard():

    st.markdown("""
    <div class="banner">
        <h1>🏙️ Welcome Back!</h1>
        <p>Help make your city cleaner, safer and smarter with AI.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Statistics Cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        stat_card("Total Complaints", "128", "📋", "#FFE8F2")

    with col2:
        stat_card("Resolved", "96", "✅", "#DFF7FF")

    with col3:
        stat_card("Pending", "24", "🚧", "#FFF0DE")

    with col4:
        stat_card("Urgent", "08", "🚨", "#FDE7EA")

    st.write("")

    left, right = st.columns([2, 1])

    with left:
        st.subheader("📋 Recent Complaints")

        df = pd.DataFrame({
            "Complaint ID": ["CMP001", "CMP002", "CMP003", "CMP004"],
            "Category": ["Garbage", "Road Damage", "Street Light", "Water Leakage"],
            "Status": ["Resolved", "Pending", "In Progress", "Resolved"]
        })

        st.dataframe(df, use_container_width=True)

    with right:
        st.markdown("""
        <div class="ai-box">
            <h2>🤖 AI Assistant</h2>
            <p>
            Hello 👋<br><br>
            I can:
            <br>✔ Classify complaints
            <br>✔ Suggest departments
            <br>✔ Predict priority
            <br>✔ Answer citizen queries
            </p>
        </div>
        """, unsafe_allow_html=True)
