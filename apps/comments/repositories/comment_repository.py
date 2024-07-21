from ..models import Comment
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import DatabaseError

class CommentRepository:
    @staticmethod
    def get_comments_by_post_id(post_id):
        """
        Retrieve all comments associated with a specific post_id.

        :param post_id: The ID of the post to retrieve comments for.
        :return: QuerySet of Comment objects.
        """
        try:
            return Comment.objects.filter(post_id=post_id)
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
        """
        try:
            return Comment.objects.get(post_id=post_id, id=comment_id)
        except Comment.DoesNotExist:
            return None
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
        """
        try:
            return Comment.objects.create(post_id=post_id, **data)
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
        """
        try:
            comment = Comment.objects.get(pk=comment_id)
            for attr, value in data.items():
                setattr(comment, attr, value)
            comment.save()
            return comment
        except Comment.DoesNotExist:
            return None
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
        """
        try:
            comment = Comment.objects.get(pk=comment_id)
            comment.delete()
            return True
        except Comment.DoesNotExist:
            return False
        except DatabaseError as e:
            # Log the exception (if logging is configured)
            # logger.error(f"Database error when deleting comment {comment_id}: {e}")
            raise e
