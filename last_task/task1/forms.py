from django import forms

class UserRegister(forms.Form):
    ## Вывод ячеек столбиком
    # username = forms.CharField(max_length=30, label='Введите логин')
    # password = forms.CharField(max_length=8, widget=forms.PasswordInput, label='Введите пароль')
    # repeat_password = forms.CharField(max_length=8, widget=forms.PasswordInput, label='Повторите пароль')
    # age = forms.CharField(max_length=3, label='Введите свой возраст')
    ## Вывод ячеек в линию
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=8, widget=forms.PasswordInput)
    repeat_password = forms.CharField(max_length=8, widget=forms.PasswordInput)
    age = forms.CharField(max_length=3, label='Введите свой возраст')