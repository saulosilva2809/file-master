from .models import Room

from django.contrib import admin


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'sector')
    search_fields = ('name', 'owner', 'sector')
