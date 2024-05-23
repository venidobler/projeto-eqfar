from django import forms
from .models import Equipamento


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ["nome", "tag", "modelo", "marca", "status"]

        

class EquipamentoEditForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ["nome", "tag", "modelo", "marca", "status"]
    

    

   