from django.db import models
from users.models import User
from attacks.models import Attack

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=40,unique=True)
    race = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attack = models.ManyToManyField(Attack)
    user = models.ForeignKey(User)

class Attribute(models.Model):
	hit_points = models.IntegerField()
	attack = models.IntegerField()
	defense = models.IntegerField()
	character = models.ForeignKey(Character)
