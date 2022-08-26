import email
from pyexpat import model
from django.db import models

# Create your models here.
class User(model.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
