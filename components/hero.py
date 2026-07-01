import streamlit as st

def hero_section():

    name = st.session_state.get("user_name", "Citizen")

    st.markdown(f"""
    <div style="
        background:linear-gradient(135deg,#FFD9EA,#DDF4FF);
        padding:35px;
        border-radius:25px;
        box-shadow:0 10px 25px rgba(0,0,0,.08);
    ">

        <h1>🏙 Smart City Complaint System</h1>

        <h3>Welcome, {name} 👋</h3>

        <p style="font-size:18px;">
            AI Powered Citizen Service Portal
        </p>

    </div>
    """, unsafe_allow_html=True)
