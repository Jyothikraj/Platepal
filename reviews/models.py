from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    recipe_id = models.CharField(max_length=50)

    rating = models.PositiveSmallIntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "recipe_id"],
                name="unique_user_review"
            )
        ]