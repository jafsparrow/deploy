# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oruma', '0006_auto_20170423_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='enquiry_notes',
            field=models.TextField(default='Plese Add Inquiry Notes here', null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='enquiry_team',
            field=models.CharField(default='Enter enquiry team Names', max_length=100),
        ),
        migrations.AddField(
            model_name='application',
            name='extra_notes',
            field=models.CharField(default='Please Add Extra Notes Here', max_length=100),
        ),
        migrations.AddField(
            model_name='application',
            name='payment_details',
            field=models.CharField(default='Please Add check/DD details', max_length=100),
        ),
    ]
