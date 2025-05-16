from django.http import HttpResponse
from django.template import loader

def teste(request):
    template = loader.get_template('paginateste.html')
    context = {
        "empresa": "AlugaFácil",
        "mensagem": "Bem-vindo ao sistema de aluguel de carros!"
    }
    return HttpResponse(template.render(context, request))
