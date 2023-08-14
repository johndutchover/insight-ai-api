import os
import streamlit as st
from dotenv import load_dotenv
from streamlit_extras.switch_page_button import switch_page

load_dotenv(".env")


def check_password():
    """Check if the password has been entered correctly."""
    if st.session_state.get("password_correct"):
        return True

    password = st.text_input("Password", type="password", key="unique_password_input")
    expected_password = os.environ.get("FE_PWD")

    if expected_password is None:
        st.error("Password not configured")
        return False

    if password == expected_password:
        st.session_state["password_correct"] = True
        return True
    else:
        st.error("Incorrect password")
        return False


# Prompt for password
if check_password():
    # Set a flag in the session state to indicate that the password is correct
    st.session_state["password_correct"] = True
    # Redirect using extras switch_page
    switch_page("Home")


# Prompt for password
if check_password():
    # Set a flag in the session state to indicate that the password is correct
    st.session_state["password_correct"] = True
    # Redirect using extras switch_page
    switch_page("Home")
