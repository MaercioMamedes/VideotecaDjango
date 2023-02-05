from django.shortcuts import render, get_object_or_404
from core.models import UserApp, FavoriteMovie


def get_profile_user(request, user_id):

    if request.method == 'GET':
        user_app = get_object_or_404(UserApp, user=user_id)
        favorite_movies = FavoriteMovie.objects.filter(user=user_app.user.id)

        list_movie = []

        for element in favorite_movies:
            list_movie.append(element.movie)

        context = {
            'title_page': 'Perfil do Usuário',
            'user_app': user_app,
            'list_movie': list_movie,
        }

        return render(request, 'core/userProfile.html', context)
