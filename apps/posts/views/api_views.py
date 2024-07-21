from rest_framework import generics
from ..serializers import PostSerializer
from ..services.post_service import PostService
from rest_framework.exceptions import NotFound


# API view for listing all posts and creating a new post.
# Utilizes Django REST Framework's ListCreateAPIView for listing and creating resources.
class PostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer  # Defines the serializer class used for converting model instances to JSON and vice versa.

    # Fetches all posts from the database.
    # `get_queryset` method specifies the queryset for listing posts.
    def get_queryset(self):
        return (
            PostService.get_all_posts()
        )  # Delegates the database query to the PostService layer.

    # Handles the creation of a new post.
    # `perform_create` is called after validation of the serializer.
    def perform_create(self, serializer):
        # Creates a new post using validated data from the serializer.
        PostService.create_post(
            serializer.validated_data
        )  # Uses PostService to handle creation logic.


# API view for retrieving, updating, and deleting a specific post.
# Extends RetrieveUpdateDestroyAPIView for detailed operations on a single resource.
class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer  # Specifies the serializer class for retrieving, updating, and deleting resources.

    # Retrieves a post object based on the provided post_id.
    # `get_object` method returns the post instance for the specified post_id.
    def get_object(self):
        post_id = self.kwargs.get("post_id")  # Extracts post_id from the URL kwargs.
        post = PostService.get_post_by_id(
            post_id
        )  # Fetches the post using PostService.
        if post is None:
            raise NotFound(
                "Post not found"
            )  # Raises a 404 error if the post does not exist.
        return post  # Returns the post instance.

    # Updates an existing post instance.
    # `perform_update` is called after the serializer's data is validated.
    def perform_update(self, serializer):
        post_id = self.kwargs["post_id"]  # Extracts post_id from the URL kwargs.
        # Updates the post with new data.
        PostService.update_post(
            serializer.validated_data, post_id
        )  # Delegates the update logic to PostService.

    # Deletes a post instance.
    # `perform_destroy` is called to delete the specified post.
    def perform_destroy(self, instance):
        post_id = self.kwargs["post_id"]  # Extracts post_id from the URL kwargs.
        # Deletes the post using PostService.
        PostService.delete_post(post_id)  # Delegates the deletion logic to PostService.
