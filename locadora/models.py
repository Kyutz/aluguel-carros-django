from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    documento_identidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    placa = models.CharField(max_length=20)
    cor = models.CharField(max_length=50)
    disponibilidade = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"

class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cliente.nome} - {self.carro.modelo} ({self.data_inicio} a {self.data_fim})"

class Pagamento(models.Model):
    locacao = models.ForeignKey(Locacao, on_delete=models.CASCADE)
    data_pagamento = models.DateField()
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=50)
    status_pagamento = models.CharField(max_length=50)

    def __str__(self):
        return f"Pagamento de {self.valor_pago} em {self.data_pagamento} - {self.status_pagamento}"
