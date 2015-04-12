from django.db import models

# Create your models here.
class Attack(models.Model):
    name = models.CharField(max_length=100,unique=True)
    element = models.CharField(max_length=100)
    damage = models.DecimalField(max_digits=4,decimal_places=1)
    