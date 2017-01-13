# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(unique=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('chef', models.ForeignKey(to='learning_cooking.Chef')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('register_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(to='learning_cooking.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=150, null=True)),
                ('zip', models.CharField(max_length=10)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('email', models.EmailField(unique=True, max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='student',
            field=models.ForeignKey(to='learning_cooking.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together=set([('course', 'student')]),
        ),
    ]
