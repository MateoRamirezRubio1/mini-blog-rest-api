import pytest


def test_post_creation(post):
    """
    Verify that a Post object is created with the correct title and content.

    Args:
        post: The Post fixture providing a Post object.
    """
    assert post.title == "Test Post"
    assert post.content == "This is a test post"


def test_comment_creation(comment):
    """
    Verify that a Comment object is created with the correct content and associated Post title.

    Args:
        comment: The Comment fixture providing a Comment object.
    """
    assert comment.content == "This is a test comment"
    assert comment.post.title == "Test Post"


def test_comment_string_representation(comment):
    """
    Verify that the string representation of a Comment is correctly truncated to 20 characters.

    Args:
        comment: The Comment fixture providing a Comment object.
    """
    strComment = "This is a test comment"
    assert str(comment) == strComment[:20]
