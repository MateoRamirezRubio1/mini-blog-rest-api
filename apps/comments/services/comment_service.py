from ..repositories.comment_repository import CommentRepository
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import DatabaseError

class CommentService:
    @staticmethod
    def get_comments_by_post_id(post_id):
        """
        Retrieve all comments associated with a specific post_id.

        :param post_id: The ID of the post to retrieve comments for.
        :return: QuerySet of Comment objects.
        :raises: DatabaseError if there is an error accessing the database.
        """
        try:
            return CommentRepository.get_comments_by_post_id(post_id)
        except DatabaseError as e:
            # Log the exception (if logging is configured)
            # logger.error(f"Database error when retrieving comments for post_id {post_id}: {e}")
            raise e

    @staticmethod
    def get_comment_by_post_and_id(post_id, comment_id):
        """
        Retrieve a specific comment by post_id and comment_id.

        :param post_id: The ID of the post the comment is associated with.
        :param comment_id: The ID of the comment to retrieve.
        :return: Comment object if found, None otherwise.
        :raises: DatabaseError if there is an error accessing the database.
        """
        try:
            return CommentRepository.get_comment_by_post_and_id(post_id, comment_id)
        except DatabaseError as e:
            # Log the exception (if logging is configured)
            # logger.error(f"Database error when retrieving comment {comment_id} for post_id {post_id}: {e}")
            raise e

    @staticmethod
    def create_comment(data, post_id):
        """
        Create a new comment associated with a specific post_id.

        :param data: Dictionary containing the data for the new comment.
        :param post_id: The ID of the post the comment is associated with.
        :return: The newly created Comment object.
        :raises: DatabaseError if there is an error accessing the database.
        """
        try:
            return CommentRepository.create_comment(data, post_id)
        except DatabaseError as e:
            # Log the exception (if logging is configured)
            # logger.error(f"Database error when creating comment for post_id {post_id}: {e}")
            raise e

    @staticmethod
    def update_comment(data, comment_id):
        """
        Update an existing comment identified by comment_id.

        :param data: Dictionary containing the data to update the comment with.
        :param comment_id: The ID of the comment to update.
        :return: The updated Comment object.
        :raises: ObjectDoesNotExist if the comment does not exist.
        :raises: DatabaseError if there is an error accessing the database.
        """
        try:
            comment = CommentRepository.update_comment(data, comment_id)
            if comment is None:
                raise ObjectDoesNotExist(f"Comment with id {comment_id} does not exist.")
            return comment
        except ObjectDoesNotExist as e:
            # Log the exception (if logging is configured)
            # logger.warning(f"Attempted to update non-existent comment {comment_id}: {e}")
            raise e
        except DatabaseError as e:
            # Log the exception (if logging is configured)
            # logger.error(f"Database error when updating comment {comment_id}: {e}")
            raise e

    @staticmethod
    def delete_comment(comment_id):
        """
        Delete an existing comment identified by comment_id.

        :param comment_id: The ID of the comment to delete.
        :return: True if the comment was successfully deleted, False otherwise.
        :raises: DatabaseError if there is an error accessing the database.
        """
        try:
            success = CommentRepository.delete_comment(comment_id)
            if not success:
                raise ObjectDoesNotExist(f"Comment with id {comment_id} does not exist.")
            return success
        except ObjectDoesNotExist as e:
            # Log the exception (if logging is configured)
            # logger.warning(f"Attempted to delete non-existent comment {comment_id}: {e}")
            raise e
        except DatabaseError as e:
            # Log the exception (if logging is configured)
            # logger.error(f"Database error when deleting comment {comment_id}: {e}")
            raise e
