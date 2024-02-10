from pydantic import BaseModel
from typing import Dict
import marvin
from fastapi import APIRouter

router = APIRouter()


class FormatResponse(BaseModel):
    value: Dict[int, str]


@marvin.fn
def random_fact(n: int) -> Dict[int, str]:
    """
    Get a random fact for `n` and return it in a dictionary with `n` as the key.

    Args:
        n (int): The number for which a random fact is to be generated.

    Returns:
        dict[int, str]: A dictionary with `n` as the key and the generated fact as the value.
    """
    if n == 0:
        return {0: "The factorial of 0 is 1."}
    else:
        return {n: f"A placeholder fact for {n}."}


@router.post("/random_fact")
def get_random_fact(n: int) -> Dict[int, str]:
    return random_fact(n)
