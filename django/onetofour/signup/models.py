from django.db import models

# Create your models here.
class signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    usertype = models.BooleanField(default=True)
    level = models.PositiveSmallIntegerField(max_length= 4)
