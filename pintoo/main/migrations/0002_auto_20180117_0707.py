# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-16 23:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commodity',
            old_name='Commodity',
            new_name='commodity',
        ),
    ]
