from django.shortcuts import render


def index(request):
    # по умолчанию шаблоны ищутся в папке templates, поэтому дополнительно её не указываем
    return render(request, 'helper/index.html')

