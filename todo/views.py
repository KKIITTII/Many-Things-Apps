from django.shortcuts import render, redirect
from .models import Todo
from .form import TodoForm
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def index(request):
    
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()
    context = {"todo_list": todo_list, "form": form}
    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = Todo(text = form.cleaned_data['text'])
        todo.save()
        return redirect('index_todo')

def completeTodo(request, todo_id):
    
    todo = Todo.objects.get(id = todo_id)
    todo.complete = True
    todo.save()
    return redirect('index_todo')

def deleteComplete(request):
    
    todo_complete = Todo.objects.filter(complete__exact=True)
    todo_complete.delete()
    return redirect('index_todo')

def deleteAll(request):
    
    todo_all = Todo.objects.all()
    todo_all.delete()
    return redirect('index_todo')
