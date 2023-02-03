from django.shortcuts import render
from core.helpers import ClientTheMovieDB


def movie_register(request):
    if request.method == 'GET':
        context = {
            'title_page': 'Procure seu filme favorito no The MovieDB ',
        }
        return render(request, 'core/movieRegister.html', context)

    elif request.method == 'POST':
        movie_title = request.POST['movie']
        client = ClientTheMovieDB()
        list_movie = client.search_movie(movie_title)['results']
        context = {
            'list_movie': list_movie,
            'title_page': 'Buscar filme no The MovieDB',
        }
        return render(request, 'core/movieRegister.html', context)


