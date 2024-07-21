from rest_framework import generics
from ..serializers import CommentSerializer
from ..services.comment_service import CommentService
from rest_framework.exceptions import NotFound


class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # Retrieve the 'post_id' from the URL kwargs. This ID is used to filter comments related to a specific post.
        post_id = self.kwargs.get("post_id")
        # Fetch comments related to the given post ID using the CommentService. The repository layer handles actual data fetching.
        return CommentService.get_comments_by_post_id(post_id)

    def perform_create(self, serializer):
        # Retrieve the 'post_id' from the URL kwargs. This ID is used to associate the new comment with a specific post.
        post_id = self.kwargs.get("post_id")
        # Create a new comment for the specified post using the CommentService. The service layer handles data manipulation.
        CommentService.create_comment(serializer.validated_data, post_id)


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer

    def get_object(self):
        # Retrieve the 'post_id' and 'comment_pk' from the URL kwargs.
        # 'post_id' is used to ensure the comment belongs to the post, while 'comment_pk' identifies the specific comment.
        post_id = self.kwargs.get("post_id")
        comment_id = self.kwargs.get("comment_pk")
        # Fetch the specific comment for the given post ID and comment ID using the CommentService.
        # Raise a 404 error if the comment is not found.
        comment = CommentService.get_comment_by_post_and_id(post_id, comment_id)
        if comment is None:
            raise NotFound("Comment not found")
        return comment

    def perform_update(self, serializer):
        # Retrieve the 'comment_pk' from the URL kwargs for updating the specific comment.
        comment_id = self.kwargs["comment_pk"]
        # Update the specified comment using the CommentService. The service layer handles data manipulation.
        CommentService.update_comment(serializer.validated_data, comment_id)

    def perform_destroy(self, instance):
        # Retrieve the 'comment_pk' from the URL kwargs for deleting the specific comment.
        comment_id = self.kwargs["comment_pk"]
        # Delete the specified comment using the CommentService. The service layer handles data manipulation.
        CommentService.delete_comment(comment_id)
