import os
import tempfile

database_file = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
database_file.close()
os.environ["DATABASE_URL"] = f"sqlite:///{database_file.name}"

from fastapi.testclient import TestClient  # noqa: E402
from app.main import app  # noqa: E402


def test_task_lifecycle():
    with TestClient(app) as client:
        assert client.get("/health").json() == {"status": "ok"}
        version_response = client.get("/version")
        assert version_response.status_code == 200
        assert version_response.json() == {"version": "0.1.0"}

        created = client.post("/tasks", json={"title": "Learn Docker"})
        assert created.status_code == 201
        task = created.json()
        assert task["completed"] is False

        updated = client.patch(f"/tasks/{task['id']}", json={"completed": True})
        assert updated.status_code == 200
        assert updated.json()["completed"] is True

        assert client.get("/tasks").json() == [updated.json()]
        assert client.delete(f"/tasks/{task['id']}").status_code == 204
        assert client.get("/tasks").json() == []
