from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from datetime import datetime

from .models import ToDo
from .models import Task


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
    todo = todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('organizer')


def current_task(request):
    current_time = datetime.now()
    current_hour = current_time.hour
    current_min = current_time.minute

    tasks_list = list(Task.objects.all())
    current_task = None

    def time_in_mins(hr, min):
        return hr * 60 + min

    for task in tasks_list:
        start_time_hour = task.start_time.hour
        start_time_min = task.start_time.minute

        day_list = []

        if task.sunday == True:
            day_list.append('Sunday')
        if task.monday == True:
            day_list.append('Monday')
        if task.tuesday == True:
            day_list.append('Tuesday')
        if task.wednesday == True:
            day_list.append('Wednesday')
        if task.thursday == True:
            day_list.append('Thursday')
        if task.friday == True:
            day_list.append('Friday')
        if task.saturday == True:
            day_list.append('Saturday')


        if ((day_list.count(current_time.strftime('%A')) == 0)
            or (time_in_mins(start_time_hour, start_time_min) - 6) > time_in_mins(current_hour, current_min)):
                continue

        current_task = task

    if current_task == None:
        return render(request, 'settings.html')
    else:
        return render(request, 'projects.html', {'obj': current_task})
