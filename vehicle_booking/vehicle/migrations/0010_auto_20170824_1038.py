# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 10:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0009_auto_20170824_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requisitionticketlog',
            old_name='vehicle_Id',
            new_name='vehicle_id',
        ),
    ]
