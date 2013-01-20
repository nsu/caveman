from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CheckOut(models.Model):
    climber = models.ForeignKey(User)
    time = models.DateTimeField(auto_now_add=True)


class CheckIn(models.Model):
    climber = models.ForeignKey(User)
    time = models.DateTimeField(auto_now_add=True)
    checkOut = models.ForeignKey(CheckOut, null=True, blank=True)
