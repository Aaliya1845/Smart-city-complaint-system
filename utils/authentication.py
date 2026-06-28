import sqlite3
import hashlib

DB_NAME = "database.db"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def create_user(name, email, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    existing = cursor.fetchone()

    if existing:
        conn.close()
        return False

    cursor.execute(
        """
        INSERT INTO users(name, email, password)
        VALUES (?, ?, ?)
        """,
        (name, email, hash_password(password)),
    )

    conn.commit()
    conn.close()

    return True


def login_user(email, password):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, hash_password(password)),
    )

    user = cursor.fetchone()

    conn.close()

    return user
