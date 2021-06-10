from . import views
from django.urls import path

urlpatterns = [
    path('1/', views.index, name='index'),
    path('2/', views.second_view, name='second_view'),
    path('3/', views.third_view, name='third_view')
]