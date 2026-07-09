from django.urls import path

from .views import (
    RecipeListView,
    RecipeDetailView,
    RecipeSearchView,
    CategoryFilterView,
)


urlpatterns = [
    path("", RecipeListView.as_view(), name="recipe-list"),

    path("search/", RecipeSearchView.as_view(), name="recipe-search"),

    path(
        "filter/category/",
        CategoryFilterView.as_view(),
        name="category-filter"
    ),


    path(
        "<str:recipe_id>/",
        RecipeDetailView.as_view(),
        name="recipe-detail"
    ),
]