from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Cliente, Carro, Locacao, Pagamento

class AnoFaixaFilter(admin.SimpleListFilter):
    title = _('faixa de ano')
    parameter_name = 'ano_faixa'

    def lookups(self, request, model_admin):
        return [
            ('2000s', _('2000-2009')),
            ('2010s', _('2010-2019')),
            ('2020s', _('2020-')),
        ]

    def queryset(self, request, queryset):
        if self.value() == '2000s':
            return queryset.filter(ano__gte=2000, ano__lte=2009)
        if self.value() == '2010s':
            return queryset.filter(ano__gte=2010, ano__lte=2019)
        if self.value() == '2020s':
            return queryset.filter(ano__gte=2020)
        return queryset

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefone', 'documento_identidade')
    search_fields = ('user__username', 'documento_identidade')

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano', 'disponibilidade')
    list_filter = ('marca', 'disponibilidade', AnoFaixaFilter)
    search_fields = ('modelo', 'marca', 'placa')

@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'carro', 'data_inicio', 'data_fim', 'status')
    list_filter = ('status',)
    search_fields = ('cliente__user__username', 'carro__modelo')

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('locacao', 'data_pagamento', 'valor_pago', 'forma_pagamento', 'status_pagamento')
    list_filter = ('forma_pagamento', 'status_pagamento')
    search_fields = ('locacao__cliente__user__username',)
