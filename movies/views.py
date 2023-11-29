from django.shortcuts import get_object_or_404
from django.shortcuts import render
from . import models


def index(request):
    movies = models.Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def movie_details(request, movie_id: int):
    movie = get_object_or_404(models.Movie, id=movie_id)
    return render(request, 'movies/movie_details.html', {'movie': movie})
