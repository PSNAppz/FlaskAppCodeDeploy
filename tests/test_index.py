import requests


def test_index():
    # Test
    response = requests.get("http://127.0.0.1:5000/")
    assert response.status_code == 200
