from django.db import models


class Movie(models.Model):
    the_movie_db_id = models.IntegerField(null=False, blank=False, unique=True)
    movie_title = models.CharField('Nome do filme', max_length=50, null=False, blank=False)
    overview = models.CharField('Gênero', max_length=500, default='')
    date = models.DateField('Data de lançamento',default='2000-01-01', blank=True)
    url_image = models.CharField(max_length=100)
