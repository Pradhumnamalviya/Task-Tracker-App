from django.shortcuts import render
from todoapp.models import Task
def home(request):
    todos = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_task = Task.objects.filter(is_completed=True).order_by('-updated_at')
    context = {
        'todos' : todos,
        'completed_task' : completed_task
    }
    return render(request, "home.html", context)


