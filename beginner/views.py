from django.shortcuts import render
from .models import Employee
from django.http import Http404
# Create your views here.

def list_employee(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, './beginner/list_employee.html', context)

def employee_datail(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        context = {
            'employee': employee
        }
        return render(request, './beginner/employee_detail.html', context)
    except:
        raise Http404