# Generated by Django 3.2 on 2023-02-03 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_movie_runtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]
