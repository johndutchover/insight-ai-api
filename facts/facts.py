from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def random_fact(word: str):
    """Get a random fact for a word"""
    return {"fact": "42 is the response to the most important question"}
