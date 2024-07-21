from ..repositories.post_repository import PostRepository
from django.core.exceptions import ValidationError, ObjectDoesNotExist

class PostService:
    """
    Service class for handling business logic related to the Post model.
    """

    @staticmethod
    def get_all_posts():
        """
        Retrieve all posts from the repository.

        :return: QuerySet of all Post objects.
        """
        return PostRepository.get_all_posts()

    @staticmethod
    def get_post_by_id(post_id):
        """
        Retrieve a post by its ID from the repository.

        :param post_id: Primary key of the post to fetch.
        :return: Post object if found, None otherwise.
        :raises: ValidationError if 'post_id' is not provided.
        :raises: ObjectDoesNotExist if the post does not exist.
        """
        if not post_id:
            raise ValidationError("Post ID is required to fetch the post.")
        post = PostRepository.get_post_by_id(post_id)
        if post is None:
            raise ObjectDoesNotExist(f"Post with ID {post_id} does not exist.")
        return post

    @staticmethod
    def create_post(data):
        """
        Create a new post with the given data.

        :param data: Dictionary of data to create the post.
        :return: Newly created Post object.
        :raises: ValidationError if required data fields are missing.
        """
        # Example validation: Ensure title and content are provided
        if not data.get("title") or not data.get("content"):
            raise ValidationError("Title and content are required to create a post.")
        return PostRepository.create_post(data)

    @staticmethod
    def update_post(data, post_id):
        """
        Update an existing post with the given data.

        :param data: Dictionary of data to update the post.
        :param post_id: Primary key of the post to update.
        :return: Updated Post object.
        :raises: ValidationError if 'post_id' is not provided.
        :raises: ObjectDoesNotExist if the post does not exist.
        """
        if not post_id:
            raise ValidationError("Post ID is required to update the post.")
        if not data:
            raise ValidationError("Data is required to update the post.")
        return PostRepository.update_post(data, post_id)

    @staticmethod
    def delete_post(post_id):
        """
        Delete a post by its ID from the repository.

        :param post_id: Primary key of the post to delete.
        :raises: ValidationError if 'post_id' is not provided.
        :raises: ObjectDoesNotExist if the post does not exist.
        """
        if not post_id:
            raise ValidationError("Post ID is required to delete the post.")
        return PostRepository.delete_post(post_id)
