import marvin

from fastapi import APIRouter

router = APIRouter()


@marvin.fn
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
    if n == 0:
        return {0: "The factorial of 0 is 1."}
    else:
        return random_fact(n)
