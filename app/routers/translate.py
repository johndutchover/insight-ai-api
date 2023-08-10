from fastapi import APIRouter
from marvin import ai_fn

router = APIRouter()


@router.post("/translate")
@ai_fn
def translate_german(text: str) -> str:
    """Translate `text` to German"""
