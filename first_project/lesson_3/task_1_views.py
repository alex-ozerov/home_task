from django.http import (HttpResponse, FileResponse, HttpResponseRedirect,
                         HttpResponseNotAllowed, JsonResponse)
from django.shortcuts import render
from django.templatetags.static import static

from django.views import View

from django.template import loader, RequestContext

from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

# Create your views here.
lets_do_it = [{'priority': 100, 'task': 'Составить список дел'}, {'priority': 150, 'task': 'Изучать Django'},
{'priority': 1, 'task': 'Подумать о смысле жизни'}]


def text(request):
    return HttpResponse(lets_do_it, content_type='text/plain')