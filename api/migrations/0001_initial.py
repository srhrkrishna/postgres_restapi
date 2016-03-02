# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-02 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', max_length=100)),
                ('lastname', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('lastname',),
            },
        ),
    ]