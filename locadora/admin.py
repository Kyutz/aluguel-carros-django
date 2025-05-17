from django.contrib import admin
from .models import Cliente, Carro, Locacao, Pagamento

admin.site.register(Cliente)
admin.site.register(Carro)
admin.site.register(Locacao)
admin.site.register(Pagamento)