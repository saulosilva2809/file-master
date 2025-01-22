from .models import Position

from django import forms


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name', 'description']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }

