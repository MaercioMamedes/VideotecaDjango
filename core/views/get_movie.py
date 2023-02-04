from django.shortcuts import render, get_object_or_404
from core.models import Movie


def get_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {'movie':movie}
    return render(request, 'core/getMovie.html', context)
