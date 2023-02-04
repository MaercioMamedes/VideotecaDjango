from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from core.models import FavoriteMovie, Movie


def my_favorite_movies(request):
    user = get_object_or_404(User, pk=request.user.id)
    favorite_movies = FavoriteMovie.objects.filter(user=user.id)

    list_movie = []

    for element in favorite_movies:
        list_movie.append(element.movie)

    context = {
        'title_page': 'Meus Filmes',
        'list_movie': list_movie,
    }

    return render(request, 'core/myFavoriteMovies.html', context)
