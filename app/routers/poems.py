import marvin
from fastapi import APIRouter

router = APIRouter()


@marvin.fn
def create_poem_ai(text: str) -> str:
    """Create a poetic interpretation of the given input text. Transform the meaning, theme, or emotion of the input
    into a long poem, using creative language and metaphors."""


@router.post("/poem")
def create_poem(text: str) -> str:
    return create_poem_ai(text)
