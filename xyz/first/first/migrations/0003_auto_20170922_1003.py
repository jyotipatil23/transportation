# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_author_bookinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='Author_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='first.BookInfo'),
        ),
    ]