from django.db import models
from equipments.models import Equipamento
from users.models import Usuario

class Emprestimo(models.Model):
    id_emprestimo = models.AutoField(primary_key=True)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, null=True, default=None)
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)  # Permite valores nulos
    objects = models.Manager()
