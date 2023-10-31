import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Home")

# This code has a filename of 1_Home.py and is written in Python.

if st.button("Language Translators"):
    switch_page("Translate")
else:
    st.write("Goodbye")
