# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-19 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartCQ', '0003_auto_20160819_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.ManyToManyField(blank=True, null=True, to='smartCQ.Answer'),
        ),
    ]