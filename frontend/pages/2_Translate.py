import streamlit as st
import requests

BASE_URL = "https://insight-ai-api.fly.dev/"


def translate_eng_de(text):
    endpoint = f"translate/translate?text={text}"
    url = BASE_URL + endpoint
    response = requests.post(url, timeout=5)

    if response.status_code == 200:
        return response.text
    else:
        st.error("Failed to translate the text.")
        return ""


st.title("Translators")

user_input = st.text_area("Enter the English word you want to translate:")

if st.button("Translate to German"):
    if user_input:
        translation = translate_eng_de(user_input)
        if translation:
            st.write(f"Translation: {translation}")
