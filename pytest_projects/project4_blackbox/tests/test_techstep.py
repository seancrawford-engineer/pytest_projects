import requests

def test_get_successful_response():
    resp = requests.get("https://techstepacademy.com/training-ground")
    assert resp.status_code == 200
    