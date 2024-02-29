from django.db import models

# Create your models here.
class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    objects = models.Manager()