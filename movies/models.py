from django.db import models
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rental_rate = models.FloatField()
    creation_date = models.DateTimeField(default=timezone.now)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
