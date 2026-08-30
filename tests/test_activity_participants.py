from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    participant_email = "michael@mergington.edu"

    response = client.delete(
        f"/activities/{activity_name}/participants?email={participant_email}"
    )

    assert response.status_code == 200
    assert response.json()["message"] == (
        f"Unregistered {participant_email} from {activity_name}"
    )

    refreshed = client.get("/activities")
    assert participant_email not in refreshed.json()[activity_name]["participants"]
