import os

from dotenv import load_dotenv
from fastapi import FastAPI
from marvin import ai_fn, ai_model, AIApplication
from pydantic import BaseModel

from app.routers import facts, translate

load_dotenv()  # take environment variables from .env

app = FastAPI()

app.include_router(facts.router, prefix="/facts", tags=["facts"])
app.include_router(translate.router, prefix="/translate", tags=["translate"])

marvin_openai_api_key = os.environ.get("MARVIN_OPENAI_API_KEY")


# create models to represent the state of the insight-api app
class Insight(BaseModel):
    title: str
    description: str = None
    done: bool = False


class InsightState(BaseModel):
    todos: list[Insight] = []


# create the app with an initial state and description
insight_app = AIApplication(
    state=InsightState(),
    description="A simple app to provide insights using OpenAI.",
)


@app.get("/")
def read_root(n: int = 10, color: str = "blue"):
    return {"n": n, "color": color}


# https://www.askmarvin.ai/deployment/
@ai_fn
def generate_fruits(n: int) -> list[str]:
    """Generates a list of `n` fruits"""


@ai_fn
def generate_vegetables(n: int, color: str) -> list[str]:
    """Generates a list of `n` vegetables of color `color`"""


@ai_model
class Person(BaseModel):
    first_name: str
    last_name: str


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
