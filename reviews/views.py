from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Review
from .serializers import ReviewSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        recipe_id = self.request.query_params.get("recipe_id")

        queryset = Review.objects.all()

        if recipe_id:
            queryset = queryset.filter(recipe_id=recipe_id)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
    
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .forms import ReviewForm


@login_required
def add_review(request, recipe_id):

    if request.method == "POST":

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.user = request.user
            review.recipe_id = recipe_id

            review.save()

    return redirect(
        "recipe-detail",
        recipe_id=recipe_id
    )