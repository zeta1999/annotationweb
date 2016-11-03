# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-24 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotationweb', '0005_auto_20161022_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='label',
            field=models.ManyToManyField(help_text='<button onclick="window.open(\'/new-label/\', \'Add new label\', \'width=400,height=200,scrollbars=no\');" type="button">Add new label</button>', to='annotationweb.Label'),
        ),
    ]
