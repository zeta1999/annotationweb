# Generated by Django 2.2.1 on 2019-11-19 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardiac', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segmentation',
            name='image',
        ),
        migrations.DeleteModel(
            name='ControlPoint',
        ),
        migrations.DeleteModel(
            name='Segmentation',
        ),
    ]
