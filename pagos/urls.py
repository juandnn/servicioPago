from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:usuario>/', views.pagos_view, name='usuarios_view')
]