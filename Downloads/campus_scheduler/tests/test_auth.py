
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

EMAIL = "test@example.com"
PASSWORD = "secret123"

def test_signup_login_me():
    # Signup
    r = client.post("/users/signup", json={"email": EMAIL, "password": PASSWORD, "role": "student"})
    assert r.status_code in (200, 400)  # allow re-run where email already exists

    # Login
    r = client.post("/users/login", json={"email": EMAIL, "password": PASSWORD})
    assert r.status_code == 200
    token = r.json()["access_token"]

    # Me
    headers = {"Authorization": f"Bearer {token}"}
    r = client.get("/users/me", headers=headers)
    assert r.status_code == 200
    data = r.json()
    assert data["email"] == EMAIL
    assert data["role"] == "student"
