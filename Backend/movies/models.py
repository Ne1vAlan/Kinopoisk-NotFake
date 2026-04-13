from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title