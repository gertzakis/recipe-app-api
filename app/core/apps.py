"""Core config for core app."""
from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Django app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
