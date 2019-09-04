from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url('(?P<event_id>[0-9]+)/task/complete/(?P<pk>[0-9]+)/$', views.complete_task, name='task-complete'),
    url('(?P<event_id>[0-9]+)/task/delete/(?P<pk>[0-9]+)/$', views.TaskDelete.as_view(), name='task-delete'),
    url('(?P<event_id>[0-9]+)/task/update/(?P<pk>[0-9]+)/$', views.TaskUpdate.as_view(), name='task-update'),
    url('(?P<event_id>[0-9]+)/task/create/', views.EventTaskCreate.as_view(), name='task-create-event'),
    url('(?P<event_id>[0-9]+)/tasks/', views.ListTasksEvent.as_view(), name='list-tasks-event'),
    url('', views.ListEvents.as_view(), name='event-list'),
]
