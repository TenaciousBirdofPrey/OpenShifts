# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todvstom', '0003_auto_20170511_1039'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Is_Room_Set',
        ),
        migrations.AlterModelOptions(
            name='rooms',
            options={},
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='date',
        ),
        migrations.AddField(
            model_name='rooms',
            name='symph_a',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
