"""Core config for recipe app."""
from django.apps import AppConfig


class RecipeConfig(AppConfig):
    """Django app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "recipe"
