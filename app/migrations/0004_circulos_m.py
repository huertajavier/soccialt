# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171126_0330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circulos_m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField(blank=True, null=True)),
                ('y', models.FloatField(blank=True, null=True)),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
    ]
