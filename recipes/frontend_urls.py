from django.urls import path
from .views import home, recipe_detail_page, search_page, favorites_page

urlpatterns = [
    path("", home, name="home"),

    path(
        "search/",
        search_page,
        name="search-page"
    ),

    path(
        "recipe/<str:recipe_id>/",
        recipe_detail_page,
        name="recipe-detail"
    ),
    path("favorites/", favorites_page, name="favorites"),
]