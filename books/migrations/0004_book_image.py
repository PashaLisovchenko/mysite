# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/book/', verbose_name='Ссылка картинки'),
        ),
    ]
