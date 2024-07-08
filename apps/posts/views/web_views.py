from django.views.generic import ListView, DetailView
from ..models import Post
from ..services.post_service import PostService


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return PostService.get_all_posts()


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        post_id = self.kwargs.get("post_id")
        return PostService.get_post_by_id(post_id)
