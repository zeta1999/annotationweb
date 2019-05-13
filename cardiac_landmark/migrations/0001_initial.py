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
            name='CardiacLandmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_ED', models.IntegerField()),
                ('frame_ES', models.IntegerField()),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='annotationweb.Annotation')),
            ],
        ),
        migrations.CreateModel(
            name='ControlPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('index', models.PositiveIntegerField()),
                ('phase', models.PositiveIntegerField(choices=[(0, 'End Diastole'), (1, 'End Systole')])),
                ('object', models.PositiveIntegerField(choices=[(0, 'Anterior'), (1, 'Apex'), (2, 'Inferior')])),
                ('uncertain', models.BooleanField()),
                ('landmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardiac_landmark.CardiacLandmark')),
            ],
        ),
    ]
