from django.urls import path

from .frontend_views import (
    add_favorite,
    remove_favorite,
)


urlpatterns = [
    path(
        "add/<str:recipe_id>/",
        add_favorite,
        name="add-favorite"
    ),

    path(
        "remove/<str:recipe_id>/",
        remove_favorite,
        name="remove-favorite"
    ),
]