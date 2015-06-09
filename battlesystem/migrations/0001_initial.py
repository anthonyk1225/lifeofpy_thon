# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('opponent_name', models.CharField(max_length=40)),
                ('opponent_race', models.CharField(max_length=80)),
                ('battle_date', models.DateTimeField(auto_now_add=True)),
                ('was_victorious', models.BooleanField(default=False)),
                ('character', models.ForeignKey(to='characters.Character')),
            ],
        ),
    ]
