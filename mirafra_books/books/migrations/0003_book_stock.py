# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-29 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20171029_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
