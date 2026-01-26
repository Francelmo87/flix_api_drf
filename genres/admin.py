from django.contrib import admin
from .models import Genre


@admin.register(Genre)
class GenrAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
