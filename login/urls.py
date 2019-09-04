from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^change-password/$', auth_views.PasswordChangeView.as_view(), name="user-change-pass"),
    url(r'^login/$', auth_views.LoginView.as_view(), name="user-login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name="user-logout"),
]
