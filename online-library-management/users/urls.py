from django.urls import path
from users import views

urlpatterns = [
    
    path('add', views.Add_User),
    path('show', views.Show_Users),
]