from django.urls import path
from ..views.api_views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView
from ...comments.views.api_views import (
    CommentListCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # Route for listing all posts or creating a new post
    path("", PostListCreateAPIView.as_view(), name="post-list-create"),
    # Route for retrieving, updating, or deleting a specific post by post_id
    path(
        "<int:post_id>/",
        PostRetrieveUpdateDestroyAPIView.as_view(),
        name="post-retrieve-update-destroy",
    ),
    # Route for listing all comments for a specific post or creating a new comment for that post
    path(
        "<int:post_id>/comments/",
        CommentListCreateAPIView.as_view(),
        name="post-comment-create",
    ),
    # Route for retrieving, updating, or deleting a specific comment by comment_pk for a specific post
    path(
        "<int:post_id>/comments/<int:comment_pk>/",
        CommentRetrieveUpdateDestroyAPIView.as_view(),
        name="post-comment-retrieve-update-destroy",
    ),
]
