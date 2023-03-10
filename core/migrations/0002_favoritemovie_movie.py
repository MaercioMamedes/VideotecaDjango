# Generated by Django 3.2 on 2023-02-02 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_movie_db_id', models.IntegerField(unique=True)),
                ('movie_title', models.CharField(max_length=50, verbose_name='Nome do filme')),
                ('genre', models.CharField(max_length=20, verbose_name='Gênero')),
                ('runtime', models.IntegerField(verbose_name='duração')),
                ('year', models.IntegerField(verbose_name='ano')),
                ('url_image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
