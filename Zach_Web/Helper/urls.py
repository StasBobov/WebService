from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('organizer', views.organizer, name='organizer'),
    path('add', views.add, name='add'),
    path('settings', views.settings, name='settings'),
    path('projects', views.projects, name='projects'),
    # name ссылается на ссылку в html файле в a классе
    path('_add', views._add, name='_add'),
    path('_update/<int:todo_id>/', views._update, name='_update'),
    path('_delete/<int:todo_id>/', views._delete, name='_delete'),
]