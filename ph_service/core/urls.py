from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('return_word', views.return_word, name='index')
    
]


