from django.urls import path
from .views import home, listar_locacoes, carros
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('carros/', carros, name='carros'),
    path('locacoes/', listar_locacoes, name='listar_locacoes'),
    path('auth/cadastro', views.cadastro, name='cadastro'),
]
