from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import Poll

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poll_home')
        
    form = CreatePollForm()
    context = {'form': form}
    return render(request, 'poll/create.html', context)

def vote(request, poll_id):
    
    poll = Poll.objects.get(id = poll_id)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == "option1":
            poll.option_one_count += 1
        if selected_option == "option2":
            poll.option_two_count += 1
        if selected_option == "option3":
            poll.option_three_count += 1
        poll.save()
        return redirect('poll_results', poll_id)
            
    context = {'poll': poll}
    return render(request, 'poll/vote.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(id = poll_id)
    context = {'poll': poll}
    return render(request, 'poll/results.html', context)

def home(request):
    polls = Poll.objects.all()
    context = {"polls": polls}
    return render(request, 'poll/home.html', context)