"""Serializers for Recipe APIs."""
from core.models import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipes."""

    class Meta:
        """Meta attrs for RecipeSerializer."""

        model = Recipe
        fields = ["id", "title", "time_minutes", "price", "link"]
        read_only_fields = ["id"]


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        """Meta attrs for RecipeDetailSerializer."""

        fields = RecipeSerializer.Meta.fields + ["description"]
