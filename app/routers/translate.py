from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class TranslationInput(BaseModel):
    text: str


@router.post("/")
def translate_german(data: TranslationInput):
    """Get a German response"""
    return {"translation": "Guten Tag"}
