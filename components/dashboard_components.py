import streamlit as st

def stat_card(title, value, icon, color):

    st.markdown(
        f"""
<div style="
background:{color};
padding:22px;
border-radius:22px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
text-align:center;
height:160px;
">

<div style="font-size:40px;">{icon}</div>

<h4>{title}</h4>

<h1>{value}</h1>

</div>
""",
        unsafe_allow_html=True
    )


def ai_card():

    st.markdown(
        """
<div style="
background:white;
padding:25px;
border-radius:22px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
height:330px;
">

<h2>🤖 AI Assistant</h2>

<hr>

<p>Hello Citizen 👋</p>

<p>I can help you:</p>

✅ Classify complaints

✅ Detect complaint priority

✅ Generate complaint summary

✅ Suggest department

✅ Answer Smart City questions

</div>
""",
        unsafe_allow_html=True
    )
