from django.urls import path
from . import task_1_views


urlpatterns = [
    path('main/text/', task_1_views.text, name="text"),
]

