from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('home/', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('addition/', views.addition, name='addition'),
]