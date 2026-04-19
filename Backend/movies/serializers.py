#Alans part
from django.contrib.auth.models import User
from rest_framework import serializers

# -------- Check --------
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

#Yegors part
from .models import Movie
#from rest_framework import serializers

# -------- MOVIES --------
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


#Yerdaulet's part
from .models import Genre, Review

class GenreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class ReviewModelSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'text', 'rating', 'movie', 'user', 'created_at']

class ReviewCreateSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    text = serializers.CharField()
    rating = serializers.IntegerField(min_value=1, max_value=10)

    def validate_movie_id(self, value):
        if not Movie.objects.filter(id=value).exists():
            raise serializers.ValidationError('Movie not found')
        return value

    def create(self, validated_data):
        request = self.context.get('request')
        movie = Movie.objects.get(id=validated_data['movie_id'])
        return Review.objects.create(
            movie=movie,
            user=request.user if request else None,
            text=validated_data['text'],
            rating=validated_data['rating']
        )
