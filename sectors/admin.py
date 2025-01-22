from .models import Sector

from django.contrib import admin


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
