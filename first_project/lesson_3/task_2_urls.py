from django.urls import path
from . import task_2_views

urlpatterns = [
    path('main/', task_2_views.main),
    path('lukepage/', task_2_views.lukepage, name="text_luk"),
    path('hanpage/', task_2_views.hanpage, name="text_han"),
    path('leipage/', task_2_views.leipage, name="text_lei")
]