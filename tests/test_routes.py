import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"To-Do List" in response.data


def test_add_task(client):
    response = client.post(
        '/add',
        data={"title": "Test Task"},
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b"Test Task" in response.data


def test_add_empty_task(client):
    initial_task_count = len(client.get('/').data.split(b'<li>')) - 1
    response = client.post(
        '/add',
        data={"title": ""},
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b"To-Do List" in response.data
    updated_task_count = len(client.get('/').data.split(b'<li>')) - 1
    assert updated_task_count == initial_task_count


def test_complete_task(client):
    client.post('/add', data={"title": "Complete Me"}, follow_redirects=True)
    response = client.get('/complete/0', follow_redirects=True)
    assert response.status_code == 200
    assert b"Completed" in response.data
