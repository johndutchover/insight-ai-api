import os

import marvin
from fastapi import FastAPI
from marvin import ai_fn, ai_model, AIApplication
from pydantic import BaseModel

from .routers import facts, poems, translate

marvin.settings.llm_model = "openai/gpt-3.5-turbo"
marvin_openai_api_key = os.getenv("MARVIN_OPENAI_API_KEY")

# Create FastAPI instance
app = FastAPI()

app.include_router(facts.router)
app.include_router(poems.router)
app.include_router(translate.router)


# Definite a response model for root endpoint
class RootResponse(BaseModel):
    n: int | None = None
    color: str | None = None


# Definite a route for the root endpoint
@app.get("/")
async def root():
    """Get the root with optional parameters n and color."""
    return {"n": None, "color": None}


# Include APIRouter objects
app.include_router(facts.router, prefix="/facts", tags=["facts"])
app.include_router(translate.router, prefix="/translate", tags=["translate"])
app.include_router(poems.router, prefix="/poem", tags=["poem"])


# Setup the insight-ai-api application
class Insight(BaseModel):
    name: str | None = None
    description: str | None = None
    done: bool = False


class InsightState(BaseModel):
    todos: list[Insight] = []


insight_app = AIApplication(
    state=InsightState(),
    description="A simple app to provide insights using OpenAI.",
)


# Define routes for generating fruits and vegetables
@ai_fn
async def generate_fruits(n: int, color: str) -> list[str]:
    """Generates a list of `n` fruits"""
    return ["apple", "banana", "orange"]


@ai_fn
def generate_vegetables(n: int, color: str) -> list[str]:
    """Generates a list of `n` vegetables of color `color`"""
    return ["carrot", "potato", "onion"]


# Define a pydantic model for a person
@ai_model
class Person(BaseModel):
    first_name: str
    last_name: str


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
