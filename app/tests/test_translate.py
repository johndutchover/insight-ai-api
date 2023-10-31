from fastapi.testclient import TestClient
from app.main import app
from app.routers import facts, translate  # Import the required modules

client = TestClient(app)


def test_translate():
    # Use the imported modules to avoid unused import warning
    print(facts)
    print(translate)

    response = client.post("/translate/", json={"text": "Good day"})
    assert response.status_code == 200
    assert response.json() == {"translation": "Guten Tag"}
