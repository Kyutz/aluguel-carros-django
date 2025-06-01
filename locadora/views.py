from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.template import loader
from .models import Carro, Cliente, Locacao 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import LocacaoForm

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

def dashboard(request):
    carros_alugados = Locacao.objects.filter(status='ativo').count()
    carros_disponiveis = Carro.objects.filter(disponibilidade=True).count()
    total_clientes = Cliente.objects.count()
    locacoes_ativas = Locacao.objects.filter(status='ativo').count()

    context = {
        'carros_alugados': carros_alugados,
        'carros_disponiveis': carros_disponiveis,
        'total_clientes': total_clientes,
        'locacoes_ativas': locacoes_ativas,
    }
    return render(request, 'dashboard.html', context)

@login_required
def alugar_carro(request):
    if request.method == 'POST':
        form = LocacaoForm(request.POST)
        if form.is_valid():
            locacao = form.save(commit=False)
            locacao.cliente = Cliente.objects.get(user=request.user)
            locacao.status = 'ativo'
            locacao.save()
            locacao.carro.disponibilidade = False
            locacao.carro.save()
            messages.success(request, 'Carro alugado com sucesso!')
            return redirect('listar_locacoes')
    else:
        form = LocacaoForm()
    
    return render(request, 'alugar_carro.html', {'form': form})

