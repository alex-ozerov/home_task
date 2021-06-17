from django.urls import path
from lesson_6 import views

urlpatterns = [
    path('try-form/', views.my_form, name='my_form'),
    path('example-form/', views.ExampleFormView.as_view(), name='example_form'),
    path('example-form/success/', views.example_success, name='example_form_success'),
]