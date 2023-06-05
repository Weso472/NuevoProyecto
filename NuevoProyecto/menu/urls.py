from django.contrib import admin
from django.urls import path
from menu import views


urlpatterns = [
    path('', views.home, name="home"),
    path('product/<id>', views.product, name="product")
]