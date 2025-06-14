from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    placa = models.CharField(max_length=20)
    cor = models.CharField(max_length=50)
    disponibilidade = models.BooleanField(default=True)
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"

class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    status = models.CharField(max_length=50)
    
    def save(self, *args, **kwargs):
        dias = (self.data_fim - self.data_inicio).days + 1
        self.valor_total = dias * self.carro.valor_diaria
        super().save(*args, **kwargs)

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

@receiver(post_save, sender=User)
def criar_cliente_automaticamente(sender, instance, created, **kwargs):
    if created and not instance.is_superuser: 
        Cliente.objects.create(
            user=instance,
            nome=instance.username,
        )