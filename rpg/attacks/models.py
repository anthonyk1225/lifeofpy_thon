from django.db import models
from models.character import Character

# Create your models here.
class Attack(models.Model):
    name = models.CharField(max_length=40,unique=True)
    