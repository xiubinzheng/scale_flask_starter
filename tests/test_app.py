import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_environment_ready():
    assert 1 == 1


def test_hello_world(client):
    response = client.get("/hello_world")
    assert response.status_code == 200
    assert response.json == {"hello": "world"}


def test_echo(client):
    response = client.post("/echo", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json == {"received": {"text": "hello"}}


def test_echo_requires_json_object(client):
    response = client.post("/echo", data="not json", content_type="text/plain")
    assert response.status_code == 400
