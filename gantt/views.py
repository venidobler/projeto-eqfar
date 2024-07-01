from django.shortcuts import render
from gantt.models import Gantt
from equipments.models import Equipamento
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from django.http import HttpResponse
import csv

def index(request):
    equipments = Equipamento.objects.all()
    selected_equipment_id = request.GET.get('equipment')
    
    if selected_equipment_id:
        qs = Gantt.objects.filter(equipment_id=selected_equipment_id)
    else:
        qs = Gantt.objects.all()

    projects_data = [
        {
            'Project': x.name,
            'Start': x.start_date,
            'Finish': x.finish_date,
        } for x in qs
    ]
    df = pd.DataFrame(projects_data)
    fig = px.timeline(
        df, x_start="Start", x_end="Finish", y="Project"
    )
    
    fig.update_yaxes(autorange="reversed")
    gantt_plot = plot(fig, output_type="div")
    context = {'plot_div': gantt_plot, 'equipments': equipments, 'selected_equipment_id': selected_equipment_id}
    return render(request, 'pages/index.html', context)

def exportar_relatorio(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        qs = Gantt.objects.filter(start_date__gte=start_date, finish_date__lte=end_date)
    else:
        qs = Gantt.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="relatorio.csv"'

    writer = csv.writer(response)
    writer.writerow(['Projeto', 'Data de Início', 'Data de Término'])

    for task in qs:
        writer.writerow([task.name, task.start_date, task.finish_date])

    return response

def relatorio(request):
    return render(request, 'pages/relatorio.html')
