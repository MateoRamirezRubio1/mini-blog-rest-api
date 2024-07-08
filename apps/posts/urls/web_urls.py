from django.urls import path
from ..views.web_views import PostListView, PostDetailView
from ...comments.views.web_views import CommentListView, CommentDetailView

urlpatterns = [
    # Route for listing all posts.
    # The URL is "web/posts/", and it maps to PostListView to display a list of all posts.
    path("", PostListView.as_view(), name="post-list"),
    # Route for displaying details of a specific post identified by post_id.
    # The URL is "web/posts/<post_id>/", and it maps to PostDetailView to display details of a single post.
    path("<int:post_id>/", PostDetailView.as_view(), name="post-detail"),
    # Route for listing all comments for a specific post identified by post_id.
    # The URL is "web/posts/<post_id>/comments", and it maps to CommentListView to display a list of comments for the given post.
    path(
        "<int:post_id>/comments",
        CommentListView.as_view(),
        name="post-comments",
    ),
    # Route for displaying details of a specific comment identified by comment_id for a specific post.
    # The URL is "web/posts/<post_id>/comments/<comment_id>/", and it maps to CommentDetailView to display details of a single comment.
    path(
        "<int:post_id>/comments/<int:comment_id>/",
        CommentDetailView.as_view(),
        name="post-comment-detail",
    ),
]
