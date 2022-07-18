from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('one/', views.one),
    path('load_docs/', views.load_docs),
    path('show_table/', views.show_table),
    path('delete_docs/', views.delete_docs),
    path('logout_view/', views.logout_view),
    path('setcommand/<int:id>/<str:cmd>/', views.setcommand),
    path('cmdstrind.txt', views.cmdstrind),
    path('post_resp/', views.post_resp),
]
