from django.views.generic import ListView, DetailView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
from ..models import Comment
from ..services.comment_service import CommentService

class CommentListView(ListView):
    model = Comment
    template_name = "comments/comment_list.html"
    context_object_name = "comments"

    def get_queryset(self):
        """
        Extract 'post_id' from URL parameters to fetch comments associated with a specific post.

        :return: QuerySet of Comment objects.
        :raises: ValidationError if 'post_id' is not provided.
        """
        post_id = self.kwargs.get("post_id")
        if not post_id:
            raise ValidationError("Post ID is required to fetch comments.")
        try:
            return CommentService.get_comments_by_post_id(post_id)
        except Exception as e:
            raise e

    def get_context_data(self, **kwargs):
        """
        Get the default context from the parent class and add additional context for 'post_id'.

        :param kwargs: Additional context parameters.
        :return: Context dictionary.
        """
        context = super().get_context_data(**kwargs)
        context["post_id"] = self.kwargs.get("post_id")
        return context

class CommentDetailView(DetailView):
    model = Comment
    template_name = "comments/comment_detail.html"
    context_object_name = "comment"

    def get_object(self, queryset=None):
        """
        Extract 'post_id' and 'comment_id' from URL parameters to retrieve a specific comment for a post.

        :return: Comment object.
        :raises: ValidationError if 'post_id' or 'comment_id' is not provided.
        :raises: ObjectDoesNotExist if the comment does not exist.
        """
        post_id = self.kwargs.get("post_id")
        comment_id = self.kwargs.get("comment_id")
        if not post_id or not comment_id:
            raise ValidationError("Post ID and Comment ID are required to fetch the comment.")
        try:
            comment = CommentService.get_comment_by_post_and_id(post_id, comment_id)
            if comment is None:
                raise ObjectDoesNotExist(f"Comment with post_id {post_id} and comment_id {comment_id} not found.")
            return comment
        except ObjectDoesNotExist as e:
            raise e
        except Exception as e:
            raise e
