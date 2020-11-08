from django.urls import path, re_path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login, name='login'),
    re_path('welcome', views.welcome, name='welcome'),
    path('user_logout', views.user_logout, name='logout'),
]