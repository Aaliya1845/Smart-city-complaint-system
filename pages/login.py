import streamlit as st

from utils.authentication import create_user
from utils.authentication import login_user


def show_login():

    st.title("🔐 Login")

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:

        email = st.text_input(
            "Email",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_pass"
        )

        if st.button("Login"):

            user = login_user(email, password)

if user:

    st.session_state.logged_in = True
    st.session_state.email = email
    st.session_state.user_name = user[1]

    st.success("Welcome " + user[1] + " 🎉")

    st.rerun()

else:

    st.error("Invalid Email or Password")

            else:

                st.error("Invalid Credentials")

    with tab2:

        name = st.text_input(
            "Full Name"
        )

        email = st.text_input(
            "Email",
            key="signup_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="signup_pass"
        )

        if st.button("Create Account"):

            success = create_user(
                name,
                email,
                password
            )

            if success:

                st.success(
                    "Account Created Successfully!"
                )

            else:

                st.warning(
                    "Email already exists."
                )
