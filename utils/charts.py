import sqlite3
import pandas as pd
import plotly.express as px

DB_NAME = "database.db"


def get_category_chart():
    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query("""
        SELECT category, COUNT(*) AS count
        FROM complaints
        GROUP BY category
    """, conn)

    conn.close()

    if df.empty:
        return None

    fig = px.pie(
        df,
        names="category",
        values="count",
        title="Complaints by Category"
    )

    return fig


def get_status_chart():
    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query("""
        SELECT status, COUNT(*) AS count
        FROM complaints
        GROUP BY status
    """, conn)

    conn.close()

    if df.empty:
        return None

    fig = px.bar(
        df,
        x="status",
        y="count",
        title="Complaint Status Overview"
    )

    return fig
