# Generated by Django 3.2 on 2023-02-03 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230203_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='runtime',
        ),
    ]