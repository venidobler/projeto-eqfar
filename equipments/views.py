from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipamento
from .forms import EquipamentoForm, EquipamentoEditForm

def home_equipamento(request):
    return render(request, 'home/home_equipamento.html')

def cadastro_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_equipamento')
    else:
        form = EquipamentoForm()

    return render(request, 'equipamentos/cadastro_equipamento.html', {'form': form})

def listagem_equipamento(request):
    equipamentos = {
        'equipamentos': Equipamento.objects.all().order_by('id_equipamento')
    }
    return render(request, 'equipamentos/listagem_equipamento.html', equipamentos)

def editar_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, id_equipamento=equipamento_id)

    if request.method == 'POST':
        form = EquipamentoEditForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('listagem_equipamento')
    else:
        form = EquipamentoEditForm(instance=equipamento)

    return render(request, 'equipamentos/editar_equipamento.html', {'form': form, 'equipamento_id': equipamento_id})

def delete_equipment(request, equipamento_id):
    usuario = get_object_or_404(Equipamento, pk=equipamento_id)
    usuario.delete()
    return redirect('listagem_equipamento')