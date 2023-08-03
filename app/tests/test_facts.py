from fastapi.testclient import TestClient
from app.main import app
from typing import Dict

client = TestClient(app)


def test_fact_for_number():
    response = client.post("/facts/fact_for_number?n=10")
    assert response.status_code == 200

    # assert that the response is a dictionary that contains "fact" as key
    #  and the value is string type.
    assert isinstance(response.json(), Dict)
    assert "fact" in response.json()
    assert isinstance(response.json().get("fact"), str)
