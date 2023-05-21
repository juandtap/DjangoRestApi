from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    lastname = models.CharField(max_length=100, blank=False, default='')
    country = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    gender = models.CharField(max_length=10, blank=True, default='')
