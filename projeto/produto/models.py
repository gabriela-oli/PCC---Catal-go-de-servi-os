from django.db import models

class Produto(models.Model):
    nome = models.CharField( max_length=175)
    descricao = models.TextField()
    valor = models.IntegerField()
    
