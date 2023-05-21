from .views import *
from django.urls import path

urlpatterns = [
    path('', main_form, name='main_form')
]