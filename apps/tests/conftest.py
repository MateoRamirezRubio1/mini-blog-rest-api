import pytest
from rest_framework.test import APIClient
from django.test import Client
from apps.posts.models import Post
from apps.comments.models import Comment


# Fixture to create a Post instance for testing
@pytest.fixture
def post(db):
    """
    Create a Post instance with title and content for testing.

    Args:
        db: The pytest fixture that sets up a test database.

    Returns:
        Post: A Post object with predefined title and content.
    """
    return Post.objects.create(title="Test Post", content="This is a test post")


# Fixture to create a Comment instance for testing, linked to a Post
@pytest.fixture
def comment(db, post):
    """
    Create a Comment instance associated with the provided Post.

    Args:
        db: The pytest fixture that sets up a test database.
        post: The Post fixture providing a Post object.

    Returns:
        Comment: A Comment object linked to the provided Post.
    """
    return Comment.objects.create(content="This is a test comment", post=post)

@pytest.fixture
def api_client():
    """
    Provide an instance of APIClient for making API requests.

    Returns:
        APIClient: An instance of the APIClient class.
    """
    return APIClient()

@pytest.fixture
def client():
    """
    Provide a Django test client instance for making HTTP requests.

    Returns:
        Client: An instance of Django's test Client class.
    """
    return Client()


