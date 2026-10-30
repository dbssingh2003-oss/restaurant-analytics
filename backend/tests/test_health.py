
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "healthy",
        "service": "restaurant-analytics-backend",
    }


def test_home_page():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Welcome to the Restaurant Intelligence Platform API",
        "status": "running",
    }
