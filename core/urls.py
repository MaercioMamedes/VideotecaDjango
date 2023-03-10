from django.urls import path
from core.views import user_register, index, login, authenticate, movie_register, add_movie, logout, my_favorite_movies,\
    get_users, get_movie, update_movie, get_profile_user, update_user

app_name = 'core'
urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', user_register, name='user_register'),
    path('login/', login, name='login'),
    path('auth/', authenticate, name='authenticate'),
    path('cadastrar-filme/', movie_register, name='movie_register'),
    path('adicionar-filme/', add_movie, name='add_movie'),
    path('logout/', logout, name='logout'),
    path('meus-filmes/', my_favorite_movies, name='my_favorite_movies'),
    path('usuario/', get_users, name='get_users'),
    path('filmes/<int:movie_id>/', get_movie, name='get_movie'),
    path('update-filme/<int:movie_id>/', update_movie, name='update_movie'),
    path('usuario/<int:user_id>/', get_profile_user, name='get_profile_user'),
    path('update-user/', update_user, name='update_user'),
]
