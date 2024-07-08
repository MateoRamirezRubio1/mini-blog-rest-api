from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    # This configuration specifies that this app is located at 'apps.posts'.
    name = "apps.posts"
