import os
import marvin

from fastapi import APIRouter
from marvin import ai_fn

router = APIRouter()

marvin.settings.llm_model = "openai/gpt-3.5-turbo"
marvin_openai_api_key = os.environ.get("MARVIN_OPENAI_API_KEY")

# Set the OpenAI API key in marvin's settings
marvin.settings.openai.api_key = marvin_openai_api_key


@ai_fn
def random_fact(n: int) -> dict[int, str]:
    """
    Get a random fact for `n` and return it in a dictionary with `n` as the key.

    Args:
        n (int): The number for which a random fact is to be generated.

    Returns:
        dict[int, str]: A dictionary with `n` as the key and the
         generated fact as the value.
         :param n:
    """


@router.post("/fact_for_number")
def fact_for_number(n: int) -> dict[int, str]:
    return random_fact(n)
