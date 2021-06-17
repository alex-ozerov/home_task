"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app_urls/', include('first_app.urls')),
    path('lesson_2/', include('lesson_2.urls')),
    path('lesson_3/', include('lesson_3.task_1_urls')),
    path('lesson_3/', include('lesson_3.task_2_urls')),
    path('lesson_4/', include('lesson_4.task_1_urls')),
    path('lesson_4/', include('lesson_4.task_2_urls')),
    path('lesson_6/', include('lesson_6.urls'))
]
