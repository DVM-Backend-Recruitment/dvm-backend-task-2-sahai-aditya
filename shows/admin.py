from django.contrib import admin
from .models import Theatre, TheatreAdmin, Movie, Show

admin.site.register(Theatre)
admin.site.register(TheatreAdmin)
admin.site.register(Movie)
admin.site.register(Show)