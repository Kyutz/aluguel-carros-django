from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Carro, Locacao  # importa o model

def home(request):
    template = loader.get_template('home.html')  
    context = {
        "empresa": "AlugaFácil",
        "mensagem": "Bem-vindo ao sistema de aluguel de carros!"
    }
    return HttpResponse(template.render(context, request))

def carros(request):
    template = loader.get_template('carros.html')
    lista_carros = Carro.objects.filter(disponibilidade=True)  # só carros disponíveis
    
    context = {
        "carros": lista_carros,
    }
    
    return HttpResponse(template.render(context, request))

def listar_locacoes(request):
    locacoes = Locacao.objects.select_related('cliente', 'carro').all()
    return render(request, 'locacoes.html', {'locacoes': locacoes})