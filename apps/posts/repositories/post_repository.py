from ..models import Post
from django.core.exceptions import ObjectDoesNotExist, ValidationError


class PostRepository:
    """
    Repository class for handling data operations related to the Post model.
    """

    @staticmethod
    def get_all_posts():
        """
        Fetch all posts from the database.

        :return: QuerySet of all Post objects.
        """
        return Post.objects.all()

    @staticmethod
    def get_post_by_id(post_id):
        """
        Fetch a specific post by its primary key (ID).

        :param post_id: Primary key of the post to fetch.
        :return: Post object if found, None otherwise.
        :raises: ValidationError if 'post_id' is not provided.
        """
        if not post_id:
            raise ValidationError("Post ID is required to fetch the post.")
        try:
            return Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return None

    @staticmethod
    def create_post(data):
        """
        Create a new post with the provided data.

        :param data: Dictionary of data to create the post.
        :return: Newly created Post object.
        """
        return Post.objects.create(**data)

    @staticmethod
    def update_post(data, post_id):
        """
        Update an existing post with the provided data.

        :param data: Dictionary of data to update the post.
        :param post_id: Primary key of the post to update.
        :return: Updated Post object.
        :raises: ValidationError if 'post_id' is not provided.
        :raises: ObjectDoesNotExist if the post is not found.
        """
        if not post_id:
            raise ValidationError("Post ID is required to update the post.")
        try:
            post = Post.objects.get(pk=post_id)
            for attr, value in data.items():
                setattr(post, attr, value)  # Dynamically update each attribute
            post.save()
            return post
        except Post.DoesNotExist:
            raise ObjectDoesNotExist(f"Post with ID {post_id} does not exist.")

    @staticmethod
    def delete_post(post_id):
        """
        Delete a post by its primary key (ID).

        :param post_id: Primary key of the post to delete.
        :raises: ValidationError if 'post_id' is not provided.
        :raises: ObjectDoesNotExist if the post is not found.
        """
        if not post_id:
            raise ValidationError("Post ID is required to delete the post.")
        try:
            post = Post.objects.get(pk=post_id)
            post.delete()
        except Post.DoesNotExist:
            raise ObjectDoesNotExist(f"Post with ID {post_id} does not exist.")
