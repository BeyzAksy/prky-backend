# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-06-02 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Park', '0005_park_number_of_car_inside'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='number_of_car_inside',
            field=models.PositiveSmallIntegerField(default='10', verbose_name='Number of Car'),
        ),
    ]