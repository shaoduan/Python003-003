from django.urls import path

from . import views

urlpatterns = [
    path('filter', views.filter, name='filter'),
    path('', views.index, name='index'),
    
]