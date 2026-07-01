import streamlit as st

def hero_section():

    name = st.session_state.get("user_name", "Citizen")

    left, right = st.columns([2, 1])

    with left:

        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#FFD9EA,#DDF4FF);
        padding:35px;
        border-radius:25px;
        height:250px;
        box-shadow:0 10px 20px rgba(0,0,0,.08);
        ">

        <h1 style="color:#E75480;">
        🏙 Smart City Complaint System
        </h1>

        <h3 style="color:#4F9DD9;">
        Welcome {name} 👋
        </h3>

        <p style="font-size:18px;">
        AI Powered Smart Governance Platform
        </p>

        </div>
        """, unsafe_allow_html=True)

    with right:

        st.image(
            "assets/hero_city.png",
            use_container_width=True
        )
