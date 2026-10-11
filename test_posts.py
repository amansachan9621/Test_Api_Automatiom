import pytest

@pytest.mark.smoke
def test_get_existing_post_returns_expected_data(api_client):
    response = api_client.get("/posts/1")
    assert response.status_code == 200

    body = response.json()
    assert body["id"] == 1
    assert body["userId"] == 1
    assert isinstance(body["title"], str)
    assert body["title"]
    assert isinstance(body["body"], str)

@pytest.mark.regression
@pytest.mark.parametrize("post_id", [1, 2, 5, 10])
def test_get_multiple_existing_posts(api_client, post_id):
    response = api_client.get(f"/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id

@pytest.mark.regression
def test_create_post_returns_created_resource(api_client, sample_post_payload):
    response = api_client.post("/posts", json=sample_post_payload)
    assert response.status_code == 201

    body = response.json()
    assert body["title"] == sample_post_payload["title"]
    assert body["body"] == sample_post_payload["body"]
    assert body["userId"] == sample_post_payload["userId"]
    assert "id" in body

@pytest.mark.regression
def test_get_posts_by_user_id(api_client):
    response = api_client.get("/posts", params={"userId": 1})
    assert response.status_code == 200

    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0
    assert all(post["userId"] == 1 for post in posts)

@pytest.mark.negative
def test_get_non_existing_post_returns_empty_object(api_client):
    response = api_client.get("/posts/999999")
    assert response.status_code == 404
    assert response.json() == {}

@pytest.mark.regression
def test_delete_post_returns_success(api_client):
    response = api_client.delete("/posts/1")
    assert response.status_code == 200
    assert response.json() == {}

@pytest.mark.regression
def test_get_comments(api_client):
    response = api_client.get("/posts/1/comments")
    assert response.status_code == 200

    comments = response.json()

    assert isinstance(comments, list)
    assert len(comments) > 0
    assert all(comment["postId"] == 1 for comment in comments)
    assert all("email" in comment for comment in comments)
    assert all(comment["email"] != "" for comment in comments)
    assert all("@" in comment["email"] for comment in comments)
