from django.urls import path
from . import views

app_name = 'appeal'

urlpatterns = [
    path('', views.main_form, name='main_form'),
    path('feedback/', views.new_appeal, name='feedback_form'),
    path('profile/', views.profile, name='profile'),
]
