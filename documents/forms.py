from .models import Document
from rooms.models import Room

from django import forms
from django.shortcuts import get_object_or_404


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'category', 'description', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do Documento'
            }),
            'category': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição do Documento',
                'rows': 5
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }

        labels = {
            'name': 'Nome',
            'category': 'Categoria',
            'description': 'Descrição',
            'photo': 'Foto (Arquivo)',
        }

    def __init__(self, *args, **kwargs):
        room_pk = kwargs.pop('room_pk', None)
        print(f"room_pk: {room_pk}")  # Debug
        super(DocumentForm, self).__init__(*args, **kwargs)
        if room_pk:
            room = get_object_or_404(Room, pk=room_pk)
            self.fields['category'].queryset = room.categories.all()
