from django.db import models

from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=225)
    cnpj = models.CharField(max_length=50)
    categoria =models.CharField(max_length=100)

    

