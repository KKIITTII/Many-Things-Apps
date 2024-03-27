from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index_todo"),
   path('add', views.addTodo, name="add_todo"),
   path('complete/<todo_id>', views.completeTodo, name="complete_todo"),
   path('deleteall', views.deleteAll, name='deleteall_todo'),
   path('deletecomplete', views.deleteComplete, name='deletecomplete')
]
