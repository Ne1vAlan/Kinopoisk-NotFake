from django.urls import path
from .views import (
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView,
    get_genres,
    get_reviews,
    MoviesListCreateAPIView,
    MovieDetailAPIView,
    CreateReviewAPIView,
)

urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),

    path('genres', get_genres),

    path('movies', MoviesListCreateAPIView.as_view()),
    path('movies/<int:movie_id>', MovieDetailAPIView.as_view()),

    path('reviews', get_reviews),
    path('reviews/create', CreateReviewAPIView.as_view()),
]