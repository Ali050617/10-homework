from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks


def tasks_list(request):
    tasks = Tasks.objects.all()
    ctx = {'tasks': tasks}
    return render(request, 'tasks/tasks-list.html', ctx)

def tasks_create(request):
    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        due_date = request.POST.get('due_date')
        description = request.POST.get('description')
        if task_title and due_date and description:
            Tasks.objects.create(
                task_title=task_title,
                due_date=due_date,
                description=description
            )
            return redirect('tasks:list')
    return render(request, 'tasks/tasks-form.html')


def tasks_detail(request, pk):
    tasks = get_object_or_404(Tasks, pk=pk)
    ctx = {'tasks': tasks}
    return render(request, 'tasks/detail.html', ctx)


def tasks_update(request, pk):
    tasks = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        due_date = request.POST.get('due_date')
        description = request.POST.get('description')
        if task_title and due_date and description:
            tasks.task_title = tasks_create
            tasks.due_date = due_date
            tasks.description =description
            tasks.save()
            return redirect(tasks.get_detail_url())
    ctx = {'tasks': tasks}
    return render(request, 'tasks/tasks-form.html', ctx)



def tasks_delete(request, pk):
    tasks = get_object_or_404(Tasks, pk=pk)
    tasks.delete()
    return redirect('tasks:list')


