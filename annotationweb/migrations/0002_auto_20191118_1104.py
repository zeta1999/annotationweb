# Generated by Django 2.2.1 on 2019-11-18 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotationweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='post_processing_method',
            field=models.CharField(default='', help_text='Name of post processing method to use', max_length=255),
        ),
        migrations.AlterField(
            model_name='label',
            name='color_blue',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='label',
            name='color_green',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='label',
            name='color_red',
            field=models.PositiveSmallIntegerField(default=255),
        ),
    ]
