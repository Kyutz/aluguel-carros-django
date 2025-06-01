from django.urls import path
from .views import home, listar_locacoes, carros
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('carros/', carros, name='carros'),
    path('locacoes/', listar_locacoes, name='listar_locacoes'),
    path('auth/cadastro', views.cadastro, name='cadastro'),
    path('auth/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
