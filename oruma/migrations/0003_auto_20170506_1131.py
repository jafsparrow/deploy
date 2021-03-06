# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-06 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oruma', '0002_auto_20170504_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Submitted', 'Submitted'), ('Review', 'Review'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='New', max_length=10),
        ),
        migrations.AlterField(
            model_name='dependend',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dependend',
            name='full_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='dependend',
            name='occupation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dependend',
            name='relation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
