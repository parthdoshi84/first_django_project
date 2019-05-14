from django.contrib import admin

# Register your models here.
from imdb.models import Actor,Director,Producer, Movie

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Producer)
admin.site.register(Movie)