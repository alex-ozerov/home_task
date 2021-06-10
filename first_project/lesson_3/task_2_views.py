from django.http import (HttpResponse, FileResponse, HttpResponseRedirect,
                         HttpResponseNotAllowed, JsonResponse)
from django.shortcuts import render
from django.templatetags.static import static

from django.views import View

from django.template import loader, RequestContext

from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
import base64


def main(request):
    test_template = loader.render_to_string("main.html", request=request)
    return HttpResponse(test_template, content_type='text/html')



def lukepage(request):
    return HttpResponse('Люк Скайуокер — один из главных персонажей вселенной «Звёздных войн», джедай, сын'
                        'сенатора с Набу Падме Амидалы Наберри и рыцаря-джедая Энакина Скайуокера')


def hanpage(request):
    return HttpResponse('Хан. Соло — пилот космического корабля «Тысячелетний сокол», его бортмехаником и вторым'
                        'пилотом является вуки по имени Чубакка.')


def leipage(request):
    return HttpResponse('Лея Органа — дочь рыцаря-джедая Энакина Скайуокера и сенатора Падме Амидалы Наберри.')



