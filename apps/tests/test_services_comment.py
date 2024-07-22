import pytest
from django.db import DatabaseError
from apps.comments.services.comment_service import CommentService
from django.core.exceptions import ObjectDoesNotExist

def test_database_error_service_get_comments_by_post_id(mocker):
    mocker.patch('apps.comments.services.comment_service.CommentRepository.get_comments_by_post_id', side_effect=DatabaseError)

    with pytest.raises(DatabaseError):
        CommentService.get_comments_by_post_id(-1)

def test_database_error_service_get_comment_by_post_and_id(mocker):
    mocker.patch('apps.comments.services.comment_service.CommentRepository.get_comment_by_post_and_id', side_effect=DatabaseError)

    with pytest.raises(DatabaseError):
        CommentService.get_comment_by_post_and_id(-1, -2)

def test_database_error_service_create_comment(mocker):
    mocker.patch('apps.comments.services.comment_service.CommentRepository.create_comment', side_effect=DatabaseError)

    with pytest.raises(DatabaseError):
        CommentService.create_comment({}, -2)

def test_database_error_service_update_comment(mocker):
    mocker.patch('apps.comments.services.comment_service.CommentRepository.update_comment', side_effect=DatabaseError)

    with pytest.raises(DatabaseError):
        CommentService.update_comment({}, -2)

def test_database_error_service_delete_comment(mocker):
    mocker.patch('apps.comments.services.comment_service.CommentRepository.delete_comment', side_effect=DatabaseError)

    with pytest.raises(DatabaseError):
        CommentService.delete_comment(-2)

@pytest.mark.django_db
def test_service_update_comment_is_does_not_exist():
    try:
        result = CommentService.update_comment({}, -1) # Non-existent ID
    except ObjectDoesNotExist:
        pass
    else:
        pytest.fail("ObjectDoesNotExist was not raised")

@pytest.mark.django_db
def test_service_delete_comment_is_does_not_exist():
    try:
        result = CommentService.delete_comment(-1) # Non-existent ID
    except ObjectDoesNotExist:
        pass
    else:
        pytest.fail("ObjectDoesNotExist was not raised")