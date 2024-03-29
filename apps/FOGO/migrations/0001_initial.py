# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-29 22:39
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
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('admin_flag', models.IntegerField(default=0)),
                ('street', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('zipcode', models.IntegerField()),
                ('aptnum', models.IntegerField(default=0)),
                ('lat', models.CharField(max_length=60)),
                ('lon', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
