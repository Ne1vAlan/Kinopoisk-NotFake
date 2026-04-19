from django.urls import path

# -------- Alans --------
from .views import RegisterView, TestAuthView

# -------- Yegors --------
from .views import MovieListCreateView, MovieDetailView

# -------- Yerdaulet --------
from .views import GenreListView, ReviewListView, ReviewCreateView

urlpatterns = [
    # Alans
    path('register/', RegisterView.as_view()),

    # Movies
    path('movies/', MovieListCreateView.as_view()),
    path('movies/<int:pk>/', MovieDetailView.as_view()),

    # Genres & Reviews
    path('genres/', GenreListView.as_view()),
    path('reviews/', ReviewListView.as_view()),
    path('reviews/create/', ReviewCreateView.as_view()),
]