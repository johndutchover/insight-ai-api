from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_fact_for_number():
    response = client.post("/facts/fact_for_number")
    assert response.status_code == 200
    assert response.json() == {"fact": "10 is the base of the decimal numeral system."}
