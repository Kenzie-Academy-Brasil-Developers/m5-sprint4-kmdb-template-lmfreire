from django.urls import path
from . import views

urlpatterns = [
    path("movies/<int:movie_id>/reviews/", views.CreateReviewsReview.as_view()),
    path("movies/<int:movie_id>/reviews/<int:review_id>/", views.ReviewMovieDetailReview.as_view()),
]
