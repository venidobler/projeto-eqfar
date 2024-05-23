from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.utils.dateparse import parse_date
from django.http import HttpResponseBadRequest

from equipments.models import Equipamento
from loans.models import Emprestimo
from users.models import Usuario

def emprestimo_view(request):
    if request.method == 'POST':
        # Captura dos dados do formulário
        equipamento_id = request.POST.get('equipamento')
        responsavel_id = request.POST.get('responsavel')
        data_emprestimo = request.POST.get('data_emprestimo')

        # Validação da data
        if not data_emprestimo:
            return HttpResponseBadRequest("Data de Empréstimo é obrigatória.")
        
        data_emprestimo = parse_date(data_emprestimo)
        if data_emprestimo is None:
            return HttpResponseBadRequest("Formato de data inválido. Use o formato YYYY-MM-DD.")
        
        # Criar uma instância de empréstimo e salvar
        emprestimo = Emprestimo.objects.create(
            equipamento_id=equipamento_id,
            responsavel_id=responsavel_id,
            data_emprestimo=data_emprestimo
        )
        
        # Atualizar o status do equipamento para emprestado
        equipamento = Equipamento.objects.get(id=equipamento_id)
        equipamento.status = False
        equipamento.save()

        return redirect('index_gantt')

    # Se não for POST, renderiza a página de empréstimo sem o formulário
    equipamentos = Equipamento.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, 'pages/emprestimo.html', {'equipamentos': equipamentos, 'usuarios': usuarios})


def devolucao_view(request):
    if request.method == 'POST':
        # Captura dos dados do formulário
        equipamento_id = request.POST.get('equipamento')
        data_devolucao = request.POST.get('data_devolucao')

        # Validação da data
        if not data_devolucao:
            return HttpResponseBadRequest("Data de Devolução é obrigatória.")
        
        data_devolucao = parse_date(data_devolucao)
        if data_devolucao is None:
            return HttpResponseBadRequest("Formato de data inválido. Use o formato YYYY-MM-DD.")
        
        # Encontrar o empréstimo correspondente e atualizar a data de devolução
        emprestimo = Emprestimo.objects.get(equipamento_id=equipamento_id, data_devolucao=None)
        emprestimo.data_devolucao = data_devolucao
        emprestimo.save()
        
        # Atualizar o status do equipamento para ativo
        equipamento = emprestimo.equipamento
        equipamento.status = True
        equipamento.save()
        
        return redirect('devolucao_view')

    # Se não for POST, renderiza a página de devolução sem o formulário
    emprestimos = Emprestimo.objects.filter(data_devolucao=None)
    return render(request, 'pages/devolucao.html', {'emprestimos': emprestimos})
