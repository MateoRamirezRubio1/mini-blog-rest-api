from rest_framework import generics
from rest_framework.exceptions import NotFound, ValidationError, APIException
from ..serializers import CommentSerializer
from ..services.comment_service import CommentService

class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        Retrieve the 'post_id' from the URL kwargs and fetch comments related to the given post ID using the CommentService.

        :return: QuerySet of Comment objects.
        :raises: ValidationError if 'post_id' is not provided.
        """ 
        post_id = self.kwargs.get("post_id")
        if not post_id:
            raise APIException("Post ID is required to fetch comments.")
        try:
            return CommentService.get_comments_by_post_id(post_id)
        except ValueError:
            raise APIException("Invalid Post ID format.")

    def perform_create(self, serializer):
        """
        Create a new comment for the specified post using the CommentService.

        :param serializer: Serializer instance with validated data.
        :raises: ValidationError if 'post_id' is not provided.
        """
        post_id = self.kwargs.get("post_id")
        if not post_id:
            raise APIException("Post ID is required to create a comment.")
        try:
            CommentService.create_comment(serializer.validated_data, post_id)
        except ValueError:
            raise APIException("Invalid Post ID format.")

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer

    def get_object(self):
        """
        Retrieve the specific comment for the given post ID and comment ID using the CommentService.
        
        :return: Comment object.
        :raises: NotFound if the comment does not exist.
        :raises: ValidationError if 'post_id' or 'comment_pk' is not provided.
        """
        post_id = self.kwargs.get("post_id")
        comment_id = self.kwargs.get("comment_pk")
        if not post_id or not comment_id:
            raise APIException("Post ID and Comment ID are required to fetch the comment.")
        try:
            comment = CommentService.get_comment_by_post_and_id(post_id, comment_id)
            if comment is None:
                raise NotFound("Comment not found")
            return comment
        except ValueError:
            raise APIException("Invalid Post or Comment ID format.")

    def perform_update(self, serializer):
        """
        Update the specified comment using the CommentService.

        :param serializer: Serializer instance with validated data.
        :raises: ValidationError if 'comment_pk' is not provided.
        """
        comment_id = self.kwargs.get("comment_pk")
        if not comment_id:
            raise APIException("Comment ID is required to update the comment.")
        try:
            CommentService.update_comment(serializer.validated_data, comment_id)
        except ValueError:
            raise APIException("Invalid Comment ID format.")

    def perform_destroy(self, instance):
        """
        Delete the specified comment using the CommentService.

        :param instance: Comment instance to be deleted.
        :raises: ValidationError if 'comment_pk' is not provided.
        """
        comment_id = self.kwargs.get("comment_pk")
        if not comment_id:
            raise APIException("Comment ID is required to delete the comment.")
        try:
            CommentService.delete_comment(comment_id)
        except ValueError:
            raise APIException("Invalid Comment ID format.")
