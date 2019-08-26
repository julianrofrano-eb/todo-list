from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'update/(?P<pk>[0-9]+)/$', views.TaskUpdate.as_view(), name='task-update'),
    url('create', views.TasksCreateView.as_view(), name='task-create'),
    url('', views.TasksListView.as_view(), name='task-list'),
]