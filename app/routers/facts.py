import marvin
from fastapi import APIRouter
from marvin import ai_fn

router = APIRouter()

marvin.settings.llm_model = "openai/gpt-3.5-turbo"


@router.post("/fact_for_number")
@ai_fn
def random_fact(n: int) -> dict[int, str]:
    """Get a random fact for `n` and return both as a dictionary with `n` as key
    and the random fact as value"""
