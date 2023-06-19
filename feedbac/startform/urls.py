from django.urls import path
from . import views

app_name = 'appeal'

urlpatterns = [
    
    path('profile/<str:username>', views.profile, name='profile'),
    path('detail/<int:feedback_id>', views.feedback_detail, name='feedback_detail'),
    path('feedback/', views.new_appeal, name='feedback_form'),
    path('create/', views.post_create, name='post_create'),
    path('all_posts/', views.all_posts, name='all_posts'),
    path('consent/', views.consent, name='consent'),
    path('', views.main_form, name='main_form'),
]
