from django.contrib import admin
from . import models


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year', 'genre', 'daily_rental_rate')
    exclude = ('creation_date',)


admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Movie, MovieAdmin)
