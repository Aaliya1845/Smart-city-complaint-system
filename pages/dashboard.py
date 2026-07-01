import streamlit as st

from components.hero import hero_section
from components.stat_cards import stat_card
from components.ai_card import ai_card


def show_dashboard():

    # Hero Banner
    hero_section()

    st.write("")

    # Statistics Cards
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

    # Main Dashboard Layout
    left, right = st.columns([2, 1])

    with left:

        st.subheader("📋 Recent Complaints")

        st.dataframe(
            {
                "Complaint ID": [
                    "CMP001",
                    "CMP002",
                    "CMP003",
                    "CMP004"
                ],
                "Category": [
                    "Garbage",
                    "Road Damage",
                    "Street Light",
                    "Water Leakage"
                ],
                "Status": [
                    "Pending",
                    "Resolved",
                    "In Progress",
                    "Pending"
                ]
            },
            use_container_width=True,
            hide_index=True
        )

    with right:

        ai_card()
