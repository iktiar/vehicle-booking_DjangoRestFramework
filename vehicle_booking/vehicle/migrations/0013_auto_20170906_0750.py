# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0012_requisitionticketlog_passenger_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requisitionticketlog',
            old_name='type',
            new_name='vehicle_type',
        ),
        migrations.AlterField(
            model_name='requisitionticketlog',
            name='passenger_number',
            field=models.IntegerField(),
        ),
    ]
