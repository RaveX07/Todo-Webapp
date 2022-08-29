from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=50)
    EMail = models.CharField(max_length=100)
    Password = models.CharField(max_length=50)

class Todo(models.Model):
    Name = models.CharField(max_length=50)
    Content = models.CharField(max_length=100)