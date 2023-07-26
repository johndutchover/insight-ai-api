from fastapi import FastAPI

from translate.translate import router as translate_router
from facts.facts import router as facts_router

# Create an instance of the FastAPI app
app = FastAPI()

app.include_router(translate_router, prefix="/translate")
app.include_router(facts_router, prefix="/fact_for_number")


# Define a route for the root endpoint ("/")
@app.get("/")
def read_root():
    return {"msg": "Hello World"}


# Run the application using uvicorn server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
