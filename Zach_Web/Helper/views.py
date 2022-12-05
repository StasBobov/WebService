from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .utils import *
from .forms import AuthForm, PostForm, RegisterUserForm
from .models import Post
from django.utils import timezone
from django.contrib.auth.views import LoginView, LogoutView


'''работает'''
class LoginUser(LoginView):
    form_class = AuthForm
    template_name = 'helper/index.html'
    # вызывается, если пользователь верно ввёл логин и пароль
    def get_success_url(self):
        return reverse_lazy('index')


def index(request):
    if request.method == "POST":
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            # authenticate вернёт объект пользователя или None
            user = authenticate(username=username, password=password)
            # сначала аутентификация
            if user:
                # проверяет, не отключили ли аккаунт пользователю
                if user.is_active:
                    # если всё норм, то логиним пользователя
                    login(request, user)
                    return render(request, 'helper/index.html', {'auth_form': auth_form})
                else:
                    auth_form.add_error('__all__', 'Error! User account is not active.')
            else:
                auth_form.add_error('__all__', 'Error! Check if the username and password are correct.')
    else:
        auth_form = AuthForm()
    return render(request, 'helper/index.html', {'auth_form': auth_form})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'helper/register.html'
    success_url = reverse_lazy('login')

    # при успешной регистрации
    def form_valid(self, form):
        # самостоятельно сохраняем форму в DB
        user = form.save()
        # авторизовываем пользователя
        login(self.request, user)
        return redirect(index)

'''работает'''
def register_view(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            # сохраняем пользователя и пароль
            form.save()
            # чтобы сразу залогинить берём данные из Post запроса
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # перенаправляем пользователя на главную страницу
            return redirect('/')
    else:
            form = RegisterUserForm()
    return render(request, 'helper/register.html', {'form': form})


'''работает'''
def logout_user(request):
    logout(request)
    return redirect('login')


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


def test(request):
    # по умолчанию шаблоны ищутся в папке templates, поэтому дополнительно её не указываем
    return render(request, 'helper/test.html')


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'helper/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'helper/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'helper/post_edit.html', {'form': form})