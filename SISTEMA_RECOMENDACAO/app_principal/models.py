from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    nota = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Notas de 1 a 5
    comentario = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.item.nome} - {self.nota}"
