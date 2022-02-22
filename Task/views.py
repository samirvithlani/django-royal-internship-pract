from django.http import request
from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import Task
from django.views.generic import DetailView

class CreateTask(CreateView):
    model = Task
    fields = ['task_name', 'task_description']
    template_name = 'Task/create_task.html'
    success_url = '/task/view/'
    
class DeleteTask(DeleteView):
    model = Task
    success_url= 'task/view/'

def index(request):
    return render(request, 'Task/index.html')

class UpdateTask(UpdateView):
    model = Task
    fields = ['task_name', 'task_description']
    template_name = 'Task/update_task.html'
    success_url = '/task/view/'

class TaskDetail(DetailView):
    model = Task
    template_name = 'Task/task_detail.html'