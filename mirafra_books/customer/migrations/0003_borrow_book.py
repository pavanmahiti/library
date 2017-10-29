# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-29 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_stock'),
        ('customer', '0002_remove_borrow_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
            preserve_default=False,
        ),
    ]