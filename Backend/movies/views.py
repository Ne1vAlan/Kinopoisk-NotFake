#Alans
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class TestAuthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authorized"})
    

from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

#Yegors
#from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


#Yerdaulet's part
from .models import Genre, Review
from .serializers import GenreModelSerializer, ReviewModelSerializer, ReviewCreateSerializer

class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer

class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewModelSerializer

    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id')
        return Review.objects.filter(movie_id=movie_id)

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]
