from ..models import Post


class PostRepository:
    # Fetch all posts from the database
    @staticmethod
    def get_all_posts():
        return Post.objects.all()

    # Fetch a specific post by its primary key (ID)
    @staticmethod
    def get_post_by_id(post_id):
        try:
            return Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return None

    # Create a new post with the provided data
    @staticmethod
    def create_post(data):
        return Post.objects.create(**data)

    # Update an existing post with the provided data
    @staticmethod
    def update_post(data, post_id):
        post = Post.objects.get(pk=post_id)
        for attr, value in data.items():
            setattr(post, attr, value)  # Dynamically update each attribute
        post.save()
        return post

    # Delete a post by its primary key (ID)
    @staticmethod
    def delete_post(post_id):
        post = Post.objects.get(pk=post_id)
        post.delete()
