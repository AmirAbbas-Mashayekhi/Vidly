from django.shortcuts import render
from . import models


def index(request):
    movies = models.Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})
