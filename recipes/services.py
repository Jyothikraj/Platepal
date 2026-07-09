import requests

BASE_URL = "https://www.themealdb.com/api/json/v1/1"


def get_popular_recipes():
    response = requests.get(
        f"{BASE_URL}/search.php?s="
    )

    return response.json()["meals"]


def get_recipe(recipe_id):
    response = requests.get(
        f"{BASE_URL}/lookup.php?i={recipe_id}"
    )

    meals = response.json()["meals"]

    if meals:
        return meals[0]

    return None



def search_recipes(query):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"

    response = requests.get(url)

    return response.json()


def filter_by_category(category):
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}"

    response = requests.get(url)

    return response.json()


    