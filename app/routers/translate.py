from fastapi import APIRouter
from marvin import ai_fn

router = APIRouter()


@ai_fn
def translate_ai(text: str) -> str:
    """Given the input `text`, return a translation to czech."""


@router.post("/translate")
def translate(text: str) -> str:
    """Translate input `text` to czech."""
    # """Translate input `text` to the given output language `language`."""
    return translate_ai(text)
