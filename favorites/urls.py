from django.urls import path
from .views import FavoriteListCreateView, FavoriteDeleteView

urlpatterns = [
    path(
        "",
        FavoriteListCreateView.as_view(),
        name="favorite-list-create"
    ),

    path(
        "<str:recipe_id>/",
        FavoriteDeleteView.as_view(),
        name="favorite-delete"
    ),
]