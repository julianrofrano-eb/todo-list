from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from app.models import Task


class TasksListView(ListView):
    model = Task


class TasksCreateView(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')

