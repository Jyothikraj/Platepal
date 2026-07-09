from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # APIs
    path("api/favorites/", include("favorites.urls")),
    path("api/users/", include("users.urls")),
    path("api/reviews/", include("reviews.urls")),
    path("api/recipes/", include("recipes.urls")),
    path("api/login/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path(
    "favorites/",
    include("favorites.frontend_urls")
    ),
    # Authentication pages
    path("", include("users.frontend_urls")),

    # Recipe frontend pages
    path("home/", include("recipes.frontend_urls")),
]