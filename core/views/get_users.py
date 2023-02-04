from django.shortcuts import render
from core.models import UserApp, FavoriteMovie
from django.contrib.auth.models import User


def get_users(request):
    users = User.objects.all()
    user_app = UserApp.objects.all()
    favorite_movie = FavoriteMovie.objects.all()

    list_users = []

    for user in users:
        movies = favorite_movie.filter(user=user)
        list_users.append({'name':user.username, 'qtd_movie':len(movies)})

    context = {
        'title_page': 'Usuários cadastrados',
        'list_users': list_users,
    }
    return render(request, 'core/listUsers.html', context)

