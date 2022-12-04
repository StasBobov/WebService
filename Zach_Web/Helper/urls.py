from django.urls import path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
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