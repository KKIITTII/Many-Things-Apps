
from django.urls import path
from . import views

urlpatterns = [
    path('list_employee/', views.list_employee, name="list_employee"),
    path('list_employee/<int:pk>/', views.employee_datail, name="employee_detail")
]
