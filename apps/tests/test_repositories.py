import pytest
from apps.comments.repositories.comment_repository import CommentRepository


@pytest.mark.django_db
def test_get_comment_by_id_exists(comment):
    """
    Verify that a Comment can be retrieved by its ID when it exists in the database.

    Args:
        comment: The Comment fixture providing a Comment object.

    Asserts:
        The result should be equal to the provided Comment object.
    """
    result = CommentRepository.get_comment_by_post_and_id(comment.post.id, comment.id)
    assert result == comment


@pytest.mark.django_db
def test_get_comment_by_id_does_not_exist():
    """
    Verify that attempting to retrieve a Comment by ID when it does not exist returns None.

    Asserts:
        The result should be None.
    """
    result = CommentRepository.get_comment_by_post_and_id(232, 9999)  # Non-existent ID
    assert result is None
