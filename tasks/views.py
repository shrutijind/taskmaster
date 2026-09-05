from django.shortcuts import render
from .models import Task
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def home(request):
    pending_tasks = Task.objects.filter(status="Pending").order_by('due_date')
    completed_tasks = Task.objects.filter(status="Completed").order_by('due_date')
    return render(request, 'task/index.html', {
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks
    })

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'task/create_task.html', {'form': form})

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/update_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('home')
    return render(request, 'task/delete_task.html', {'task': task})

