from .models import Sector

from django import forms

class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }
