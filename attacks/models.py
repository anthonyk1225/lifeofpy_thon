from django.db import models

# Create your models here.
class Attack(models.Model):
    name = models.CharField(max_length=100)
    element = models.CharField(max_length=100)
