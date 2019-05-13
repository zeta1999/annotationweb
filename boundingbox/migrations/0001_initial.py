# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-05-13 12:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('annotationweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoundingBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.PositiveIntegerField()),
                ('y', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotationweb.Annotation')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotationweb.Label')),
            ],
        ),
    ]
