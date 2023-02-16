from importlib.resources import path
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    