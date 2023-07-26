from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def translate(text: str):
    """Get a German response"""
    return {"translation": "Guten Tag."}
