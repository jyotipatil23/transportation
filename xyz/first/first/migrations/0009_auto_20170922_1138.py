# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0008_auto_20170922_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='Author_book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='first.BookInfo'),
        ),
    ]
