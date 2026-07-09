from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Favorite


def add_favorite(request, recipe_id):

    if request.method == "POST":

        Favorite.objects.get_or_create(
            user=request.user,
            recipe_id=recipe_id
        )

    return redirect(
        "recipe-detail",
        recipe_id=recipe_id
    )
def remove_favorite(request, recipe_id):

    Favorite.objects.filter(
        user=request.user,
        recipe_id=recipe_id
    ).delete()

    return redirect("favorites")