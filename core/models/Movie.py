from django.db import models


class Movie(models.Model):
    the_movie_db_id = models.IntegerField(null=False, blank=False, unique=True)
    movie_title = models.CharField('Nome do filme', max_length=50, null=False, blank=False)
    genre = models.CharField('Gênero', max_length=20)
    runtime = models.IntegerField('duração')
    year = models.IntegerField('ano')
    url_image = models.CharField(max_length=100)
