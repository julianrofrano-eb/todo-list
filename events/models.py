from django.db import models
from django.conf import settings

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(
        max_length=1024,
        null=True,
        blank=True,
    )
    eb_event_id = models.CharField(
        max_length=40,
        unique=True,
    )
    url = models.CharField(max_length=128)
