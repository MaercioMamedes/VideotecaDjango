from django.urls import path
from core.views import user_register, index, login, authenticate

app_name = 'core'
urlpatterns = [
    path('', index, name='index'),
    path('cadastro', user_register, name='user_register'),
    path('login', login, name='login'),
    path('auth', authenticate, name='authenticate')
]
