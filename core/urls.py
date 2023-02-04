from django.urls import path
from core.views import user_register, index, login, authenticate, movie_register, add_movie, logout, my_favorite_movies,\
    get_users

app_name = 'core'
urlpatterns = [
    path('', index, name='index'),
    path('cadastro', user_register, name='user_register'),
    path('login', login, name='login'),
    path('auth', authenticate, name='authenticate'),
    path('cadastrar-filme', movie_register, name='movie_register'),
    path('adicionar-filme', add_movie, name='add_movie'),
    path('logout', logout, name='logout'),
    path('meus-filmes', my_favorite_movies, name='my_favorite_movies'),
    path('usuario', get_users, name='get_users'),
]
