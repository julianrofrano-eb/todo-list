from datetime import datetime
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from bootstrap_datepicker_plus import DateTimePickerInput
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from app.models import Task


class TasksListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        task = Task
        return task.objects.filter(user=self.request.user)


class TasksCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'priority', 'reminder']
    success_url = reverse_lazy('task-list')
    template_name = 'app/task_form.html'

    def get_form(self):
        form = super().get_form()
        form.fields['reminder'].widget = DateTimePickerInput()
        return form
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(TasksCreateView, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'app/task_form.html'
    success_url = reverse_lazy('task-list')


class TaskDelete(LoginRequiredMixin, DeleteView):
    login_url = '/user/login/'
    model = Task
    success_url = reverse_lazy('task-list')


def complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.done = datetime.now() if not task.done else None
    task.save()
    return redirect('task-list')

