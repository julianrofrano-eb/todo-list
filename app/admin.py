from django.contrib import admin

from .models import Task, Priority, User
# Register your models here.
admin.site.register(Task)
admin.site.register(Priority)
admin.site.register(User)
