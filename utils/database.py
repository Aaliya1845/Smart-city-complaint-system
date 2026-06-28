import sqlite3
from pathlib import Path

DB_PATH = Path("database.db")


def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Complaints Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        complaint_id TEXT UNIQUE,
        user_email TEXT,
        category TEXT,
        priority TEXT,
        location TEXT,
        description TEXT,
        image TEXT,
        status TEXT DEFAULT 'Pending',
        ai_summary TEXT,
        assigned_department TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
