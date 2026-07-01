import streamlit as st

from components.hero import hero_section
from components.stat_cards import stat_card
from components.ai_card import ai_card


def show_dashboard():

    # ==========================
    # Hero Section
    # ==========================
    hero_section()

    st.write("")

    # ==========================
    # Statistics Cards
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        stat_card(
            title="Total Complaints",
            value="120",
            color="#FFE5F1",
            emoji="📋"
        )

    with col2:
        stat_card(
            title="Resolved",
            value="90",
            color="#DFF4FF",
            emoji="✅"
        )

    with col3:
        stat_card(
            title="Pending",
            value="25",
            color="#F7E6D5",
            emoji="🚧"
        )

    with col4:
        stat_card(
            title="Urgent",
            value="5",
            color="#FFECEC",
            emoji="🚨"
        )

    st.write("")
    st.divider()

    # ==========================
    # Analytics + AI Section
    # ==========================

    left, right = st.columns([2, 1])

    with left:

        st.subheader("📊 Analytics Dashboard")

        st.info(
            "📈 Live analytics charts will appear here in the next step."
        )

        st.write("")

        st.metric(
            "Today's Complaints",
            "18",
            "+5"
        )

        st.metric(
            "Resolved Today",
            "12",
            "+3"
        )

    with right:

        ai_card()

    st.write("")
    st.divider()

    # ==========================
    # Recent Complaints
    # ==========================

    st.subheader("📋 Recent Complaints")

    st.dataframe(
        {
            "Complaint ID": [
                "CMP001",
                "CMP002",
                "CMP003",
                "CMP004",
                "CMP005"
            ],
            "Category": [
                "Garbage",
                "Road Damage",
                "Street Light",
                "Water Leakage",
                "Electricity"
            ],
            "Priority": [
                "Medium",
                "High",
                "Low",
                "High",
                "Medium"
            ],
            "Status": [
                "Pending",
                "Resolved",
                "In Progress",
                "Pending",
                "Resolved"
            ]
        },
        use_container_width=True,
        hide_index=True
    )

    st.write("")
    st.divider()

    # ==========================
    # Notifications
    # ==========================

    st.subheader("🔔 Latest Updates")

    st.success("✅ Garbage complaint CMP002 has been resolved.")

    st.info("🚧 Road repair work has started in Sector 12.")

    st.warning("⚠ Heavy rain may delay water leakage repairs.")

    st.success("🤖 AI has categorized today's complaints automatically.")
