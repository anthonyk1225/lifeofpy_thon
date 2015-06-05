# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('attacks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('race', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attack', models.ManyToManyField(to='attacks.Attack')),
                ('user', models.ForeignKey(to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('race', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attack', models.ManyToManyField(to='attacks.Attack')),
            ],
        ),
        migrations.CreateModel(
            name='EnemyAttribute',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('hit_points', models.IntegerField()),
                ('power', models.IntegerField()),
                ('character', models.ForeignKey(to='characters.Enemy')),
            ],
        ),
        migrations.CreateModel(
            name='HeroAttribute',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('hit_points', models.IntegerField()),
                ('power', models.IntegerField()),
                ('character', models.ForeignKey(to='characters.Character')),
            ],
        ),
    ]
