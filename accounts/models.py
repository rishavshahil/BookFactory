from django.db import models
from datetime import datetime


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField(default=0)
    email = models.CharField(max_length=20)
    feedback = models.CharField(max_length=200)
    subscribe = models.BooleanField(default=True)
    date = models.DateField(default=datetime.today())

    def __str__(self):
        return self.name
