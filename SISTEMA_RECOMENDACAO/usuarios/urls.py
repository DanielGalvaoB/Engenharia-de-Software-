from django.urls import path
from .views import registrar, logar, deslogar

urlpatterns = [
    path('registrar/', registrar, name='registrar'),
    path('login/', logar, name='login'),
    path('logout/', deslogar, name='logout'),
]
