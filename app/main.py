from fastapi import FastAPI
from app.routers import facts, translate

app = FastAPI()

app.include_router(facts.router, prefix="/facts", tags=["facts"])
app.include_router(translate.router, prefix="/translate", tags=["translate"])


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
