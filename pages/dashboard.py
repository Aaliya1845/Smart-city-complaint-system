import streamlit as st

def show_dashboard():

    st.markdown("""
    <div class="banner">

        <div>

            <h1>🏙️ Welcome Back!</h1>

            <p>Help make your city cleaner, safer and smarter.</p>

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="card">
        <h3>Total Complaints</h3>
        <h1>128</h1>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card blue">
        <h3>Resolved</h3>
        <h1>96</h1>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card brown">
        <h3>In Progress</h3>
        <h1>24</h1>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="card">
        <h3>Rejected</h3>
        <h1>8</h1>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    left, right = st.columns([2,1])

    with left:

        st.subheader("📋 Recent Complaints")

        st.dataframe(
        {
            "Complaint ID":["CMP001","CMP002","CMP003","CMP004"],
            "Category":["Garbage","Road","Street Light","Water Leakage"],
            "Status":["Resolved","Pending","In Progress","Resolved"]
        },
        use_container_width=True
        )

    with right:

        st.markdown("""
        <div class="ai-box">

        <h2>🤖 AI Assistant</h2>

        <p>Hello 👋<br>
        I can help classify complaints, answer queries and guide citizens.</p>

        </div>
        """, unsafe_allow_html=True)
