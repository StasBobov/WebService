from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .utils import *

from .forms import AuthForm


# def login_view(request):
#     auth_form = AuthForm()
#     context = {
#         'form': auth_form
#     }
#     return render(request, 'helper/login.html', context=context)

# class RegisterUser(DataMixin, CreateView):
#     form_class = UserCreationForm
#     template_name = 'index.html'
#     success_url = 'index.html'

def test(request):
    # по умолчанию шаблоны ищутся в папке templates, поэтому дополнительно её не указываем
    return render(request, 'helper/test.html')


def index(request):
    form = AuthForm()
    return render(request, 'helper/index.html', {'form': form})
    # # если POST - пытаемся аутентифицировать пользователя
    # if request.method == 'POST':
    #     auth_form = AuthForm(request.POST)
    #     if auth_form.is_valid():
    #         email = auth_form.cleaned_data['email']
    #         password = auth_form.cleaned_data['password']
    #         pass
    #     else:
    #         pass
    # # по умолчанию шаблоны ищутся в папке templates, поэтому дополнительно её не указываем
    # return render(request, 'helper/index.html', context=auth_form)


def organizer(request):
    return render(request, 'helper/organizer.html')


def add(request):
    # по умолчанию шаблоны ищутся в папке templates, поэтому дополнительно её не указываем
    return render(request, 'helper/add.html')


def settings(request):
    # по умолчанию шаблоны ищутся в папке templates, поэтому дополнительно её не указываем
    return render(request, 'helper/settings.html')


def projects(request):
    # по умолчанию шаблоны ищутся в папке templates, поэтому дополнительно её не указываем
    return render(request, 'helper/projects.html')


