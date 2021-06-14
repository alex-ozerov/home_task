from django.urls import path
from . import task_2_views

urlpatterns = [
    path('home/', task_2_views.home, name="home"),
    path('post/<str:name>/', task_2_views.post_page, name="posts_list")
]