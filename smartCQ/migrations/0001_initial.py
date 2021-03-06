# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-19 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, default='')),
                ('intent', models.TextField(blank=True, default='')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartCQ.Answer')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartCQ.Entity')),
            ],
        ),
    ]
