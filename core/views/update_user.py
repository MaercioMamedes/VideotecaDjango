from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from core.models import UserApp


def update_user(request):
    if request.method == 'GET':
        user_app = get_object_or_404(UserApp, user=request.user.id)
        context = {
            'title_page': 'Atualização dos dados do usuário',
            'user_app': user_app
        }

        return render(request, 'core/updateUser.html', context)

    if request.method == 'POST':
        user_app = get_object_or_404(UserApp, user=request.user.id)
        user = get_object_or_404(User, pk=request.user.id)
        password = request.POST['password']

        if auth.authenticate(request, username=user.username, password=password):
            user_app.fullname = request.POST['fullname']
            user_app.phone = request.POST['phone']
            user.username = request.POST['username']
            user.first_name = request.POST['fullname'].split()[0]
            user.last_name = request.POST['fullname'].split()[-1]
            user.email = request.POST['email']

            user_app.save()
            user.save()

            return redirect('core:get_profile_user', user_app.user.id)


