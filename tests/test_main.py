from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_add():
    response = client.get("/api/add?a=1&b=2")
    assert response.status_code == 200
    assert response.json() == {"answer": 3}
