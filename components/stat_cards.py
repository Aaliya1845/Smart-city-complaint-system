import streamlit as st

def stat_card(title, value, color, emoji):

    st.markdown(f"""
    <div style="
    background:{color};
    border-radius:20px;
    padding:20px;
    text-align:center;
    box-shadow:0px 8px 20px rgba(0,0,0,.08);
    ">

    <h2>{emoji}</h2>

    <h3>{title}</h3>

    <h1>{value}</h1>

    </div>
    """, unsafe_allow_html=True)
