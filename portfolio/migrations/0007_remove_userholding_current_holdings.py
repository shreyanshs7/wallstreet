# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-04 15:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_userholding_current_holdings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userholding',
            name='current_holdings',
        ),
    ]