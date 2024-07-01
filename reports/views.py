from django.shortcuts import render
from gantt.models import Gantt

def equipamento_report(request, equipamento_id):
    # Filtrar as tarefas do Gantt para o equipamento selecionado
    tasks = Gantt.objects.filter(equipment_id=equipamento_id)
    # Aqui você pode gerar o relatório com base nas tarefas filtradas
    # Por exemplo, você pode calcular a duração total das tarefas ou qualquer outra informação relevante
    return render(request, 'reports/equipamento_report.html', {'tasks': tasks})
