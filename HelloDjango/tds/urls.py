from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('one/', views.one),
    path('two/', views.two),
]
