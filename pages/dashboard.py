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

    from utils.cards import stat_card

c1, c2, c3, c4 = st.columns(4)

with c1:
    stat_card(
        "Total",
        "128",
        "📋",
        "#FFE8F2"
    )

with c2:
    stat_card(
        "Resolved",
        "96",
        "✅",
        "#DFF7FF"
    )

with c3:
    stat_card(
        "Pending",
        "24",
        "🚧",
        "#FFF0DE"
    )

with c4:
    stat_card(
        "Urgent",
        "08",
        "🚨",
        "#FDE7EA"
    )

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
