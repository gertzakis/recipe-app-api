"""Core config for user app."""
from django.apps import AppConfig


class UserConfig(AppConfig):
    """Django app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "user"
