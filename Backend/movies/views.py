#Alans
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import RegisterSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username, 'message': 'User created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Неверный логин или пароль'}, status=400)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username, 'message': 'Login successful'})

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response({'message': 'Logout successful'})

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
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreModelSerializer
    permission_classes = [AllowAny]

class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewModelSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id')
        if movie_id:
            return Review.objects.filter(movie_id=movie_id).select_related('user')
        return Review.objects.none()

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
