from django.urls import path
from .views import home
from locadora import views

urlpatterns = [
    path('', home, name='home'),
    path('carros/', views.carros, name='carros'),
]
