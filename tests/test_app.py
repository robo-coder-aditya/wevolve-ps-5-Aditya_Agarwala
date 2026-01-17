from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home_page_loads():
    response = client.get("/")
    assert response.status_code == 200
    assert "Skills Gap" in response.text


def test_applications_success_flow():
    payload = {
        "currentRole": "Backend Developer",
        "targetRole": "Senior Backend Developer",
        "experience": 1,
        "education": "B.Tech CS",
        "skills_selected": ["Python", "FastAPI"]
    }

    response = client.post("/applications", data=payload)

    assert response.status_code == 200

    html = response.text

    # Core content checks
    assert "Senior Backend Developer" in html
    assert "Skill Gap Percentage" in html
    assert "Learning Roadmap" in html
    assert "Readiness Score" in html
    assert "Success Rate" in html


def test_applications_no_skills_selected():
    payload = {
        "currentRole": "Backend Developer",
        "targetRole": "Senior Backend Developer",
        "experience": 1,
        "education": "B.Tech CS"
    }

    response = client.post("/applications", data=payload)

    assert response.status_code == 200
    assert "Please select at least one skill" in response.text
