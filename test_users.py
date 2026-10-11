import pytest

@pytest.mark.smoke
def test_get_existing_user(api_client):
    response = api_client.get("/users/1")
    assert response.status_code == 200

    user = response.json()
    assert user["id"] == 1
    assert "name" in user
    assert "email" in user
    assert "address" in user
    assert "company" in user

@pytest.mark.regression
@pytest.mark.parametrize("user_id", [1, 3, 7])
def test_user_email_has_expected_format(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")
    assert response.status_code == 200

    email = response.json()["email"]
    assert "@" in email
    assert "." in email.split("@")[-1]

@pytest.mark.negative
def test_non_existing_user_returns_404(api_client):
    response = api_client.get("/users/999999")
    assert response.status_code == 404
    assert response.json() == {}
