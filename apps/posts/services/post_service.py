from ..repositories.post_repository import PostRepository


class PostService:
    @staticmethod
    def get_all_posts():
        # Retrieve all posts from the repository
        return PostRepository.get_all_posts()

    @staticmethod
    def get_post_by_id(post_id):
        # Retrieve a post by its ID from the repository
        return PostRepository.get_post_by_id(post_id)

    @staticmethod
    def create_post(data):
        # Create a new post with the given data
        return PostRepository.create_post(data)

    @staticmethod
    def update_post(data, post_id):
        # Update an existing post with the given data
        return PostRepository.update_post(data, post_id)

    @staticmethod
    def delete_post(post_id):
        # Delete a post by its ID from the repository
        return PostRepository.delete_post(post_id)
