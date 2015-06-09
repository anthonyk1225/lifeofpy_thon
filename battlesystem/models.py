from django.db import models
from characters.models import Character

# Create your models here.
class Battle(models.Model):
    opponent_name = models.CharField(max_length=40)
    opponent_race = models.CharField(max_length=80)
    battle_date = models.DateTimeField(auto_now_add=True)
    was_victorious = models.BooleanField(default=False)
    character = models.ForeignKey(Character)

