from django import forms
from .models import Locacao, Pagamento

class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = ['data_inicio', 'data_fim']

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        # Não inclua 'locacao', 'data_pagamento', 'valor_pago' aqui
        # Eles serão definidos na view
        fields = ['forma_pagamento'] 
        # Podemos pré-definir status_pagamento na view
        # fields = ['forma_pagamento', 'status_pagamento'] # Se quiser que o usuário escolha o status inicial

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exemplo: Adicionar um campo extra para valor, se necessário
        # self.fields['valor_a_pagar'] = forms.DecimalField(label="Valor a Pagar", required=False, disabled=True)
        # self.fields['valor_a_pagar'].widget.attrs['readonly'] = True