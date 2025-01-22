from django import forms
from django.contrib.auth.models import Permission


class PermissionForm(forms.Form):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'form-check-input'}
        ),
        label='Selecione as Permissões',
        required=True,
        help_text='Selecione uma ou mais permissões para adicionar ao usuário.'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Organiza as permissões por content type
        self.fields['permissions'].queryset = Permission.objects.all().order_by(
            'content_type__app_label', 'content_type__model'
        ) 