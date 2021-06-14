from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
import datetime


def home(request):
    test_template = loader.render_to_string("task_2.html", request=request)
    return HttpResponse(test_template, content_type='text/html')


def post_page(request, name):
    if name == 'lukepage':
        return HttpResponse('Люк Скайуокер — один из главных персонажей вселенной «Звёздных войн», джедай, сын'
                            'сенатора с Набу Падме Амидалы Наберри и рыцаря-джедая Энакина Скайуокера')
    elif name == 'hanpage':
        return HttpResponse('Хан. Соло — пилот космического корабля «Тысячелетний сокол», его бортмехаником и вторым'
                            'пилотом является вуки по имени Чубакка.')
    elif name == 'leipage':
        return HttpResponse('Лея Органа — дочь рыцаря-джедая Энакина Скайуокера и сенатора Падме Амидалы Наберри.')



