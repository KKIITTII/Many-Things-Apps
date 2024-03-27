from django.urls import path
from ToDo2 import views


urlpatterns = [
    path('home/', views.home, name="home"),
    
]