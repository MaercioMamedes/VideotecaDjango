from django.shortcuts import render, redirect
from core.forms import UserRegisterForm
from core.models import UserApp
from django.contrib import messages


def user_register(request):

    if request.method == 'POST':
        form_post = UserRegisterForm(request.POST)
        data = {
            'username': form_post.data['username'],
            'email': form_post.data['email'],
            'password': form_post.data['password'],
            'first_name': form_post.data['fullname'].split()[0],
            'last_name': form_post.data['fullname'].split()[-1],
            'fullname': form_post.data['fullname'],
            'phone': form_post.data['phone'],
        }

        user_app = UserApp.create_user_app(data)
        messages.success(request, f'usuário {user_app.user.username} criado com sucesso')
        return redirect('core:login')

    else:
        print(request.method)
        form = UserRegisterForm()
        context = {
            'title_page': 'Cadastro de usuário',
            'form': form
        }
        return render(request,'core/userRegister.html', context)
