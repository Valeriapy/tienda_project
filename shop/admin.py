from django.contrib import admin
from .models import Remera

@admin.register(Remera)
class RemeraAdmin(admin.ModelAdmin):
    list_display = ('marca', 'color', 'lisa', 'genero', 'get_talle_display')
    list_filter = ('talle', 'genero', 'lisa')
    search_fields = ('marca', 'color')
