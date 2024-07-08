from django.views.generic import ListView, DetailView
from ..models import Comment
from ..services.comment_service import CommentService


class CommentListView(ListView):
    model = Comment
    template_name = "comments/comment_list.html"
    context_object_name = "comments"

    def get_queryset(self):
        # Extract 'post_id' from URL parameters to fetch comments associated with a specific post.
        post_id = self.kwargs.get("post_id")
        # Use the CommentService to retrieve comments for the specified post.
        # The service layer handles data access logic, keeping the view simple.
        return CommentService.get_comments_by_post_id(post_id)

    def get_context_data(self, **kwargs):
        # Get the default context from the parent class and add additional context for 'post_id'.
        context = super().get_context_data(**kwargs)
        # Include 'post_id' in the context so it can be used in the template.
        # This is necessary for rendering links or forms related to the post.
        context["post_id"] = self.kwargs.get("post_id")
        return context


class CommentDetailView(DetailView):
    model = Comment
    template_name = "comments/comment_detail.html"
    context_object_name = "comment"

    def get_object(self, queryset=None):
        # Extract 'post_id' and 'comment_id' from URL parameters to retrieve a specific comment for a post.
        post_id = self.kwargs.get("post_id")
        comment_id = self.kwargs.get("comment_id")
        # Use the CommentService to retrieve the specific comment based on 'post_id' and 'comment_id'.
        # If the comment is not found, `CommentService.get_comment_by_post_and_id` will return None.
        # In this case, a 404 error will be raised automatically by the `DetailView` if the object is not found.
        return CommentService.get_comment_by_post_and_id(post_id, comment_id)
