# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='event_amount',
            field=models.CharField(default=250, max_length=1000),
            preserve_default=False,
        ),
    ]