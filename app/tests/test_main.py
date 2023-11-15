from fastapi.testclient import TestClient
from app.main import app
from fastapi.encoders import jsonable_encoder

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == jsonable_encoder({"n": None, "color": None})
