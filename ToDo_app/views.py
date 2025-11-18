from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Task

# Create your views here.
def add_task(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect('home')


def completed_task(request , pk):
    task = get_object_or_404(Task , pk = pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def incomplete_task(request , pk):
    task = get_object_or_404(Task , pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')