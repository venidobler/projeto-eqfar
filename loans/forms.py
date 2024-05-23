from django import forms
from .models import Emprestimo

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['equipamento', 'responsavel', 'data_emprestimo', 'data_devolucao']

class DevolucaoForm(forms.Form):
    equipamento = forms.ModelChoiceField(queryset=Emprestimo.objects.filter(data_devolucao__isnull=True).values_list('equipamento', flat=True))
    data_devolucao = forms.DateField()
