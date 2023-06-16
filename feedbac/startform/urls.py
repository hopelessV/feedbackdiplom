from django.urls import path
from . import views

app_name = 'appeal'

urlpatterns = [
    path('', views.main_form, name='main_form'),
    path('feedback/', views.new_appeal, name='feedback_form'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('detail/<int:feedback_id>', views.feedback_detail, name='feedback_detail'),
    path('consent/', views.consent, name='consent'),
]
