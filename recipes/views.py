from rest_framework.response import Response
from rest_framework.views import APIView
from reviews.models import Review
from reviews.forms import ReviewForm
from .services import (
    get_popular_recipes,
    get_recipe,
    search_recipes,
    filter_by_category,
)


class RecipeListView(APIView):

    def get(self, request):
        recipes = get_popular_recipes()
        return Response(recipes)


class RecipeDetailView(APIView):

    def get(self, request, recipe_id):
        recipe = get_recipe(recipe_id)
        return Response(recipe)


class RecipeSearchView(APIView):

    def get(self, request):
        query = request.GET.get("q", "").strip()

        if not query:
            return Response(
                {"error": "Search query is required"},
                status=400
            )

        recipes = search_recipes(query)

        return Response(recipes)


class CategoryFilterView(APIView):

    def get(self, request):
        category = request.GET.get("category", "").strip()

        if not category:
            return Response(
                {"error": "Category is required"},
                status=400
            )

        recipes = filter_by_category(category)

        return Response(recipes)
    
from django.shortcuts import render


def home(request):
    recipes = get_popular_recipes()

    return render(
        request,
        "recipes/home.html",
        {
            "recipes": recipes
        }
    )
def recipe_detail_page(request, recipe_id):

    recipe = get_recipe(recipe_id)

    ingredients = []

    for i in range(1, 21):

        ingredient = recipe.get(f"strIngredient{i}")
        measure = recipe.get(f"strMeasure{i}")

        if ingredient and ingredient.strip():

            ingredients.append({
                "ingredient": ingredient,
                "measure": measure,
            })

    reviews = Review.objects.filter(
        recipe_id=recipe_id
    ).order_by("-created_at")

    form = ReviewForm()

    return render(
        request,
        "recipes/detail.html",
        {
            "recipe": recipe,
            "ingredients": ingredients,
            "reviews": reviews,
            "form": form,
        }
    )
def search_page(request):
    query = request.GET.get("q", "").strip()

    recipes = []

    if query:
        recipes = search_recipes(query)

    return render(
        request,
        "recipes/search_results.html",
        {
            "query": query,
            "recipes": recipes.get("meals", [])
        }
    )

from favorites.models import Favorite


from django.contrib.auth.decorators import login_required
from favorites.models import Favorite
from .services import get_recipe


def favorites_page(request):

    favorites = Favorite.objects.filter(
        user=request.user
    )

    recipes = []

    for favorite in favorites:

        recipe = get_recipe(
            favorite.recipe_id
        )

        if recipe:
            recipes.append(recipe)

    return render(
        request,
        "recipes/favorites.html",
        {
            "recipes": recipes
        }
    )