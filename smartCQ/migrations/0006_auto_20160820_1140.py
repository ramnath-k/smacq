# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-20 06:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartCQ', '0005_auto_20160820_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='entity',
        ),
        migrations.AddField(
            model_name='question',
            name='entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartCQ.Entity'),
        ),
    ]
