# Generated by Django 5.1.4 on 2024-12-28 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envs', '0003_remove_environment_height_remove_environment_length_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='humiditycontroltype',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='humiditycontroltype',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='humiditycontroltype',
            name='user',
        ),
        migrations.RemoveField(
            model_name='lighttype',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='lighttype',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='lighttype',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ventilationtype',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='ventilationtype',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='ventilationtype',
            name='user',
        ),
    ]
