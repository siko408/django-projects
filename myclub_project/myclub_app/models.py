from django.db import models
from datetime import datetime
# Create your models here.


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length = 60)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name  #  + " " + DateField(event_date))
