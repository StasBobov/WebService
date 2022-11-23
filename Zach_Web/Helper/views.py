from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import ToDo


def index(request):
    # по умолчанию шаблоны ищутся в папке templates, поэтому дополнительно её не указываем
    return render(request, 'helper/index.html')


def organizer(request):
    # получаем все экземпляры класса Туду
    todos = ToDo.objects.all()

    return render(request, 'helper/organizer.html', {'todo_list': todos, 'title': 'Your_organizer'})



def add(request):
    # по умолчанию шаблоны ищутся в папке templates, поэтому дополнительно её не указываем
    return render(request, 'helper/add.html')


def settings(request):
    # по умолчанию шаблоны ищутся в папке templates, поэтому дополнительно её не указываем
    return render(request, 'helper/settings.html')


def projects(request):
    # по умолчанию шаблоны ищутся в папке templates, поэтому дополнительно её не указываем
    return render(request, 'helper/projects.html')


# добавляем запись в бузу данных при помощи метода POST, который импортировали из декоратора
@require_http_methods(['POST'])
def _add(request):
    # принимаем request из формы
    title = request.POST['title']
    # создаём новую TODOшку
    todo = ToDo(title=title)
    # сохраняем её в базу данных
    todo.save()
    # перемещаемся на страницу organizer
    return redirect('organizer')


def _update(request, todo_id):
    # ищем в базе нужную ToDoшку
    todo = ToDo.objects.get(id=todo_id)
    # поле is_complete ставим в значение False
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('organizer')


def _delete(request, todo_id):
    todo =  todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('organizer')

