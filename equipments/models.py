from django.db import models

# Create your models here.
class Equipamento(models.Model):
    id_equipamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    tag = models.CharField(max_lenght = 100)
    modelo = models.CharField(max_lenght = 100)
    marca = models.CharField(max_lenght = 100)
    objects = models.Manager()