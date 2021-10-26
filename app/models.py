from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarefa(models.Model):
    PERECIBILIDADE_CHOICES = [
        ("A", "Alta"),
        ("N", "Normal"),
        ("B", "Baixa"),
    ]
    UNIDADE_CHOICES = [
        ("BOCA DO RIO", "BOCA DO RIO"),
        ("CENTRO", "CENTRO"),
        ("IMBUI", "IMBUI"),
        ("PITUBA", "PITUBA"),
    ]
    unidade = models.CharField(max_length=20, choices=UNIDADE_CHOICES, null=False, blank=False)
    fornecedor = models.CharField(max_length=40, null=False, blank=False)
    produto = models.CharField(max_length=40, null=False, blank=False)
    codigo_barra = models.BigIntegerField(null=False, blank=False)
    data_fabricacao = models.DateField(null=False, blank=False)
    data_validade = models.DateField(null=False, blank=False)
    custo_unidade = models.FloatField(null=False, blank=False)
    quant_compra = models.IntegerField(null=False, blank=False)
    preco_venda = models.FloatField(null=False, blank=False)
    quant_venda = models.IntegerField(null=False, blank=False)
    perecibilidade = models.CharField(max_length=1, choices=PERECIBILIDADE_CHOICES, null=False, blank=False)
    foto_produto = models.ImageField(upload_to='images/')
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
