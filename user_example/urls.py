from django.urls import path, include
from . import views

urlpatterns = [
  
    path('', views.index, name="index_user"),
    path('accounts/', include("django.contrib.auth.urls")), # Include / if has more path
    path('register', views.register, name='register'),
]
