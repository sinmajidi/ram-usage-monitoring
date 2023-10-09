import requests
BASE_URL = "http://localhost:8000"

def test_login_endpoint():
    response = requests.get(f"{BASE_URL}/login", auth=("sin.majidi@gmail.com", "123456"))
    assert response.status_code == 200
    assert "message" in response.json()

def test_get_ram_data_endpoint():
    response = requests.get(f"{BASE_URL}/get_ram_data/")
    assert response.status_code == 200
    assert "ram_data" in response.json() or "message" in response.json()