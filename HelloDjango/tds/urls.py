from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('one/', views.one),
    path('load_docs/', views.load_docs),
    path('delete_docs/', views.delete_docs),
    path('logout_view/', views.logout_view),
]
