from django.db import models
from django.conf import settings

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    done = models.DateTimeField('date completed')
    created = models.DateTimeField('date published')
    changed = models.DateTimeField('date changed')


class Priority(models.Model):
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)
    PRIORITY = (
        ('L', 'Low'),
        ('N', 'Normal'),
        ('U', 'Urgent'),
    )


class User(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)

