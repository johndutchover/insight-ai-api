from fastapi import FastAPI

# Create an instance of the FastAPI app
app = FastAPI()


# Define a route for the root endpoint ("/")
@app.get("/")
def read_root():
    return {"Hello": "World"}


# Run the application using uvicorn server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
