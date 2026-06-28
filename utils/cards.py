import streamlit as st

def stat_card(title, value, emoji, color):

    st.markdown(
        f"""
        <div style="
        background:{color};
        padding:20px;
        border-radius:20px;
        box-shadow:0px 8px 20px rgba(0,0,0,.08);
        text-align:center;
        ">

        <h2>{emoji}</h2>

        <h3>{title}</h3>

        <h1>{value}</h1>

        </div>
        """,
        unsafe_allow_html=True
    )
