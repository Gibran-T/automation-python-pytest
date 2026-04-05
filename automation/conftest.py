import pytest
import requests

# ─────────────────────────────────────────────
# Base Configuration
# ─────────────────────────────────────────────

BASE_URL = "https://jsonplaceholder.typicode.com"

# ─────────────────────────────────────────────
# Session-scoped fixtures (created once per run)
# ─────────────────────────────────────────────

@pytest.fixture(scope="session")
def base_url():
    """Return the base URL for all API tests."""
    return BASE_URL


@pytest.fixture(scope="session")
def api_session():
    """
    Provide a shared requests.Session for the entire test run.
    Sets default headers to simulate a real API client.
    """
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "QA-Automation-Framework/2.0"
    })
    yield session
    session.close()


# ─────────────────────────────────────────────
# Function-scoped fixtures (created per test)
# ─────────────────────────────────────────────

@pytest.fixture
def sample_post_payload():
    """Return a valid payload for POST /posts endpoint."""
    return {
        "title": "Automated QA Test Post",
        "body": "This post was created by the automated QA framework.",
        "userId": 1
    }


@pytest.fixture
def sample_user_id():
    """Return a valid user ID for user-related tests."""
    return 1


@pytest.fixture
def invalid_endpoint(base_url):
    """Return a URL pointing to a non-existent resource."""
    return f"{base_url}/nonexistent-resource-404"


# ─────────────────────────────────────────────
# Parametrized fixtures
# ─────────────────────────────────────────────

@pytest.fixture(params=[1, 2, 3])
def valid_post_ids(request):
    """Parametrize tests across multiple valid post IDs."""
    return request.param


# ─────────────────────────────────────────────
# Hooks
# ─────────────────────────────────────────────

def pytest_configure(config):
    """Register custom markers to avoid warnings."""
    config.addinivalue_line("markers", "smoke: mark test as part of smoke suite")
    config.addinivalue_line("markers", "regression: mark test as part of regression suite")
    config.addinivalue_line("markers", "api: mark test as an API test")
