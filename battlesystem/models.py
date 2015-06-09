from django.db import models
from django.contrib.contenttypes import GenericForeignKey
from django.contrib.contenttypes import ContentType

# Create your models here.
class Battle(models.Model):
    opponent_name = models.CharField(max_length=40)
    opponent_race = models.CharField(max_length=80)
    battle_date = models.DateTimeField(auto_now_add=True)
    was_victorious = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

