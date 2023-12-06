from django.shortcuts import render, redirect
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
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        due_time = request.POST.get("due_time")
        completed = False

        if title != "" and due_date != "" and due_time != "":
            task = Task(
                title=title,
                description=description,
                due_date=due_date,
                due_time=due_time,
                completed=completed
            )
            task.save()
            return redirect('home')
    
    else:
        return render(request, 'add_task.html')
    return render(request, 'add_task.html')


def delete_task(request):
    return render(request, 'delete.html')


def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {"task":task}
    return render(request, 'task_detail.html', context)