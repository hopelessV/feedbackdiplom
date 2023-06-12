from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.urls import path


app_name = 'user'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='user/logged_out.html'),
        name='logout'
    ),

    path(
        'login/',
        LoginView.as_view(template_name='user/login.html'),
        name='login'
    ),
]