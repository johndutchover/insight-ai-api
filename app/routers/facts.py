import os
import marvin

from fastapi import APIRouter
from marvin import ai_fn
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

router = APIRouter()

marvin.settings.llm_model = "openai/gpt-3.5-turbo"
marvin_openai_api_key = os.environ.get("MARVIN_OPENAI_API_KEY")

# Set the OpenAI API key in marvin's settings
marvin.settings.openai.api_key = marvin_openai_api_key


@router.post("/fact_for_number")
@ai_fn
def random_fact(n: int) -> dict[str, str]:
    """
    Get a random fact for `n` and return it in a dictionary with `n` as the key.

    Args:
        n (int): The number for which a random fact is to be generated.

    Returns:
        dict[str, str]: A dictionary with `n` as the key and the
         generated fact as the value.
    """
    fact = ...  # get the fact for `n`
    return {str(n): fact}
