# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oruma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationnotes',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]