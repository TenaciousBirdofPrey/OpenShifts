# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Is_Room_Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='date')),
            ],
            options={
                'permissions': (('can_confirm_is_set', 'Can confirm is set'),),
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='date')),
            ],
            options={
                'permissions': (('can_add_set', 'Can add set'),),
            },
        ),
    ]
