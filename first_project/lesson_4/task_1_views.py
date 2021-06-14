from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
import datetime

# Create your views here.

def task_1(request):
    context = {"lets_do_it": [
                   {'priority': 100, 'task': 'Составить список дел'},
                   {'priority': 150, 'task': 'Изучать Django'},
                   {'priority': 1, 'task': 'Подумать о смысле жизни'}
               ]}
    test_template = loader.render_to_string("task_1.html",
                                            context=context)
    return HttpResponse(test_template)
