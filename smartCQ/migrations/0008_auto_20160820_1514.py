# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-20 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartCQ', '0007_auto_20160820_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='intent',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='question',
            name='entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartCQ.Entity'),
        ),
    ]
