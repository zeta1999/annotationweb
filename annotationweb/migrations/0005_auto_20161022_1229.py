# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-22 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annotationweb', '0004_processedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Use anonymized id', max_length=200)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotationweb.Dataset')),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='dataset',
        ),
        migrations.RemoveField(
            model_name='imagesequence',
            name='dataset',
        ),
        migrations.AddField(
            model_name='image',
            name='subject',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='annotationweb.Subject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagesequence',
            name='subject',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='annotationweb.Subject'),
            preserve_default=False,
        ),
    ]
