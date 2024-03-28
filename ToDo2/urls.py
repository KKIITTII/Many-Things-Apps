from django.urls import path
from ToDo2 import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('addTask', views.addTask, name="addTask"),
    path('editTask/<int:pk>', views.editTask, name="editTask"),
    path('deleteTask/<int:pk>', views.deleteTask, name="deleteTask"),
    path('markAsDone/<int:pk>', views.markAsDone, name="markAsDone"),
    path('markAsUnDone/<int:pk>', views.markAsUnDone, name="markAsUnDone"),
    
]