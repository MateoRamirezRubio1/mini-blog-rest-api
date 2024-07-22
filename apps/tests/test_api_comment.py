import pytest
from rest_framework import status
from django.urls import reverse
from apps.comments.models import Comment
from rest_framework.exceptions import APIException
from apps.comments.views.api_views import CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView
from rest_framework.serializers import Serializer

class MockSerializer(Serializer):
    validated_data = {"content": "Test comment"}

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

@pytest.mark.django_db
def test_get_queryset_raises_kwargs_does_not_exists(api_client):
    view = CommentListCreateAPIView()
    view.kwargs = {}

    try:
        view.get_queryset()
    except APIException as exc:
        # Verifica los detalles del error
        assert str(exc) == "Post ID is required to fetch comments."

@pytest.mark.django_db
def test_get_queryset_raises_invalid_kwargs_format(api_client):
    view = CommentListCreateAPIView()
    view.kwargs = {"post_id": "invalid"}

    try:
        view.get_queryset()
    except APIException as exc:
        # Verifica los detalles del error
        assert str(exc) == "Invalid Post ID format."
    
@pytest.mark.django_db
def test_perform_create_raises_kwargs_does_not_exists(api_client):
    view = CommentListCreateAPIView()
    view.kwargs = {}

    try:
        view.perform_create({})
    except APIException as exc:
        # Verifica los detalles del error
        assert str(exc) == "Post ID is required to create a comment."

@pytest.mark.django_db
def test_perform_create_invalid_post_id():
    view = CommentListCreateAPIView()
    view.kwargs = {"post_id": "invalid"}

    serializer = MockSerializer(data={"content": "Test comment"})
    serializer.is_valid()  # Simula la validación exitosa del serializer

    with pytest.raises(APIException) as excinfo:
        view.perform_create(serializer)
    assert str(excinfo.value) == "Invalid Post ID format."

@pytest.mark.django_db
def test_retrieve_queryset_raises_kwargs_does_not_exists(api_client):
    view = CommentRetrieveUpdateDestroyAPIView()
    view.kwargs = {}

    try:
        view.get_object()
    except APIException as exc:
        # Verifica los detalles del error
        assert str(exc) == "Post ID and Comment ID are required to fetch the comment."

@pytest.mark.django_db
def test_retrieve_queryset_raises_invalid_kwargs_format(api_client):
    view = CommentRetrieveUpdateDestroyAPIView()
    view.kwargs = {"comment_pk": "invalid", "post_id": "invalid"}

    try:
        view.get_object()
    except APIException as exc:
        # Verifica los detalles del error
        assert str(exc) == "Invalid Post or Comment ID format."

@pytest.mark.django_db
def test_perform_update_raises_kwargs_does_not_exists(api_client):
    view = CommentRetrieveUpdateDestroyAPIView()
    view.kwargs = {}

    try:
        view.perform_update({})
    except APIException as exc:
        # Verifica los detalles del error
        assert str(exc) == "Comment ID is required to update the comment."

@pytest.mark.django_db
def test_perform_update_invalid_comment_id():
    view = CommentRetrieveUpdateDestroyAPIView()
    view.kwargs = {"comment_pk": "invalid"}

    serializer = MockSerializer(data={"content": "Test comment"})
    serializer.is_valid()  # Simula la validación exitosa del serializer

    with pytest.raises(APIException) as excinfo:
        view.perform_update(serializer)
    assert str(excinfo.value) == "Invalid Comment ID format."

@pytest.mark.django_db
def test_perform_destroy_raises_kwargs_does_not_exists(api_client):
    view = CommentRetrieveUpdateDestroyAPIView()
    view.kwargs = {}  # Falta comment_pk

    with pytest.raises(APIException) as excinfo:
        view.perform_destroy(None)
    assert str(excinfo.value) == "Comment ID is required to delete the comment."

@pytest.mark.django_db
def test_perform_destroy_raises_invalid_comment_pk():
    view = CommentRetrieveUpdateDestroyAPIView()
    view.kwargs = {"comment_pk": "invalid"}

    with pytest.raises(APIException) as excinfo:
        view.perform_destroy(None)
    assert str(excinfo.value) == "Invalid Comment ID format."