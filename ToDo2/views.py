from django.shortcuts import render, redirect
from .models import Task
from django.views.decorators.http import require_POST


# Create your views here.
def home(request):
    
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = { 'tasks': tasks }
    return render(request, './ToDo2/home-todo.html', context)


@require_POST
def addTask(request):

    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect('home')