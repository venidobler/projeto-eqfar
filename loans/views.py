from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Emprestimo
from equipments.models import Equipamento
from users.models import Usuario
from django.utils import timezone

def emprestimo_view(request):
    if request.method == 'POST':
        equipamento_id = request.POST['equipamento']
        responsavel_id = request.POST['responsavel']
        data_emprestimo = request.POST['data_emprestimo']
        data_devolucao = request.POST['data_devolucao']
        
        equipamento = Equipamento.objects.get(id=equipamento_id)
        responsavel = Usuario.objects.get(id=responsavel_id)
        
        Emprestimo.objects.create(
            equipamento=equipamento,
            responsavel=responsavel,
            data_emprestimo=data_emprestimo,
            data_devolucao=data_devolucao
        )
        return redirect('emprestimo_view')
    
    equipamentos = Equipamento.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, 'emprestimo.html', {'equipamentos': equipamentos, 'usuarios': usuarios})

def devolucao_view(request):
    if request.method == 'POST':
        equipamento_id = request.POST['equipamento']
        data_devolucao = request.POST['data_devolucao']
        
        emprestimo = Emprestimo.objects.get(equipamento_id=equipamento_id, data_devolucao=None)
        emprestimo.data_devolucao = data_devolucao
        emprestimo.save()
        
        return redirect('devolucao_view')
    
    emprestimos = Emprestimo.objects.filter(data_devolucao=None)
    return render(request, 'devolucao.html', {'emprestimos': emprestimos})
