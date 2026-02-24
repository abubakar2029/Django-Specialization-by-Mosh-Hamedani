from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_01, name='hello'),
    path('hello_02/', views.hello_02, name='hello_02'),
    path('hello_03/', views.hello_03, name='hello_03'),
]