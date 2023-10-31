from fastapi.testclient import TestClient
from app.main import app
from app.routers import facts, translate  # Import the required modules

client = TestClient(app)


def test_read_root(n: int = 10, color: str = "blue"):
    # Use the imported modules to avoid unused import warning
    print(facts)
    print(translate)

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"n": n, "color": color}
