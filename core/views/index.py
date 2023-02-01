from django.shortcuts import render


def index(request):
    context = {
        'title_page': 'Galeria de Filmes'
    }
    return render(request, 'core/index.html', context)
