from django import forms
from .models import Locacao

class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = ['data_inicio', 'data_fim']

