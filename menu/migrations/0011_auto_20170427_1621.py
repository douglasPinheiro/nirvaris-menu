# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20160629_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='name_en',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='name_pt_br',
            field=models.CharField(max_length=70, null=True),
        ),
    ]