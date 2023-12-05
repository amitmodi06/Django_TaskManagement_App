from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    context = {"tasks":tasks}
    return render(request, 'index.html', context)


def completed_tasks(request):
    tasks_completed = Task.objects.filter(completed=True)
    context = {"tasks_completed":tasks_completed}
    return render(request, 'completed.html', context)


def remaining_tasks(request):
    tasks_remaining = Task.objects.filter(completed=False)
    context = {"tasks_remaining" : tasks_remaining}
    return render(request, 'remaining.html', context)


def add_task(request):
    return render(request, 'add_task.html')


def delete_task(request):
    return render(request, 'delete.html')


def task_detail(request):
    return render(request, 'task_detail.html')