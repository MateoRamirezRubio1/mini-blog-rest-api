from ..repositories.comment_repository import CommentRepository


class CommentService:
    @staticmethod
    def get_comments_by_post_id(post_id):
        # Delegate the task of retrieving comments by post_id to the repository layer
        return CommentRepository.get_comments_by_post_id(post_id)

    @staticmethod
    def get_comment_by_post_and_id(post_id, comment_id):
        # Delegate the task of retrieving a specific comment by post_id and comment_id to the repository layer
        return CommentRepository.get_comment_by_post_and_id(post_id, comment_id)

    @staticmethod
    def create_comment(data, post_id):
        # Delegate the task of creating a new comment to the repository layer
        return CommentRepository.create_comment(data, post_id)

    @staticmethod
    def update_comment(data, comment_id):
        # Delegate the task of updating an existing comment to the repository layer
        return CommentRepository.update_comment(data, comment_id)

    @staticmethod
    def delete_comment(comment_id):
        # Delegate the task of deleting a comment to the repository layer
        return CommentRepository.delete_comment(comment_id)
