import os

from django.conf import settings
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.shortcuts import render
from . import forms_review

from lesson_6.forms import MyForm


def my_form(request):
    print(request.POST)
    form = MyForm(request.POST or None, request.FILES or None)

    return render(request, 'form_page.html', context={'form': form})


class ExampleFormView(FormView):
    form_class = forms_review.ExampleForm
    template_name = "model_form_page.html"
    success_url = reverse_lazy("example_form_success")

    def form_valid(self, form):
        return super().form_valid(form)


def example_success(request):
    return HttpResponse('Спасибо за отзыв!')