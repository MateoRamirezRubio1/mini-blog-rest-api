from django.urls import reverse

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