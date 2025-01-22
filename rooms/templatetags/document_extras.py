from django import template
import os

register = template.Library()

@register.filter
def file_extension(url):
    _, ext = os.path.splitext(url)
    return ext.lower()
