from django.db import models

# Create your models here.
class Battle(models.Model):
    character = models.ForeignKey(Character)
    enemy_type = models.CharField(max_length=40)
    battle_date = models.DateTimeField(auto_now_add=True)
    was_victorious = models.BooleanField(default=False)
