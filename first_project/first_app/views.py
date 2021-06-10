from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html', context={
        'hello_world': 'Hello, world! Вы на 1 странице',
        'urls': ['2 страница:\n'
                 + 'http://127.0.0.1:59/first_app_urls/2/, \n'
                 + '3 страница:\n'
                 + 'http://127.0.0.1:59/first_app_urls/3/\n']
    })


def second_view(request):
    return HttpResponse('Hello, world! Вы на 2 странице. <br>'
                        + '1 страница: <br>'
                        + 'http://127.0.0.1:59/first_app_urls/1/ <br>'
                        + '3 страница: <br>'
                        + 'http://127.0.0.1:59/first_app_urls/3/')


def third_view(request):
    return HttpResponse('Hello, world! Вы на 3 странице. <br>'
                        + '1 страница: <br>'
                        + 'http://127.0.0.1:59/first_app_urls/1/ <br>'
                        + '2 страница: <br>'
                        + 'http://127.0.0.1:59/first_app_urls/2/')


