from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.template import loader
from .models import Carro, Locacao  # importa o model
from django.contrib.auth.forms import UserCreationForm

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

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})

def carro_detalhes(request, id):
    carro = get_object_or_404(Carro, id=id)
    template = loader.get_template('carro_detalhes.html')
    context = {
        'carro': carro
    }
    return HttpResponse(template.render(context, request))