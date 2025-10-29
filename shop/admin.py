
from django.contrib import admin
from .models import Remera

@admin.register(Remera)
class RemeraAdmin(admin.ModelAdmin):
    list_display = ('marca', 'talle', 'color', 'lisa', 'genero')
