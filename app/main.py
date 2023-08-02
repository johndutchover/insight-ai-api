import os
from pydantic import BaseModel, Field
from fastapi import FastAPI
from app.routers import facts, translate

app = FastAPI()

app.include_router(facts.router, prefix="/facts", tags=["facts"])
app.include_router(translate.router, prefix="/translate", tags=["translate"])

marvin_openai_api_key = os.environ.get("MARVIN_OPENAI_API_KEY")


class Location(BaseModel):
    city: str
    state: str = Field(..., description="The two-letter state abbreviation")


@app.post("/location/")
def create_location(location: Location):
    return {"location": location}


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
