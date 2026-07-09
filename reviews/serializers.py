from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            "id",
            "recipe_id",
            "rating",
            "comment",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Rating must be between 1 and 5."
            )

        return value

    def validate_recipe_id(self, value):
        user = self.context["request"].user

        if self.instance is None and Review.objects.filter(
            user=user,
            recipe_id=value
        ).exists():
            raise serializers.ValidationError(
                "You have already reviewed this recipe."
            )

        return value