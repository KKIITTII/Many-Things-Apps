
from django.urls import path, include
from diary import views


urlpatterns = [
    path('', views.index, name="diary_home"),
    path('add/', views.add, name="diary_add")
]
