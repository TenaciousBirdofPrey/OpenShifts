# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-12 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todvstom', '0009_auto_20170511_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='ballroom',
            field=models.TextField(blank=True, default='no information available', max_length=200, verbose_name='Ballroom'),
        ),
        migrations.AlterField(
            model_name='room',
            name='beethoven',
            field=models.TextField(blank=True, default='no information available', max_length=200, verbose_name='Beethoven'),
        ),
        migrations.AlterField(
            model_name='room',
            name='board',
            field=models.TextField(blank=True, default='no information available', max_length=200, verbose_name='Temple Boardroom'),
        ),
        migrations.AlterField(
            model_name='room',
            name='capitol',
            field=models.TextField(blank=True, default='no information available', max_length=200, verbose_name='Capitol'),
        ),
        migrations.AlterField(
            model_name='room',
            name='handel',
            field=models.TextField(blank=True, default='no information available', max_length=200, verbose_name='Handel'),
        ),
        migrations.AlterField(
            model_name='room',
            name='haydn',
            field=models.TextField(blank=True, default='no information available', max_length=200, verbose_name='Haydn'),
        ),
        migrations.AlterField(
            model_name='room',
            name='mozart',
            field=models.TextField(blank=True, default='no information available', max_length=200, verbose_name='mozart'),
        ),
        migrations.AlterField(
            model_name='room',
            name='other',
            field=models.TextField(blank=True, default='no information available', max_length=200, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='room',
            name='set_date',
            field=models.DateField(blank=True, default='no information available', null=True, verbose_name='set date'),
        ),
        migrations.AlterField(
            model_name='room',
            name='symph_a',
            field=models.TextField(blank=True, default='no information available', max_length=200, verbose_name='Symphony A'),
        ),
        migrations.AlterField(
            model_name='room',
            name='symph_b',
            field=models.TextField(blank=True, default='no information available', max_length=200, verbose_name='Symphony b'),
        ),
        migrations.AlterField(
            model_name='room',
            name='thirty_third',
            field=models.TextField(blank=True, default='no information available', max_length=200, verbose_name='33rd'),
        ),
    ]
