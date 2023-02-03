from django.contrib import admin
from core.models import UserApp, Movie, FavoriteMovie


class ListingUsers(admin.ModelAdmin):
    list_display = ('id', 'fullname')


admin.site.register(UserApp, ListingUsers)


class ListingMovie(admin.ModelAdmin):
    list_display = ('id', 'movie_title')


admin.site.register(Movie, ListingMovie)


class ListingFavoriteMovie(admin.ModelAdmin):
    list_display = ('user', 'movie')


admin.site.register(FavoriteMovie, ListingFavoriteMovie)
