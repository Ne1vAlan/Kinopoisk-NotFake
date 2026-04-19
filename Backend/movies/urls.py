from django.urls import path

#Alans
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]

#Yegors
from .views import MovieListCreateView, MovieDetailView

urlpatterns += [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
]

#Yerdaulet's part
from .views import GenreListView, ReviewListView, ReviewCreateView

urlpatterns += [
    path('genres/', GenreListView.as_view(), name='genre-list'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),
]