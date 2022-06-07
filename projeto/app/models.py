from django.db import models
from requests import delete

# Create your models here
class Cidade(models.Model):
    nome = models.CharField( max_length=50)

    def __str__(self):
        return self.nome 
class Empresa(models.Model):
    nome = models.CharField(max_length=75)
    endereco = models.CharField(max_length=225)
    cidade_name = models.CharField( max_length=50)
    

    def __str__(self):
        return self.nome 

class Produto(models.Model):
    nome = models.CharField(max_length=75)
    descricao = models.TextField()
    contato = models.CharField(max_length=225)
    empresa = models.CharField(max_length=75)

    def __str__(self):
        return self.nome 


class Local(models.Model):
    nome = models.CharField( max_length=50)
    descricao = models.TextField()
    cidade_name = models.CharField( max_length=50)
    
    def __str__(self):
        return self.nome 


