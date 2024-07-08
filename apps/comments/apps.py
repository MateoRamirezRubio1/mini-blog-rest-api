from django.apps import AppConfig


class CommentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    # This configuration specifies that this app is located at 'apps.comments'.
    name = "apps.comments"
