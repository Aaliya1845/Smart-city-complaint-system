import streamlit as st
import sqlite3
import pandas as pd

from utils.charts import get_category_chart, get_status_chart

DB_NAME = "database.db"

def show_admin_dashboard():

    st.title("👨‍💼 Admin Dashboard")

    conn = sqlite3.connect(DB_NAME)

    total = pd.read_sql_query(
        "SELECT COUNT(*) AS total FROM complaints",
        conn
    ).iloc[0]["total"]

    pending = pd.read_sql_query(
        "SELECT COUNT(*) AS total FROM complaints WHERE status='Pending'",
        conn
    ).iloc[0]["total"]

    resolved = pd.read_sql_query(
        "SELECT COUNT(*) AS total FROM complaints WHERE status='Resolved'",
        conn
    ).iloc[0]["total"]

    progress = pd.read_sql_query(
        "SELECT COUNT(*) AS total FROM complaints WHERE status='In Progress'",
        conn
    ).iloc[0]["total"]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total", total)
    c2.metric("Pending", pending)
    c3.metric("Resolved", resolved)
    c4.metric("In Progress", progress)

    st.divider()

    st.subheader("📊 Analytics")

col1, col2 = st.columns(2)

with col1:
    category_chart = get_category_chart()
    if category_chart:
        st.plotly_chart(category_chart, use_container_width=True)

with col2:
    status_chart = get_status_chart()
    if status_chart:
        st.plotly_chart(status_chart, use_container_width=True)

st.divider()

    st.subheader("All Complaints")

    df = pd.read_sql_query(
        """
        SELECT
        complaint_id,
        category,
        priority,
        status,
        location,
        created_at
        FROM complaints
        ORDER BY created_at DESC
        """,
        conn
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    conn.close()
