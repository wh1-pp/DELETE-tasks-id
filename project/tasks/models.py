from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)