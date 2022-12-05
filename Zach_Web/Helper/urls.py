from django.urls import path
# from django.conf.urls import url
from . import views

urlpatterns = [
    # path('register/', views.register_view, name='register'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),

    path('', views.index, name='index'),

    path('logout/', views.logout_user, name='logout'),


    path('post_list/', views.post_list, name='post_list'),
# <int:pk> означает, что Django ожидает целочисленное значение и преобразует его в представление — переменную pk.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    # path('login/', views.login_view, name='login'),
    # path('', views.MainView.as_view()),
    # # path('register', views.LoginFormView, name='register'),
    # path('login', views.RegisterFormView.as_view()),

    path('organizer', views.organizer, name='organizer'),
    path('add', views.add, name='add'),
    path('settings', views.settings, name='settings'),
    path('projects', views.projects, name='projects'),
    path('test', views.test, name='test'),
]