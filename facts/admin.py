from django.contrib import admin
from .models import Song, Artist, Fact
# Register your models here.
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Fact)