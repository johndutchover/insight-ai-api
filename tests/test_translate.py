from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_translate():
    response = client.post("/translate/", json={"text": "Good day"})
    assert response.status_code == 200
    assert response.json() == {"translation": "Guten Tag"}
