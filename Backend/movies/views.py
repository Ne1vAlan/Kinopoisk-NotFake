from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Genre, Movie, Review
from .serializers import (
    GenreModelSerializer,
    MovieModelSerializer,
    ReviewModelSerializer,
    RegisterSerializer,
    ReviewCreateSerializer,
)


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    'message': 'User created successfully',
                    'token': token.key,
                    'username': user.username,
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return Response(
                {'error': 'Invalid username or password'},
                status=status.HTTP_400_BAD_REQUEST
            )

        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                'message': 'Login successful',
                'token': token.key,
                'username': user.username,
            },
            status=status.HTTP_200_OK
        )


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)


# -------- Erda's part --------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_genres(request):
    genres = Genre.objects.all().order_by('name')
    serializer = GenreModelSerializer(genres, many=True)
    return Response(serializer.data)


class MoviesListCreateAPIView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]

    def get(self, request):
        movies = Movie.objects.select_related('genre').all().order_by('id')
        serializer = MovieModelSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieModelSerializer(data=request.data)
        if serializer.is_valid():
            movie = serializer.save()
            return Response(MovieModelSerializer(movie).data, status=201)
        return Response(serializer.errors, status=400)


class MovieDetailAPIView(APIView):
    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_object(self, movie_id):
        try:
            return Movie.objects.select_related('genre').get(id=movie_id)
        except Movie.DoesNotExist:
            return None

    def get(self, request, movie_id):
        movie = self.get_object(movie_id)
        if not movie:
            return Response({'error': 'Movie not found'}, status=404)
        return Response(MovieModelSerializer(movie).data)

    def put(self, request, movie_id):
        movie = self.get_object(movie_id)
        if not movie:
            return Response({'error': 'Movie not found'}, status=404)

        serializer = MovieModelSerializer(movie, data=request.data)
        if serializer.is_valid():
            updated_movie = serializer.save()
            return Response(MovieModelSerializer(updated_movie).data)
        return Response(serializer.errors, status=400)

    def delete(self, request, movie_id):
        movie = self.get_object(movie_id)
        if not movie:
            return Response({'error': 'Movie not found'}, status=404)

        movie.delete()
        return Response({'message': 'Movie deleted successfully'}, status=200)


# -------- Erda's part --------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_reviews(request):
    movie_id = request.GET.get('movie_id')

    if not movie_id:
        return Response({'error': 'movie_id is required'}, status=400)

    reviews = Review.objects.filter(movie_id=movie_id).select_related('user')
    serializer = ReviewModelSerializer(reviews, many=True)
    return Response(serializer.data)


# -------- Erda's part --------
class CreateReviewAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ReviewCreateSerializer(
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            review = serializer.save()
            return Response(ReviewModelSerializer(review).data, status=201)

        return Response(serializer.errors, status=400)