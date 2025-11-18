from django.http import HttpResponse
from django.shortcuts import render
from ToDo_app.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    is_completed_tasks = Task.objects.filter(is_completed = True)
    context = {
        'tasks' : tasks,
        'is_completed_tasks' : is_completed_tasks,
    }
    return render(request, "home.html" , context)