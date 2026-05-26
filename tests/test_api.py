def test_root_redirects_to_static_index(client):
    # Arrange
    # No special setup is needed for this endpoint.

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activity_names = [
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Soccer Team",
        "Basketball Team",
        "Art Club",
        "Drama Club",
        "Science Club",
        "Debate Club",
    ]

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()

    assert len(data) == len(expected_activity_names)
    for activity_name in expected_activity_names:
        assert activity_name in data
        assert "description" in data[activity_name]
        assert "schedule" in data[activity_name]
        assert "max_participants" in data[activity_name]
        assert "participants" in data[activity_name]
        assert isinstance(data[activity_name]["participants"], list)


def test_signup_for_activity_success(client):
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"

    refreshed_response = client.get("/activities")
    refreshed_data = refreshed_response.json()
    assert email in refreshed_data[activity_name]["participants"]


def test_signup_for_activity_rejects_duplicate_email(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_for_missing_activity_returns_404(client):
    # Arrange
    activity_name = "Nonexistent Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]
