
from django.shortcuts import render, redirect
from equipments.models import Equipamento
from loans.forms import DevolucaoForm, EmprestimoForm
from django.http import HttpResponseNotFound

def emprestimo_view(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.save()
            equipamento = Equipamento.objects.get(id_equipamento=emprestimo.equipamento_id)
            equipamento.status = False
            equipamento.save()
            return redirect('index_gantt')
        else:
            return render(request, 'pages/emprestimo.html', {'form': form})
    form = EmprestimoForm()
    return render(request, 'pages/emprestimo.html', {'form': form})





def devolucao_view(request):
    if request.method == 'POST':
        form = DevolucaoForm(request.POST)
        if form.is_valid():
            equipamento_id = form.cleaned_data['equipamento']
            data_devolucao = form.cleaned_data['data_devolucao']
            
            try:
                equipamento = Equipamento.objects.get(pk=equipamento_id)
            except Equipamento.DoesNotExist:
                # Trate o caso em que o equipamento não existe
                return HttpResponseNotFound("O equipamento não foi encontrado.")
            else:
                # Verificar se o equipamento já está marcado como ativo
                if not equipamento.status:
                    # Marcar o equipamento como disponível novamente
                    equipamento.status = True
                    equipamento.save()
                # Redirecionar para a tela index_gantt
                return redirect('index_gantt')
    else:
        form = DevolucaoForm()
    return render(request, 'pages/devolucao.html', {'form': form})



