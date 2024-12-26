from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label="Логин")
    password = forms.CharField(min_length=8, label="Введите пароль")
    repeat_password = forms.CharField(min_length=8, label="Введите пароль")
    age = forms.CharField(max_length=3, label="Ваш возраст")



