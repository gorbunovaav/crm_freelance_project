from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

INPUT_CLASS = 'w-full py-4 px-6 rounded-xl bg-gray-100 mt-3 mb-3'

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите имя пользователя',
            'class': INPUT_CLASS,
        })
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введите пароль',
            'class': INPUT_CLASS,
        })
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control form-control-sm"

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите имя пользователя',
            'class': INPUT_CLASS,
        })
    )
    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Введите свой e-mail',
            'class': INPUT_CLASS,
        })
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введите пароль',
            'class': INPUT_CLASS,
        })
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Подтвердите пароль',
            'class': INPUT_CLASS,
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control form-control-sm"