from django.contrib import admin
from django.urls import path, include
from qrcode_gen import views
urlpatterns = [
    path('', views.index, name='index'),
]
