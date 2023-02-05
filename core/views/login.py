from django.shortcuts import render, redirect
from core.forms import LoginForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages


def login(request):
    form = LoginForm()
    context = {
        'title_page': 'Login',
        'form': form,
    }

    return render(request, 'core/login.html', context)


def authenticate(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = form.data['username']
        password = form.data['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login realizado com sucesso')
            return redirect('core:index')

        else:
            messages.error(request, 'username ou senha inválidos')
            return redirect('core:login')
