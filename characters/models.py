from django.db import models
from users.models import User
from attacks.models import Attack

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=40)
    race = models.CharField(max_length=80)
    attack = models.ManyToManyField(Attack)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, blank=True)

class Attribute(models.Model):
    hit_points = models.IntegerField()
    power = models.IntegerField()
    character = models.ForeignKey(Character)