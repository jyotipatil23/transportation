# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 07:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0013_patient_p_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('tripplace', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TruckInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truck_no', models.IntegerField()),
                ('truck_load', models.CharField(max_length=50)),
                ('truckroute', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Truckowner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=60)),
                ('contact_no', models.IntegerField()),
                ('place', models.CharField(max_length=50)),
                ('truck_no', models.ManyToManyField(to='first.TruckInfo')),
            ],
        ),
        migrations.AddField(
            model_name='trips',
            name='trip_truckno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.TruckInfo'),
        ),
    ]
