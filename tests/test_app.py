import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_time_endpoint(client):
    response = client.get('/time')
    assert response.status_code == 200
    data = response.get_json()
    assert 'time' in data
    assert isinstance(data['time'], int)
    assert data['time'] > 0

def test_metrics_endpoint(client):
    # Сначала делаем несколько запросов к /time
    for _ in range(3):
        client.get('/time')
    
    response = client.get('/metrics')
    assert response.status_code == 200
    data = response.get_json()
    assert 'count' in data
    assert data['count'] == 3
