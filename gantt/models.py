from django.db import models
from django.contrib.auth.models import User
from equipments.models import Equipamento

class Gantt(models.Model):
    name = models.CharField(max_length=200) 
    start_date = models.DateField()
 
    week_number = models.CharField(max_length=2, blank=True)
    finish_date = models.DateField()
    equipment = models.ForeignKey(Equipamento, on_delete=models.CASCADE, null=True, default=None)  # Adicionando o campo de equipamento

#string representation method
    def __str__(self):
        return str(self.name)
#overiding the save method
    def save(self, *args, **kwargs):
        print(self.start_date.isocalendar()[1])
        if self.week_number == "":
            self.week_number = self.start_date.isocalendar()[1]
        super().save(*args, **kwargs)
        
        