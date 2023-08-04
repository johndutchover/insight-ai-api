from fastapi.testclient import TestClient
from main import app
from typing import Dict

client = TestClient(app)


def test_fact_for_number():
    test_values = [0, 1, 2, 5, 10, 100, 999]

    for n in test_values:
        response = client.post(f"/facts/fact_for_number?n={n}")
        assert response.status_code == 200
        assert isinstance(response.json(), Dict)
        assert str(n) in response.json()  # assuming the keys are strings
        assert isinstance(
            response.json().get(str(n)), str
        )  # assuming the keys are strings
