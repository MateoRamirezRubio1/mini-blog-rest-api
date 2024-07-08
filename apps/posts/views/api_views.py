from rest_framework import generics
from ..serializers import PostSerializer
from ..services.post_service import PostService


class PostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return PostService.get_all_posts()

    def perform_create(self, serializer):
        PostService.create_post(serializer.validated_data)


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_object(self):
        post_id = self.kwargs.get("post_id")
        post = PostService.get_post_by_id(post_id)
        if post is None:
            raise NotFound("Comment not fund")
        return post

    def perform_update(self, serializer):
        post_id = self.kwargs["post_id"]
        PostService.update_post(serializer.validated_data, post_id)

    def perform_destroy(self, instance):
        post_id = self.kwargs["post_id"]
        PostService.delete_post(post_id)
