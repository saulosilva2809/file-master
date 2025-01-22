from .models import Document

from django.contrib import admin


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploader', 'date_upload')
    search_fields = ('name', 'uploader', 'date_upload')
