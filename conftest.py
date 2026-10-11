import pytest
from utils.api_client import ApiClient

@pytest.fixture(scope="session")
def api_client() -> ApiClient:
    return ApiClient()

@pytest.fixture
def sample_post_payload() -> dict:
    return {
        "title": "QA automation with pytest",
        "body": "Created by an automated API test",
        "userId": 1,
    }
