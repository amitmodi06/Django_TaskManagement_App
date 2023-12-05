from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')


def completed_tasks(request):
    return render(request, 'completed.html')


def remaining_tasks(request):
    return render(request, 'remaining.html')


def add_task(request):
    return render(request, 'add_task.html')


def delete_task(request):
    return render(request, 'delete.html')


def task_detail(request):
    return render(request, 'task_detail.html')