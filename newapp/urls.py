# newapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:title>', views.blog_details)
]
