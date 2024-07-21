from rest_framework import generics
from ..serializers import PostSerializer
from ..services.post_service import PostService
from rest_framework.exceptions import NotFound, ValidationError
from django.core.exceptions import ObjectDoesNotExist


class PostListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing all posts and creating a new post.
    Utilizes Django REST Framework's ListCreateAPIView for listing and creating resources.
    """
    serializer_class = PostSerializer  # Defines the serializer class used for converting model instances to JSON and vice versa.

    def get_queryset(self):
        """
        Fetch all posts from the database.
        `get_queryset` method specifies the queryset for listing posts.

        :return: QuerySet of all Post objects.
        """
        return PostService.get_all_posts()  # Delegates the database query to the PostService layer.

    def perform_create(self, serializer):
        """
        Handle the creation of a new post.
        `perform_create` is called after validation of the serializer.

        :param serializer: Validated serializer containing data for creating a new post.
        :raises ValidationError: If the creation of the post fails.
        """
        try:
            PostService.create_post(serializer.validated_data)  # Use PostService to handle creation logic.
        except ValidationError as e:
            raise ValidationError({"detail": str(e)})


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific post.
    Extends RetrieveUpdateDestroyAPIView for detailed operations on a single resource.
    """
    serializer_class = PostSerializer  # Specifies the serializer class for retrieving, updating, and deleting resources.

    def get_object(self):
        """
        Retrieve a post object based on the provided post_id.
        `get_object` method returns the post instance for the specified post_id.

        :return: Post object if found.
        :raises NotFound: If the post does not exist.
        """
        post_id = self.kwargs.get("post_id")  # Extract post_id from the URL kwargs.
        try:
            post = PostService.get_post_by_id(post_id)  # Fetch the post using PostService.
            return post
        except ObjectDoesNotExist:
            raise NotFound("Post not found")  # Raise a 404 error if the post does not exist.
        except ValidationError as e:
            raise NotFound({"detail": str(e)})

    def perform_update(self, serializer):
        """
        Update an existing post instance.
        `perform_update` is called after the serializer's data is validated.

        :param serializer: Validated serializer containing data for updating the post.
        :raises ValidationError: If the update fails.
        """
        post_id = self.kwargs["post_id"]  # Extract post_id from the URL kwargs.
        try:
            PostService.update_post(serializer.validated_data, post_id)  # Delegate the update logic to PostService.
        except ObjectDoesNotExist:
            raise NotFound("Post not found")
        except ValidationError as e:
            raise ValidationError({"detail": str(e)})

    def perform_destroy(self, instance):
        """
        Delete a post instance.
        `perform_destroy` is called to delete the specified post.

        :param instance: The post instance to delete.
        :raises NotFound: If the post does not exist.
        """
        post_id = self.kwargs["post_id"]  # Extract post_id from the URL kwargs.
        try:
            PostService.delete_post(post_id)  # Delegate the deletion logic to PostService.
        except ObjectDoesNotExist:
            raise NotFound("Post not found")
        except ValidationError as e:
            raise ValidationError({"detail": str(e)})
