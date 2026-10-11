import pytest

@pytest.mark.regression
def test_posts_response_time_is_reasonable(api_client):
    response = api_client.get("/posts")
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 3

@pytest.mark.regression
def test_posts_response_is_json(api_client):
    response = api_client.get("/posts/1")
    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type", "")
