import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from apps.posts.models import Post
from apps.comments.models import Comment


@pytest.fixture
def api_client():
    """
    Provide an instance of APIClient for making API requests.

    Returns:
        APIClient: An instance of the APIClient class.
    """
    return APIClient()


@pytest.mark.django_db
def test_create_post(api_client):
    """
    Verify that a new Post can be created via the API.

    Args:
        api_client: The APIClient fixture for making API requests.

    Asserts:
        The response status should be HTTP 201 Created.
        The response data should include the title of the new Post.
    """
    response = api_client.post(
        reverse("post-list-create"),
        {"title": "New Post", "content": "Post content"},
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == "New Post"


def test_get_posts(api_client, post):
    """
    Verify that existing Posts can be retrieved via the API.

    Args:
        api_client: The APIClient fixture for making API requests.
        post: The Post fixture providing a Post object.

    Asserts:
        The response status should be HTTP 200 OK.
        The response data should include the title and content of the existing Post.
    """
    response = api_client.get(reverse("post-list-create"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]["title"] == "Test Post"
    assert response.data[0]["content"] == "This is a test post"


@pytest.mark.django_db
def test_create_post_invalid_data(api_client):
    """
    Verify that creating a Post with invalid data returns a HTTP 400 Bad Request.

    Args:
        api_client: The APIClient fixture for making API requests.

    Asserts:
        The response status should be HTTP 400 Bad Request.
        The response data should include errors for title and content fields.
    """
    response = api_client.post(
        reverse("post-list-create"),
        {"title": "", "content": ""},
        format="json",
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "title" in response.data
    assert "content" in response.data


@pytest.mark.django_db
def test_update_post(api_client, post):
    """
    Verify that an existing Post can be updated via the API.

    Args:
        api_client: The APIClient fixture for making API requests.
        post: The Post fixture providing a Post object.

    Asserts:
        The response status should be HTTP 200 OK.
        The updated Post in the database should reflect the new title and content.
    """
    response = api_client.put(
        reverse("post-retrieve-update-destroy", args=[post.id]),
        {
            "title": "Updated Post",
            "content": "Updated content",
            "created_at": "2024-07-08T10:10:04.611801Z",
            "updated_at": "2024-07-21T05:30:49.390684Z",
        },
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    updated_post = Post.objects.get(id=post.id)
    assert updated_post.title == "Updated Post"
    assert updated_post.content == "Updated content"


@pytest.mark.django_db
def test_delete_post(api_client, post):
    """
    Verify that an existing Post can be deleted via the API.

    Args:
        api_client: The APIClient fixture for making API requests.
        post: The Post fixture providing a Post object.

    Asserts:
        The response status should be HTTP 204 No Content.
        The Post should be removed from the database.
    """
    response = api_client.delete(
        reverse("post-retrieve-update-destroy", args=[post.id])
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Post.objects.count() == 0


@pytest.mark.django_db
def test_update_delete_post_not_found(api_client):
    """
    Verify that trying to retrieve, update, or delete a non-existent Post returns HTTP 404 Not Found.

    Args:
        api_client: The APIClient fixture for making API requests.

    Asserts:
        The response status should be HTTP 404 Not Found.
    """
    response = api_client.get(reverse("post-retrieve-update-destroy", args=[444]))

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_create_comment(api_client, post):
    """
    Verify that a new Comment can be created for a Post via the API.

    Args:
        api_client: The APIClient fixture for making API requests.
        post: The Post fixture providing a Post object.

    Asserts:
        The response status should be HTTP 201 Created.
        The response data should include the content of the new Comment.
    """
    response = api_client.post(
        reverse("post-comment-create", args=[post.id]),
        {"post": post.id, "content": "New comment"},
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["content"] == "New comment"


def test_get_comments_by_post_id(api_client, comment):
    """
    Verify that comments for a specific Post can be retrieved via the API.

    Args:
        api_client: The APIClient fixture for making API requests.
        comment: The Comment fixture providing a Comment object.

    Asserts:
        The response status should be HTTP 200 OK.
        The response data should include the content of the existing Comment.
    """
    response = api_client.get(reverse("post-comment-create", args=[comment.post.id]))

    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]["content"] == "This is a test comment"


@pytest.mark.django_db
def test_update_comment(api_client, comment):
    """
    Verify that an existing Comment can be updated via the API.

    Args:
        api_client: The APIClient fixture for making API requests.
        comment: The Comment fixture providing a Comment object.

    Asserts:
        The response status should be HTTP 200 OK.
        The updated Comment in the database should reflect the new content.
    """
    response = api_client.put(
        reverse(
            "post-comment-retrieve-update-destroy", args=[comment.post.id, comment.id]
        ),
        {"post": comment.post.id, "content": "Updated comment"},
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    updated_comment = Comment.objects.get(id=comment.id)
    assert updated_comment.content == "Updated comment"


@pytest.mark.django_db
def test_delete_comment(api_client, comment):
    """
    Verify that an existing Comment can be deleted via the API.

    Args:
        api_client: The APIClient fixture for making API requests.
        comment: The Comment fixture providing a Comment object.

    Asserts:
        The response status should be HTTP 204 No Content.
        The Comment should be removed from the database.
    """
    response = api_client.delete(
        reverse(
            "post-comment-retrieve-update-destroy", args=[comment.post.id, comment.id]
        )
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Comment.objects.count() == 0


@pytest.mark.django_db
def test_update_delete_comment_not_found(api_client):
    """
    Verify that trying to retrieve, update, or delete a non-existent Comment returns HTTP 404 Not Found.

    Args:
        api_client: The APIClient fixture for making API requests.

    Asserts:
        The response status should be HTTP 404 Not Found.
    """
    response = api_client.get(
        reverse("post-comment-retrieve-update-destroy", args=[444, 323])
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
