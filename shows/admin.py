from django.contrib import admin
from .models import Theatre, TheatreAdmin, Movie

admin.site.register(Theatre)
admin.site.register(TheatreAdmin)
admin.site.register(Movie)