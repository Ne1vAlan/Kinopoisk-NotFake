from django.urls import path
#Alans
from .views import TestAuthView

urlpatterns = [
    path('test/', TestAuthView.as_view()),
]

from .views import RegisterView

urlpatterns = [
    path('test/', TestAuthView.as_view()),
    path('register/', RegisterView.as_view()),
]

#Yegors
from .views import MovieListCreateView, MovieDetailView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
]