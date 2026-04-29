from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200

def test_get_events_returns_list():
    response = client.get("/events")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
