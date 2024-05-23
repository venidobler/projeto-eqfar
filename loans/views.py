
from django.shortcuts import render, redirect
from equipments.models import Equipamento
from loans.forms import DevolucaoForm, EmprestimoForm
from loans.models import Emprestimo
from django.http import HttpResponse, HttpResponseNotFound

def emprestimo_view(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            equipamento_id = emprestimo.equipamento_id
            try:
                equipamento = Equipamento.objects.get(id_equipamento=equipamento_id)
            except Equipamento.DoesNotExist:
                return HttpResponseNotFound("O equipamento não foi encontrado.")
            else:
                if equipamento.status:  # Verifica se o equipamento está disponível
                    equipamento.status = False
                    equipamento.save()
                    emprestimo.save()
                    return redirect('index_gantt')
                else:
                    return HttpResponse("Este equipamento não está disponível para empréstimo.")
        else:
            return render(request, 'pages/emprestimo.html', {'form': form})
    form = EmprestimoForm()
    return render(request, 'pages/emprestimo.html', {'form': form})



def devolucao_view(request):
    if request.method == 'POST':
        form = DevolucaoForm(request.POST)
        if form.is_valid():
            id_emprestimo = form.cleaned_data['id_emprestimo']
            data_devolucao = form.cleaned_data['data_devolucao']
            
            try:
                emprestimo = Emprestimo.objects.get(pk=id_emprestimo)
            except Emprestimo.DoesNotExist:
                # Trate o caso em que o empréstimo não existe
                return HttpResponseNotFound("O empréstimo não foi encontrado.")
            else:
                # Verificar se o equipamento associado ao empréstimo está atualmente emprestado
                if emprestimo.equipamento.status == False:
                    # Marcar o equipamento como disponível novamente
                    emprestimo.equipamento.status = True
                    emprestimo.equipamento.save()
                # Atualizar a data de devolução do empréstimo
                emprestimo.data_devolucao = data_devolucao
                emprestimo.save()
                # Redirecionar para a tela index_gantt
                return redirect('index_gantt')
    else:
        form = DevolucaoForm()
    return render(request, 'pages/devolucao.html', {'form': form})



