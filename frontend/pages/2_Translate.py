import streamlit as st
import requests
import logging

BASE_URL = "https://insight-ai-api.fly.dev/"
# BASE_URL = "http://localhost:8000/"


def translate(text: str, language: str):
    endpoint = f"translate/translate?text={text}&language={language}"
    url = BASE_URL + endpoint
    logging.info(f"Requesting {url}")
    response = requests.post(url, timeout=5)

    if response.status_code == 200:
        return response.text
    else:
        st.error("Failed to translate the text.")
        return ""


def create_poem(text: str):
    endpoint = f"poem/poem?text={text}"
    url = BASE_URL + endpoint
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
        translation = translate(user_input_text, language="english")
        poem = create_poem(translation)
        if translation:
            st.subheader("Translation:")
            st.code(translation)  # Displaying the translation in a monospace font
            st.subheader("Here is a poem about the translation:")
            poem = poem.replace(
                "\\n", "\n"
            )  # Replacing literal "\n" with actual newline characters
            st.code(poem)  # Displaying the poem in a monospace font
