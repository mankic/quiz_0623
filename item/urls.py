from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # item/
    path('', views.ItemView.as_view()),
    path('order/', views.OrderView.as_view()),
]
