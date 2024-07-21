import pytest
from django.urls import reverse
from django.test import Client
from bs4 import BeautifulSoup


@pytest.fixture
def client():
    """
    Provide a Django test client instance for making HTTP requests.

    Returns:
        Client: An instance of Django's test Client class.
    """
    return Client()


def test_post_list_view(client, post):
    """
    Verify that the Post list view returns a successful response and includes the title of an existing Post.

    Args:
        client: The Django test client fixture for making HTTP requests.
        post: The Post fixture providing a Post object.

    Asserts:
        The response status should be HTTP 200 OK.
        The response content should include the title of the Post.
    """
    response = client.get(reverse("post-list"))
    assert response.status_code == 200
    assert b"Test Post" in response.content


def test_post_detail_view(client, post):
    """
    Verify that the Post detail view returns a successful response and includes the title of the specific Post.

    Args:
        client: The Django test client fixture for making HTTP requests.
        post: The Post fixture providing a Post object.

    Asserts:
        The response status should be HTTP 200 OK.
        The response content should include the title of the Post.
    """
    response = client.get(reverse("post-detail", args=[post.id]))
    assert response.status_code == 200
    assert b"Test Post" in response.content


def test_comment_list_view(client, comment):
    """
    Verify that the Comment list view returns a successful response and includes the content of comments for a specific Post.

    Args:
        client: The Django test client fixture for making HTTP requests.
        comment: The Comment fixture providing a Comment object.

    Asserts:
        The response status should be HTTP 200 OK.
        The response content should include the text of the comments.
    """
    response = client.get(reverse("post-comments", args=[comment.post.id]))
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, "html.parser")
    comments = soup.find_all("li")
    comment_texts = [comment.get_text() for comment in comments]
    assert "This is a test comment" in comment_texts


def test_comment_detail_view(client, comment):
    """
    Verify that the Comment detail view returns a successful response and includes the content of a specific Comment.

    Args:
        client: The Django test client fixture for making HTTP requests.
        comment: The Comment fixture providing a Comment object.

    Asserts:
        The response status should be HTTP 200 OK.
        The response content should include the text of the Comment.
    """
    response = client.get(
        reverse("post-comment-detail", args=[comment.post.id, comment.id])
    )
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, "html.parser")
    comments = soup.find_all("p")
    comment_texts = [comment.get_text() for comment in comments]
    assert "This is a test comment" in comment_texts
