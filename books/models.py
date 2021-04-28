from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField(upload_to='users/image',  default='defaultuser.png')
    phone = models.IntegerField(default=0, blank=True)
    dob = models.DateField(default=datetime.today())
    gender = models.CharField(default='', max_length=28)

    def __str__(self):
        return self.user.first_name+' '+self.user.last_name



class Book(models.Model):
    title = models.CharField(max_length=20)
    price = models.FloatField()
    author = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to='books/image')

    def __str__(self):
        return self.title