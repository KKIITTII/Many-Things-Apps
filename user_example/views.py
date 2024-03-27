from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return render(request, 'user_example/index.html')

def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # create new user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)  # authen new user
            
            login(request, user)
            return render(request, 'user_example/index.html') # redirect('index_user')


    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)