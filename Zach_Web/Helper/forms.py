from django import forms
from django.contrib.auth.models import User

from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class PlaceholderForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(PlaceholderForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.help_text


class AuthForm(PlaceholderForm):
    username = forms.CharField(max_length=20, help_text="user name")
    # email = forms.EmailField(help_text="email")
    password = forms.CharField(widget=forms.PasswordInput, help_text="password")


class RegisterUserForm(UserCreationForm):
    # должно отформатироваться, но нет
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        # названия элементов можно посмотреть в админке, при просмотре кода
        fields = ('username', 'email', 'password1', 'password2')
