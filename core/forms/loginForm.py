from django.forms import forms, CharField, PasswordInput


class LoginForm(forms.Form):
    username = CharField(label='usuário', max_length=20)
    password = CharField(label='ssenha', widget=PasswordInput)
