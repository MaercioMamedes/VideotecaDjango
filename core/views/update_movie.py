from django.shortcuts import render, get_object_or_404, redirect
from core.models import Movie
from django.contrib.auth.models import User


def update_movie(request, movie_id):
    if request.method == 'GET':
        movie = get_object_or_404(Movie,pk=movie_id)
        context = {
            'title_page': 'Atualização da Sinopse',
            'movie': movie,
        }

        return render(request, 'core/updateMovie.html', context)

    if request.method == 'POST':

        movie = get_object_or_404(Movie, pk=movie_id)
        movie.overview = request.POST['overview']
        movie.save()
        return redirect('core:get_movie', movie.id)
