from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, null=False) 
    idade = models.IntegerField(null=False) 
    cpf = models.CharField(max_length=11, null=False, unique=True) 
    rg = models.CharField(max_length=9, null=False, unique=True)
    email = models.CharField(max_length=50, null=False)
    telefone = models.CharField(max_length=11, null=False)  
    cep = models.CharField(max_length=8, null=False)  
    endereco = models.CharField(max_length=100, null=False) 
    numero = models.IntegerField(max_length=5, null=False) 
    bairro = models.CharField(max_length=100, null=False)
    cidade = models.CharField(max_length=100, null=False)
    complemento = models.CharField(max_length=100, null=False) 
    uf = models.CharField(max_length=2, null=False)  
    cargo = models.CharField(max_length=50, null=False)
    objects = models.Manager()
