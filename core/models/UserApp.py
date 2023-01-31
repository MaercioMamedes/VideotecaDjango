from django.db import models
from django.contrib.auth.models import User


class UserApp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField('Nome Completo', max_length=100, null=False, blank=False)
    phone = models.CharField('celular', max_length=11)

    @staticmethod
    def create_user_app(kargs):
        user_app = User.objects.create_user(
            username=kargs['username'],
            email=kargs['email'],
            password=kargs['password'],
            first_name=kargs['first_name'],
            last_name=kargs['last_name']
        )

        return UserApp.objects.create(
            user=user_app,
            fullname=kargs['fullname'],
            phone=['phone'],
        )