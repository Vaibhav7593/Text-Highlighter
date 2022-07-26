from django import views
from django.urls import path
from singlepagesite import views

urlpatterns = [
    path('home/',views.home),
    path('homepage/',views.homepage)
]