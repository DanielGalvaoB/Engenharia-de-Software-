from django.urls import path
from . import views  # Certifique-se de importar views corretamente

urlpatterns = [
    path('', views.home, name='home'),  # Aqui a função home precisa estar definida em views.py
]
