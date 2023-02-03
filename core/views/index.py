from django.shortcuts import render
from core.models import Movie


def index(request):

    list_movie = Movie.objects.all()
    context = {
        'title_page': 'Galeria de Filmes',
        'list_movie': list_movie
    }
    return render(request, 'core/index.html', context)
