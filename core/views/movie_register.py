from django.shortcuts import render


def movie_register(request):
    if request.method == 'GET':
        context = {
            'title_page': 'Procure seu filme favorito no The MovieDB ',
        }
        return render(request, 'core/movieRegister.html', context)
