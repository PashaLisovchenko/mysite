# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20171017_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]
