# Em loans/views.py

# loans/views.py

from django.shortcuts import redirect, render

from users.models import Usuario
from .models import Emprestimo
from equipments.models import Equipamento
from .forms import EmprestimoForm

def emprestimo_view(request):
    form = EmprestimoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Salvar o empréstimo
            emprestimo = form.save(commit=False)
            
            # Atualizar o status do equipamento para inativo
            equipamento_emprestado = emprestimo.equipamento
            equipamento_emprestado.status = False
            equipamento_emprestado.save()

            # Salvar o empréstimo no banco de dados
            emprestimo.save()

            return redirect('index_gantt')
    
    equipamentos = Equipamento.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, 'pages/emprestimo.html', {'form': form, 'equipamentos': equipamentos, 'usuarios': usuarios})

def devolucao_view(request):
    if request.method == 'POST':
        equipamento_id = request.POST['equipamento']
        data_devolucao = request.POST['data_devolucao']
        
        emprestimo = Emprestimo.objects.get(equipamento_id=equipamento_id, data_devolucao=None)
        emprestimo.data_devolucao = data_devolucao
        emprestimo.save()
        
        # Atualiza o status do equipamento para ativo ao devolver
        equipamento = emprestimo.equipamento
        equipamento.status = True
        equipamento.save()
        
        return redirect('devolucao_view')
    
    emprestimos = Emprestimo.objects.filter(data_devolucao=None)
    return render(request, 'pages/devolucao.html', {'emprestimos': emprestimos})
