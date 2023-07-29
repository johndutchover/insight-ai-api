from fastapi import APIRouter

router = APIRouter()


@router.post("/fact_for_number")
def random_fact() -> dict[str, str]:
    """Get a random fact for a number"""
    return {"fact": "10 is the base of the decimal numeral system."}
