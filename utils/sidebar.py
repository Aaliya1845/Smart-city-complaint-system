from streamlit_option_menu import option_menu
import streamlit as st

def show_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <h2 style='text-align:center;color:#F48FB1;'>
            🏙️ Smart City
            </h2>
            <p style='text-align:center;color:#6AAFE6;'>
            Complaint System
            </p>
            """,
            unsafe_allow_html=True,
        )

        selected = option_menu(
            menu_title=None,
            options=[
                "Dashboard",
                "Raise Complaint",
                "Track Complaint",
                "My Complaints",
                "AI Assistant",
                "Reports",
                "Notifications",
                "Profile",
                "Settings",
            ],
            icons=[
                "house-fill",
                "plus-circle-fill",
                "geo-alt-fill",
                "folder-fill",
                "robot",
                "bar-chart-fill",
                "bell-fill",
                "person-fill",
                "gear-fill",
            ],
            default_index=0,
        )

    return selected
