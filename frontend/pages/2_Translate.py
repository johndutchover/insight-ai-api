import streamlit as st
import requests
import logging
from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.environ.get("BASE_URL")


def translate(text: str, language: str):
    endpoint = f"translate/translate?text={text}&language={language}"
    url = base_url + endpoint
    logging.info(f"Requesting {url}")
    response = requests.post(url, timeout=5)

    if response.status_code == 200:
        return response.text
    else:
        st.error("Failed to translate the text.")
        return ""


def create_poem(text: str):
    endpoint = f"poem/poem?text={text}"
    url = base_url + endpoint
    logging.info(f"Requesting {url}")
    response = requests.post(url, timeout=5)

    if response.status_code == 200:
        return response.text.strip('"')
    else:
        st.error("Failed to create a poem.")
        return


st.title("Translators")

user_input_text = st.text_area("Enter the text to translate", "book")

if st.button("Czech out this poem"):
    if user_input_text:
        translation = translate(user_input_text, language="czech")
        poem = create_poem(translation)
        if translation:
            st.subheader("Translation:")
            st.code(translation)
            st.subheader("Here is a poem about the translation:")
            poem = poem.replace(
                "\\n", "\n"
            )  # Replacing literal "\n" with actual newline characters
            st.code(poem)
