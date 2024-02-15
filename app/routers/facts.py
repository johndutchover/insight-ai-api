from pydantic import BaseModel
import marvin
from fastapi import APIRouter

router = APIRouter()


class FormatResponse(BaseModel):
    value: str


@marvin.fn
def generate_fact_ai(n: int) -> str:
    """
    Get a random fact for `n` and return only the value of dictionary in response.

    Args:
        n (int): The number for which a random fact is to be generated.

    Returns:
        str: The generated fact as the value.
    """


@router.post("/fact_to_number", response_model=FormatResponse)
async def get_text_post(n: int) -> FormatResponse:
    return FormatResponse(value=generate_fact_ai(n))


@router.get("/fact_to_number", response_model=FormatResponse)
async def get_text_get(n: int) -> FormatResponse:
    return FormatResponse(value=generate_fact_ai(n))
