from django.shortcuts import render
from .utils import get_auth_token, get_api_events, get_api_event_id
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from .models import Event
from app.models import Task
from eventbrite import Eventbrite
from app.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from bootstrap_datepicker_plus import DateTimePickerInput
from django.shortcuts import redirect
from datetime import datetime


# Create your views here.
class ListEvents(LoginRequiredMixin, TemplateView):
    template_name = "events/event_list.html"

    def get_context_data(self, **kwargs):
        token = get_auth_token(self.request.user)
        context = super(ListEvents, self).get_context_data(**kwargs)
        query = get_api_events(token)
        pagination = query.pagination
        event_ids = [ event['id'] for event in  query.get('events') ]
        unconpleted_tasks = Task.objects.select_related('priority').filter(done=None, event__in=event_ids)
        for event in query.get('events'):
            event['tasks'] = [ task for task in unconpleted_tasks if task.event == event['id'] ]
        context['events'] = query
        context['pagination'] = pagination

        return context


class ListTasksEvent(LoginRequiredMixin, TemplateView):
    template_name = "events/list_tasks_event.html"

    def get_context_data(self, **kwargs):
        token = get_auth_token(self.request.user)
        context = super(ListTasksEvent, self).get_context_data(**kwargs)
        query = get_api_event_id(token, self.kwargs['event_id'])
        context['event'] = query
        context['tasks'] = Task.objects.filter(event=self.kwargs['event_id'])
        return context


class EventTaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'priority', 'reminder']
    success_url = reverse_lazy('event-list')
    template_name = 'app/task_form.html'

    def get_form(self):
        form = super().get_form()
        form.fields['reminder'].widget = DateTimePickerInput()
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.event = self.kwargs['event_id']
        form.save()
        return super(EventTaskCreate, self).form_valid(form)


def complete_task(request, pk, event_id):
    task = Task.objects.get(pk=pk)
    task.done = datetime.now() if not task.done else None
    task.save()
    return redirect('list-tasks-event', event_id=(event_id))


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'priority', 'reminder']
    template_name = 'app/task_form.html'

    def get_success_url(self):
        return reverse_lazy('list-tasks-event', kwargs={'event_id': self.kwargs['event_id']})


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task

    def get_success_url(self):
        return reverse_lazy('list-tasks-event', kwargs={'event_id': self.kwargs['event_id']})
