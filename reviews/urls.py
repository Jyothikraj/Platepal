from django.urls import path
from .views import ReviewListCreateView, ReviewUpdateDeleteView, add_review


urlpatterns = [
    path(
        "",
        ReviewListCreateView.as_view(),
        name="review-list-create"
    ),

    path(
        "<int:pk>/",
        ReviewUpdateDeleteView.as_view(),
        name="review-update-delete"
    ),
    path(
        "add/<str:recipe_id>/",
        add_review,
        name="add-review"
    ),
]