from django.forms import forms, CharField, PasswordInput


class UserRegisterForm(forms.Form):
    fullname = CharField(label='Nome completo', max_length=100)
    username = CharField(label='Digete um username para Login', max_length=20)
    email = CharField(label='email', max_length=100)
    phone = CharField(label='celular', max_length=11)
    password = CharField(label='Digite sua senha', widget=PasswordInput())
    password_confirm = CharField(label='confirme sua senha', widget=PasswordInput())
