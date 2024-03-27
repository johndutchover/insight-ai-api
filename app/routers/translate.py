import marvin
from fastapi import APIRouter

router = APIRouter()


@marvin.fn
def translate_ai(text: str) -> str:
    """Given the input `text`, return a translation to input language `language`."""


@marvin.fn
def translate_service(text: str) -> str:
    """Target language service translates my_language to target_language."""


@router.post("/translate")
def translate(text: str, my_language: str, target_language: str) -> str:
    """Return the translation of `text` from `my_language` to language `target_language`."""
    return translate_service(text)
