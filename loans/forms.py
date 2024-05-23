# loans/forms.py

from django import forms
from .models import Emprestimo
from equipments.models import Equipamento

class EmprestimoForm(forms.ModelForm):
    data_emprestimo = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={'placeholder': 'dd/mm/yyyy', 'class': 'w-full h-10 border border-black rounded-md'})
    )

    class Meta:
        model = Emprestimo
        fields = ['equipamento', 'responsavel', 'data_emprestimo']
        widgets = {
            'equipamento': forms.Select(attrs={'class': 'w-full h-10 border border-black rounded-md'}),
            'responsavel': forms.Select(attrs={'class': 'w-full h-10 border border-black rounded-md'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar os equipamentos ativos (status=True)
        self.fields['equipamento'].queryset = Equipamento.objects.filter(status=True)
        
        
class DevolucaoForm(forms.ModelForm):
    id_emprestimo = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Emprestimo
        fields = ['equipamento', 'data_devolucao']
        widgets = {
            'equipamento': forms.Select(attrs={'class': 'w-full h-10 border border-black rounded-md'}),
            'data_devolucao': forms.DateInput(attrs={'placeholder': 'dd/mm/yyyy', 'class': 'w-full h-10 border border-black rounded-md'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar os equipamentos disponíveis (status=False)
        self.fields['equipamento'].queryset = Equipamento.objects.filter(status=False)


        
