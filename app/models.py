from django.db import models
from django.conf import settings
from events.models import Event


# Create your models here.


class Priority(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    done = models.DateTimeField('date completed', null=True)
    reminder = models.DateTimeField('reminder date', null=True)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )
    event = models.CharField(max_length=200)




