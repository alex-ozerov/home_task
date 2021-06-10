from . import views
from django.urls import path, re_path

urlpatterns = [
    path('home/', views.home, name='home-view'),
    path('book/<name>/', views.book, name='book'),
    re_path(r'^task2_1/([db]o[gx])/$', views.task2_1),
    re_path(r'^task2_2/([^db]o[^gx])/$', views.task2_2)
]
