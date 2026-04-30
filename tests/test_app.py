import json
import pytest
from app.ACEest_Fitness import app, init_db


@pytest.fixture
def client():
    init_db()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200


def test_add_member(client):
    data = {
        "name": "TestUser",
        "age": 25,
        "plan": "Silver"
    }

    response = client.post(
        '/add_member',
        data=json.dumps(data),
        content_type='application/json'
    )

    assert response.status_code == 201
    assert b"Member added successfully" in response.data


def test_get_members(client):
    response = client.get('/members')
    assert response.status_code == 200
    data = response.get_json()
    assert "members" in data