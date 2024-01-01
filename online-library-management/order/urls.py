from django.urls import path, include
from . import views

urlpatterns = [
    path('add', views.Add_Order),
    path('show', views.Show_All_Orders),
]