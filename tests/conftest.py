import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture(autouse=True)
def reset_activities():
    initial_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"],
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"],
        },
        "Soccer Team": {
            "description": "Competitive soccer team practices and matches",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 25,
            "participants": ["liam@mergington.edu"],
        },
        "Basketball Team": {
            "description": "Team practices, drills, and inter-school games",
            "schedule": "Mondays, Wednesdays, 4:30 PM - 6:30 PM",
            "max_participants": 20,
            "participants": ["noah@mergington.edu"],
        },
        "Art Club": {
            "description": "Explore drawing, painting, and mixed media projects",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["ava@mergington.edu"],
        },
        "Drama Club": {
            "description": "Acting, stagecraft, and school productions",
            "schedule": "Fridays, 3:30 PM - 6:00 PM",
            "max_participants": 30,
            "participants": ["isabella@mergington.edu"],
        },
        "Science Club": {
            "description": "Hands-on experiments and science fair projects",
            "schedule": "Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 20,
            "participants": ["ethan@mergington.edu"],
        },
        "Debate Club": {
            "description": "Practice debating, public speaking, and tournaments",
            "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
            "max_participants": 24,
            "participants": ["mia@mergington.edu"],
        },
    }

    activities.clear()
    activities.update(copy.deepcopy(initial_activities))

    yield

    activities.clear()
    activities.update(copy.deepcopy(initial_activities))


@pytest.fixture
def client():
    return TestClient(app)
