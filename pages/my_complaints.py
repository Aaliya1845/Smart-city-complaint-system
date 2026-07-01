import streamlit as st
import pandas as pd
import sqlite3

DB_NAME = "database.db"


def show_my_complaints():

    st.title("📂 My Complaints")

    email = st.session_state.get("email")

    conn = sqlite3.connect(DB_NAME)

    query = """
    SELECT
        complaint_id,
        category,
        priority,
        location,
        status,
        created_at
    FROM complaints
    WHERE user_email = ?
    ORDER BY created_at DESC
    """

    df = pd.read_sql_query(query, conn, params=(email,))

    conn.close()

    if df.empty:
        st.info("You haven't submitted any complaints yet.")
        return

    # ---------- Filters ----------

    col1, col2 = st.columns(2)

    with col1:
        status = st.selectbox(
            "Filter by Status",
            ["All"] + sorted(df["status"].unique().tolist())
        )

    with col2:
        category = st.selectbox(
            "Filter by Category",
            ["All"] + sorted(df["category"].unique().tolist())
        )

    filtered = df.copy()

    if status != "All":
        filtered = filtered[
            filtered["status"] == status
        ]

    if category != "All":
        filtered = filtered[
            filtered["category"] == category
        ]

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )
