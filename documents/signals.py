from .models import Document

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Document)
def post_save_document(sender, instance, created, **kwargs):
    if created and hasattr(instance, '_room'):
        room = instance._room
        room.documents.add(instance)  # Associa o documento à sala
        del instance._room  # Remove o atributo temporário
