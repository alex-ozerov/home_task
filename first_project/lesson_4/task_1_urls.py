from django.urls import path
from . import task_1_views


urlpatterns = [
    path('task_1/', task_1_views.task_1),
]