from django.contrib import admin
from django.urls import path, include
from chats import views

urlpatterns = [
    path('webhook', views.chats, name='chats'),
    path('', views.home, name='chatpage'),
]