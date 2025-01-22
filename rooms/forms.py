from .models import Room

from django import forms

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'password']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da Sala'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Senha da Sala'
            }),
        }

        labels = {
            'name': 'Nome',
            'password': 'Senha',
        }
