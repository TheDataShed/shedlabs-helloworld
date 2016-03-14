# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=200)),
                ('signed_up', models.DateTimeField(verbose_name='signed up')),
            ],
        ),
    ]
