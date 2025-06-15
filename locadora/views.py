from datetime import date
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.template import loader
from .models import Carro, Cliente, Locacao, Pagamento 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import LocacaoForm, PagamentoForm 
from django.contrib.auth import logout as logout_django

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

@login_required
def carro_detalhes(request, id):
    carro = get_object_or_404(Carro, id=id)

    if request.method == 'POST':
        form = LocacaoForm(request.POST)
        if form.is_valid():
            with transaction.atomic(): 
                locacao = form.save(commit=False)
                locacao.carro = carro
                locacao.cliente = Cliente.objects.get(user=request.user)
                locacao.status = 'ativo' 
                locacao.save()

                carro.disponibilidade = False
                carro.save()

                messages.success(request, 'Carro alugado com sucesso! Agora, finalize o pagamento.')
                return redirect('realizar_pagamento', locacao_id=locacao.id)
        else:
            context = {
                'carro': carro,
                'form': form, 
            }
            return render(request, 'carro_detalhes.html', context)
    else:
        form = LocacaoForm() 

    context = {
        'carro': carro,
        'form': form,
    }
    return render(request, 'carro_detalhes.html', context)

@login_required
def dashboard(request):
    carros_disponiveis = Carro.objects.filter(disponibilidade=True).count()
    carros_alugados    = Locacao.objects.filter(cliente__user=request.user).count()
    locacoes_ativas    = Locacao.objects.filter(cliente__user=request.user, status='ativo').count()

    context = {
        'usuario':            request.user.username,
        'carros_disponiveis': carros_disponiveis,
        'carros_alugados':    carros_alugados,
        'locacoes_ativas':    locacoes_ativas,
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

@login_required
def realizar_pagamento(request, locacao_id):
    locacao = get_object_or_404(Locacao, id=locacao_id)

    if Pagamento.objects.filter(locacao=locacao).exists(): 
        messages.info(request, 'Esta locação já foi paga.')
        return redirect('listar_locacoes') 

    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            with transaction.atomic(): 
                pagamento = form.save(commit=False)
                pagamento.locacao = locacao
                pagamento.data_pagamento = date.today()
                pagamento.valor_pago = locacao.valor_total 
                pagamento.status_pagamento = 'pago'

                pagamento.save()

                messages.success(request, 'Pagamento realizado com sucesso!')
                return redirect('listar_locacoes')
        else:
            messages.error(request, 'Erro ao processar o pagamento. Verifique os dados.')
    else:
        form = PagamentoForm()

    context = {
        'locacao': locacao,
        'form': form,
        'valor_a_pagar': locacao.valor_total, 
    }
    return render(request, 'realizar_pagamento.html', context)

def logout(request):
    logout_django(request)
    return redirect('login')