from django.shortcuts import render
from gantt.models import Gantt
from equipments.models import Equipamento  # Importe o modelo Equipamento aqui
import pandas as pd
from plotly.offline import plot
import plotly.express as px

def index(request):
    equipments = Equipamento.objects.all()  # Obtém todos os equipamentos para a opção de seleção
    selected_equipment_id = request.GET.get('equipment')  # Obtém o ID do equipamento selecionado (se houver)
    
    if selected_equipment_id:
        # Filtra as tarefas pelo equipamento selecionado
        qs = Gantt.objects.filter(equipment_id=selected_equipment_id)
    else:
        # Caso nenhum equipamento seja selecionado, retorna todas as tarefas
        qs = Gantt.objects.all()

    projects_data = [
        {
            'Project': x.name,
            'Start': x.start_date,
            'Finish': x.finish_date,
            'Responsible': x.responsible.username
        } for x in qs
    ]
    df = pd.DataFrame(projects_data)
    fig = px.timeline(
        df, x_start="Start", x_end="Finish", y="Project", color="Responsible"
    )
    fig.update_yaxes(autorange="reversed")
    gantt_plot = plot(fig, output_type="div")
    context = {'plot_div': gantt_plot, 'equipments': equipments, 'selected_equipment_id': selected_equipment_id}
    return render(request, 'pages/index.html', context)
