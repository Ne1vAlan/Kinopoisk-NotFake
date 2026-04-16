from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Genre, Movie, Review


class GenreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class ReviewModelSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'text', 'rating', 'movie', 'user', 'created_at']


class MovieModelSerializer(serializers.ModelSerializer):
    genre = GenreModelSerializer(read_only=True)
    genre_id = serializers.IntegerField(write_only=True)
    reviews = ReviewModelSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'year', 'genre', 'genre_id', 'reviews']

    def validate_genre_id(self, value):
        if not Genre.objects.filter(id=value).exists():
            raise serializers.ValidationError('Genre not found')
        return value

    def create(self, validated_data):
        genre_id = validated_data.pop('genre_id')
        genre = Genre.objects.get(id=genre_id)
        return Movie.objects.create(genre=genre, **validated_data)

    def update(self, instance, validated_data):
        genre_id = validated_data.pop('genre_id', None)

        if genre_id is not None:
            genre = Genre.objects.filter(id=genre_id).first()
            if not genre:
                raise serializers.ValidationError({'genre_id': 'Genre not found'})
            instance.genre = genre

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=4)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username already exists')
        return value

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )


class ReviewCreateSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    text = serializers.CharField()
    rating = serializers.IntegerField(min_value=1, max_value=10)

    def validate_movie_id(self, value):
        if not Movie.objects.filter(id=value).exists():
            raise serializers.ValidationError('Movie not found')
        return value

    def create(self, validated_data):
        request = self.context['request']
        movie = Movie.objects.get(id=validated_data['movie_id'])

        return Review.objects.create(
            movie=movie,
            user=request.user,
            text=validated_data['text'],
            rating=validated_data['rating']
        )