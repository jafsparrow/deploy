# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 04:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=12)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('date_of_birth', models.DateField()),
                ('occupation', models.CharField(max_length=50)),
                ('monthly_family_income', models.IntegerField(default=1000)),
                ('no_earners', models.IntegerField(default=1)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_amount', models.IntegerField(default=0)),
                ('self_amount', models.IntegerField(default=0)),
                ('ouruma_expected', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('New', 'New'), ('Submitted', 'Submitted'), ('Review', 'Review'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='N', max_length=10)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('application_number', models.CharField(max_length=60)),
                ('payment_mode', models.CharField(choices=[('Check', 'Check'), ('Cash', 'Cash'), ('DD', 'DD')], max_length=50, null=True)),
                ('payment_details', models.CharField(max_length=100, null=True)),
                ('payment_frequency', models.CharField(choices=[('Monthly', 'Monthly'), ('Full', 'Full'), ('Part', 'Part')], max_length=50, null=True)),
                ('extra_notes', models.CharField(max_length=100, null=True)),
                ('enquiry_team', models.CharField(max_length=100, null=True)),
                ('enquiry_notes', models.TextField(null=True)),
                ('Applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oruma.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(null=True)),
                ('created_date', models.DateField(auto_now=True)),
                ('Application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oruma.Application')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dependend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('relation', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField(null=True)),
                ('occupation', models.CharField(max_length=50, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oruma.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid_type', models.CharField(max_length=200)),
                ('add_information', models.CharField(max_length=500)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oruma.Application')),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='application/files')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oruma.Application')),
            ],
        ),
        migrations.CreateModel(
            name='Recommender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=80)),
                ('address', models.TextField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='Recommender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oruma.Recommender'),
        ),
    ]
