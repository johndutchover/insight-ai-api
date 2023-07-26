from fastapi import FastAPI

# Create an instance of the FastAPI app
app = FastAPI()


# Define a route for the root endpoint ("/")
@app.get("/")
def read_root():
    return {"Hello": "World"}


# Define a route to post translations
@app.post("/translate/")
def translate(text: str):
    """Get a German response"""

    return {"translation": "Guten Tag."}


@app.post("/fact_for_number/")
def random_fact(word: str):
    """Get a random fact for a word"""

    return {"fact": "42 is the reponse to the most important question"}


# Run the application using uvicorn server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
