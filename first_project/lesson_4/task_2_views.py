from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
import datetime


def home(request):
    test_template = loader.render_to_string("task_2.html", request=request)
    return HttpResponse(test_template, content_type='text/html')


data = {'lukepage': 'Люк Скайуокер — один из главных персонажей вселенной «Звёздных войн», джедай, сын сенатора ' 
                    'с Набу Падме Амидалы Наберри и рыцаря-джедая Энакина Скайуокера',
        'hanpage': 'Хан. Соло — пилот космического корабля «Тысячелетний сокол», его бортмехаником и вторым '
                   'пилотом является вуки по имени Чубакка.',
        'leipage': 'Лея Органа — дочь рыцаря-джедая Энакина Скайуокера и сенатора Падме Амидалы Наберри.'}


def post_page(request, name):
    return render(request, 'task_2_2.html', {'text': data[name]})







