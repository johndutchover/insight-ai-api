from main import app

from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_root(n: int = 10, color: str = "blue"):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"n": n, "color": color}
