from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    print(request)
    return HttpResponse('home')


def book(request, name):
    print(request)
    print(name)
    return HttpResponse(f'{name}')


def task2_1(request, name):
    print(request)
    print(name)
    return HttpResponse(f'{name}')


def task2_2(request, name):
    print(request)
    print(name)
    return HttpResponse(f'{name}')
