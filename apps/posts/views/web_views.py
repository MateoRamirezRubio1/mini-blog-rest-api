from django.views.generic import ListView, DetailView
from django.http import Http404
from ..models import Post
from ..services.post_service import PostService
from django.core.exceptions import ValidationError

class PostListView(ListView):
    """
    Class-based view for listing all posts in the web interface.
    Utilizes Django's ListView to handle displaying a list of posts.
    """
    model = Post  # Specifies the model to be used in the view.
    template_name = "posts/post_list.html"  # Path to the template for rendering the list of posts.
    context_object_name = "posts"  # Context variable name to be used in the template.

    def get_queryset(self):
        """
        Overrides the default get_queryset method to fetch all posts from the service layer.
        
        :return: QuerySet of all Post objects.
        """
        return PostService.get_all_posts()  # Delegates the database query to the PostService.


class PostDetailView(DetailView):
    """
    Class-based view for displaying the details of a single post.
    Utilizes Django's DetailView to handle displaying detailed information of a single post.
    """
    model = Post
    template_name = "posts/post_detail.html"  # Path to the template for rendering post details.
    context_object_name = "post"  # Context variable name to be used in the template.

    def get_object(self, queryset=None):
        """
        Overrides the default get_object method to fetch a specific post based on post_id.

        :param queryset: Optional queryset to filter the object (default is None).
        :return: Post object if found.
        :raises Http404: If the post does not exist.
        """
        post_id = self.kwargs.get("post_id")  # Extract post_id from the URL kwargs.
        if not post_id:
            raise Http404("Post ID not provided.")
        
        try:
            post = PostService.get_post_by_id(post_id)  # Fetches the post using the PostService.
            if post is None:
                raise Http404("Post not found.")
            return post
        except ValidationError as e:
            raise Http404(f"Invalid request: {str(e)}")
