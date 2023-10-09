import requests
BASE_URL = "http://localhost:8000"

def test_successful_login():
    response = requests.get(f"{BASE_URL}/login", auth=("sin.majidi@gmail.com", "123456"))
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "you are logged in"

def test_failed_login():
    response = requests.get(f"{BASE_URL}/login", auth=("wrongemail@example.com", "wrongpassword"))
    assert response.status_code == 401  # Unauthorized
    assert "detail" in response.json()
    assert response.json()["detail"] == "Authentication failed"