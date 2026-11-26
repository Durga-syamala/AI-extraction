from fastapi.testclient import TestClient

from app.main import app
from app.models import Person
from app.exceptions import AIServiceError

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "AI Extraction Service is running"


def test_extract_success(monkeypatch):
    def mock_extract(text):
        return Person(
            name="Syamala",
            age=25,
            email="syamala@gmail.com",
            profession="Developer",
            company="ABC Tech"
        )

    monkeypatch.setattr("app.main.extract_person", mock_extract)

    response = client.post(
        "/extract",
        json={"text": "My name is Syamala"}
    )

    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"]["name"] == "Syamala"


def test_extract_error(monkeypatch):
    def mock_extract(text):
        raise AIServiceError("AI service unavailable")

    monkeypatch.setattr("app.main.extract_person", mock_extract)

    response = client.post(
        "/extract",
        json={"text": "My name is Syamala"}
    )

    assert response.status_code == 502
    assert response.json()["success"] is False