from django.views.generic import ListView, DetailView
from ..models import Post
from ..services.post_service import PostService


# Class-based view for listing all posts in the web interface.
# Utilizes Django's ListView to handle displaying a list of posts.
class PostListView(ListView):
    model = Post  # Specifies the model to be used in the view.
    template_name = (
        "posts/post_list.html"  # Path to the template for rendering the list of posts.
    )
    context_object_name = "posts"  # Context variable name to be used in the template.

    # Overrides the default get_queryset method to fetch all posts from the service layer.
    def get_queryset(self):
        return (
            PostService.get_all_posts()
        )  # Delegates the database query to the PostService.


# Class-based view for displaying the details of a single post.
# Utilizes Django's DetailView to handle displaying detailed information of a single post.
class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    # Overrides the default get_object method to fetch a specific post based on post_id.
    def get_object(self, queryset=None):
        post_id = self.kwargs.get("post_id")  # Extracts post_id from the URL kwargs.
        return PostService.get_post_by_id(
            post_id
        )  # Fetches the post using the PostService.
