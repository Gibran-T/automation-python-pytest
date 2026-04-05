import requests
import pytest


BASE_URL = "https://jsonplaceholder.typicode.com"


class TestAPIEndpoints:
    """Professional API test suite for QA portfolio demonstration."""

    def test_get_users_status_code(self):
        """Verify GET /users returns HTTP 200."""
        response = requests.get(f"{BASE_URL}/users")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    def test_get_users_returns_list(self):
        """Verify GET /users returns a non-empty list."""
        response = requests.get(f"{BASE_URL}/users")
        data = response.json()
        assert isinstance(data, list), "Response should be a list"
        assert len(data) > 0, "User list should not be empty"

    def test_get_single_user(self):
        """Verify GET /users/1 returns correct user data."""
        response = requests.get(f"{BASE_URL}/users/1")
        assert response.status_code == 200
        user = response.json()
        assert "id" in user
        assert "name" in user
        assert "email" in user

    def test_get_posts_status_code(self):
        """Verify GET /posts returns HTTP 200."""
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200

    def test_get_posts_content_type(self):
        """Verify response Content-Type is application/json."""
        response = requests.get(f"{BASE_URL}/posts")
        assert "application/json" in response.headers.get("Content-Type", "")

    def test_create_post(self):
        """Verify POST /posts creates a new resource."""
        payload = {
            "title": "QA Test Post",
            "body": "Automated test by Gibran-T",
            "userId": 1
        }
        response = requests.post(f"{BASE_URL}/posts", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == payload["title"]

    def test_invalid_endpoint_returns_404(self):
        """Verify invalid endpoint returns HTTP 404."""
        response = requests.get(f"{BASE_URL}/nonexistent-endpoint")
        assert response.status_code == 404
