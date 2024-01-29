from django.db import models

# Create your models here.
class Interacao(models.Model):
    data_contato = models.CharField(default="", max_length=100)
    canal = models.CharField(max_length=150)
    contato = models.CharField(max_length=100)
    detalhes = models.TextField()
    ocasiao = models.CharField(default="", max_length=100)
    data_evento = models.CharField(default="", max_length=100)
    primeira_cor = models.CharField(default="", max_length=100)
    segunda_cor = models.CharField(default="", max_length=100)
    tamanho = models.CharField(default="", max_length=100)
    locacao = models.CharField(default="", max_length=100)
    motivo = models.CharField(default="", max_length=100)
    motivo2 = models.CharField(default="", max_length=100)