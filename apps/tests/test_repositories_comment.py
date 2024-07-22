import pytest
from django.db import DatabaseError
from apps.comments.repositories.comment_repository import CommentRepository



def test_repository_get_comment_by_id_exists(comment):
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
def test_repository_get_comment_by_id_is_does_not_exist():
    """
    Verify that attempting to retrieve a Comment by ID when it does not exist returns None.

    Asserts:
        The result should be None.
    """
    result = CommentRepository.get_comment_by_post_and_id(232, 9999)  # Non-existent ID
    assert result is None

@pytest.mark.django_db
def test_repository_update_comment_is_does_not_exist():
    result = CommentRepository.update_comment({}, -1)
    assert result is None

@pytest.mark.django_db
def test_repository_delete_comment_is_does_not_exist():
    result = CommentRepository.delete_comment(-1)
    assert result is False


def test_database_error_repository_get_comments_by_post_id(mocker):
    """
    Test that the CommentRepository raises a DatabaseError when a database error occurs.
    
    Args:
        mocker: The pytest-mock fixture for mocking.
    
    Asserts:
        The method should raise a DatabaseError.
    """
    # Mock Comment.objects.filter to raise a DatabaseError
    mocker.patch('apps.comments.repositories.comment_repository.Comment.objects.filter', side_effect=DatabaseError)

    # Call the method and assert it raises a DatabaseError
    with pytest.raises(DatabaseError):
        CommentRepository.get_comments_by_post_id(1)


@pytest.mark.django_db
def test_database_error_repository_get_comment_by_post_and_id(mocker):
    mocker.patch('apps.comments.repositories.comment_repository.Comment.objects.get', side_effect=DatabaseError)

    with pytest.raises(DatabaseError):
        CommentRepository.get_comment_by_post_and_id(3, -1)
    

def test_database_error_repository_create_comment(mocker):
    mocker.patch('apps.comments.repositories.comment_repository.Comment.objects.create', side_effect=DatabaseError)

    with pytest.raises(DatabaseError):
        CommentRepository.create_comment({}, 1)

def test_database_error_repository_update_comment(mocker):
    mocker.patch('apps.comments.repositories.comment_repository.Comment.objects.get', side_effect=DatabaseError)

    with pytest.raises(DatabaseError):
        CommentRepository.update_comment({}, -1)

@pytest.mark.django_db
def test_database_error_repository_delete_comment(mocker):
    mocker.patch('apps.comments.repositories.comment_repository.Comment.objects.get', side_effect=DatabaseError)

    with pytest.raises(DatabaseError):
        CommentRepository.delete_comment(-1)
