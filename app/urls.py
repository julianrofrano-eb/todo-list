from django.conf.urls import url

from . import views


urlpatterns = [
    url('create', views.TasksCreateView.as_view(), name='task-create'),
    url('', views.TasksListView.as_view(), name='task-list'),
]