import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import requests


def translate_german(text):
    api_url = f"https://insight-ai-api.fly.dev/translate/translate?text={text}"
    headers = {"accept": "application/json"}
    response = requests.post(api_url, headers=headers, data="", timeout=5)

    if response.status_code == 200:
        return response.json().get("translation", "")
    else:
        st.error("Failed to translate the text.")
        return ""


def translate_english(text):
    return translate_german(text)


st.title("Translators")

# Check for the translation button click
if st.button("German to English"):
    user_input = st.text_input("Enter the German word you want to translate:")
    if user_input:
        translation = translate_english(user_input)
        st.write(f"Translation: {translation}")
    else:
        st.write("Please enter a word to translate.")

# Check for the home button click
if st.button("Home"):
    switch_page("Home")
