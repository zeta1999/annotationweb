# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 13:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Annotation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labeledimage',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 24, 13, 55, 5, 313598, tzinfo=utc)),
            preserve_default=False,
        ),
    ]