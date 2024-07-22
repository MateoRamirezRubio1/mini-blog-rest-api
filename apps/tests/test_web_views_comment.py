from django.urls import reverse
from bs4 import BeautifulSoup


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
