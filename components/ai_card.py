import streamlit as st

def ai_card():

    st.image(
        "assets/ai_robot.png",
        use_container_width=True
    )

    st.markdown("""
    ### 🤖 AI Assistant

    I can help you with:

    ✅ Complaint Analysis

    ✅ Priority Prediction

    ✅ Department Recommendation

    ✅ Complaint Tracking

    ✅ City Information
    """)
