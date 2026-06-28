import pandas as pd
import os
import hashlib


USER_FILE = "data/users.csv"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def create_user(name, email, password):

    os.makedirs("data", exist_ok=True)

    if os.path.exists(USER_FILE):
        df = pd.read_csv(USER_FILE)
    else:
        df = pd.DataFrame(
            columns=["Name", "Email", "Password"]
        )

    if email in df["Email"].values:
        return False

    new_user = {
        "Name": name,
        "Email": email,
        "Password": hash_password(password)
    }

    df = pd.concat(
        [df, pd.DataFrame([new_user])],
        ignore_index=True
    )

    df.to_csv(USER_FILE, index=False)

    return True


def login_user(email, password):

    if not os.path.exists(USER_FILE):
        return False

    df = pd.read_csv(USER_FILE)

    user = df[df["Email"] == email]

    if user.empty:
        return False

    stored = user.iloc[0]["Password"]

    return stored == hash_password(password)
